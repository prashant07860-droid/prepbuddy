import React, { useState, useEffect, useCallback } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Platform,
} from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';

// Get API base URL - use environment variable or fallback to relative path
const getApiBaseUrl = () => {
  if (Platform.OS === 'web') {
    // On web, try to use the backend URL from environment
    const backendUrl = process.env.EXPO_PUBLIC_BACKEND_URL;
    if (backendUrl) {
      return backendUrl;
    }
  }
  // Fallback to relative path
  return '';
};

interface Paper {
  id: string;
  subject_id: string;
  paper_number: number;
  is_master: boolean;
  title: string;
  total_questions: number;
  duration_minutes: number;
}

interface Subject {
  id: string;
  name: string;
  color: string;
  description: string;
}

interface Attempt {
  id: string;
  paper_id: string;
  score_percentage: number;
}

export default function SubjectScreen() {
  const router = useRouter();
  const { id } = useLocalSearchParams<{ id: string }>();
  const [activeTab, setActiveTab] = useState<'practice' | 'master'>('practice');
  
  const [subject, setSubject] = useState<Subject | null>(null);
  const [papers, setPapers] = useState<Paper[]>([]);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchData = useCallback(async () => {
    if (!id) return;
    
    try {
      setIsLoading(true);
      const apiBase = getApiBaseUrl();
      
      // Fetch subject info from API
      const subjectRes = await fetch(`${apiBase}/api/subjects/${id}`);
      if (subjectRes.ok) {
        const subjectData = await subjectRes.json();
        setSubject(subjectData);
      }
      
      // Fetch papers from API
      const papersRes = await fetch(`${apiBase}/api/subjects/${id}/papers`);
      if (papersRes.ok) {
        const papersData = await papersRes.json();
        setPapers(papersData);
      }

      // Fetch attempts
      const attemptsRes = await fetch(`${apiBase}/api/attempts?subject_id=${id}`);
      if (attemptsRes.ok) {
        const attemptsData = await attemptsRes.json();
        setAttempts(attemptsData);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setIsLoading(false);
    }
  }, [id]);

  useEffect(() => {
    if (typeof window !== 'undefined' && id) {
      fetchData();
    }
  }, [id, fetchData]);

  // Separate papers into categories
  const regularPapers = papers.filter((p) => !p.is_master && !p.title.includes('(Extreme)'));
  const extremePapers = papers.filter((p) => p.title.includes('(Extreme)'));
  const masterPaper = papers.find((p) => p.is_master);

  const getBestScore = (paperId: string) => {
    const paperAttempts = attempts.filter((a) => a.paper_id === paperId);
    if (paperAttempts.length === 0) return null;
    return Math.max(...paperAttempts.map((a) => a.score_percentage));
  };

  const navigateToPaper = (paperId: string) => {
    router.push(`/exam/${paperId}`);
  };

  const isExtremePaper = (paper: Paper) => paper.title.includes('(Extreme)');

  const renderPaperCard = (paper: Paper) => {
    const bestScore = getBestScore(paper.id);
    const hasAttempt = bestScore !== null;
    const isExtreme = isExtremePaper(paper);

    return (
      <TouchableOpacity
        key={paper.id}
        style={[styles.paperCard, isExtreme && styles.extremePaperCard]}
        onPress={() => navigateToPaper(paper.id)}
        activeOpacity={0.7}
      >
        <View style={styles.paperLeft}>
          <View style={[
            styles.paperIcon, 
            paper.is_master && styles.masterIcon,
            isExtreme && styles.extremeIcon
          ]}>
            <MaterialCommunityIcons
              name={paper.is_master ? 'star' : isExtreme ? 'fire' : 'file-document'}
              size={20}
              color={paper.is_master ? '#F59E0B' : isExtreme ? '#EF4444' : '#3B82F6'}
            />
          </View>
          <View style={styles.paperInfo}>
            <Text style={styles.paperTitle}>{paper.title}</Text>
            <View style={styles.paperMeta}>
              <Text style={styles.paperMetaText}>
                {paper.total_questions} Questions
              </Text>
              <Text style={styles.paperMetaDot}>•</Text>
              <Text style={styles.paperMetaText}>
                {paper.duration_minutes} min
              </Text>
            </View>
          </View>
        </View>
        <View style={styles.paperRight}>
          {hasAttempt ? (
            <View style={styles.scoreContainer}>
              <Text style={[
                styles.scoreText,
                bestScore! >= 70 ? styles.scoreGood : bestScore! >= 40 ? styles.scoreMedium : styles.scoreLow
              ]}>
                {bestScore}%
              </Text>
              <Text style={styles.scoreBest}>Best</Text>
            </View>
          ) : (
            <View style={[styles.newBadge, isExtreme && styles.extremeBadge]}>
              <Text style={[styles.newBadgeText, isExtreme && styles.extremeBadgeText]}>
                {isExtreme ? 'TOUGH' : 'NEW'}
              </Text>
            </View>
          )}
          <MaterialCommunityIcons name="chevron-right" size={20} color="#64748B" />
        </View>
      </TouchableOpacity>
    );
  };

  if (isLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
          <Text style={styles.loadingText}>Loading papers...</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
        >
          <MaterialCommunityIcons name="arrow-left" size={24} color="#F8FAFC" />
        </TouchableOpacity>
        <View style={styles.headerContent}>
          <Text style={styles.headerTitle} numberOfLines={1}>
            {subject?.name || 'Subject'}
          </Text>
          <Text style={styles.headerSubtitle}>
            {regularPapers.length} Practice + {extremePapers.length} Extreme + {masterPaper ? '1 Master' : '0 Master'}
          </Text>
        </View>
      </View>

      <View style={styles.tabContainer}>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'practice' && styles.tabActive]}
          onPress={() => setActiveTab('practice')}
        >
          <MaterialCommunityIcons
            name="file-document-multiple"
            size={18}
            color={activeTab === 'practice' ? '#3B82F6' : '#64748B'}
          />
          <Text style={[styles.tabText, activeTab === 'practice' && styles.tabTextActive]}>
            Practice Papers
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'master' && styles.tabActive]}
          onPress={() => setActiveTab('master')}
        >
          <MaterialCommunityIcons
            name="star"
            size={18}
            color={activeTab === 'master' ? '#F59E0B' : '#64748B'}
          />
          <Text style={[styles.tabText, activeTab === 'master' && styles.tabTextActive]}>
            Master Paper
          </Text>
        </TouchableOpacity>
      </View>

      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {activeTab === 'practice' ? (
          <>
            <Text style={styles.sectionInfo}>
              Practice with previous year questions pattern
            </Text>
            {regularPapers.map(renderPaperCard)}
            
            {extremePapers.length > 0 && (
              <>
                <View style={styles.extremeSection}>
                  <MaterialCommunityIcons name="fire" size={20} color="#EF4444" />
                  <Text style={styles.extremeSectionTitle}>Extreme Difficulty</Text>
                </View>
                <Text style={styles.extremeInfo}>
                  🔥 Challenge yourself with the toughest questions. These require deep analytical thinking and multi-concept understanding.
                </Text>
                {extremePapers.map(renderPaperCard)}
              </>
            )}
          </>
        ) : (
          <>
            <View style={styles.masterInfo}>
              <MaterialCommunityIcons name="lightbulb" size={24} color="#F59E0B" />
              <Text style={styles.masterInfoText}>
                Predicted questions based on recent trends and high-probability topics
              </Text>
            </View>
            {masterPaper && renderPaperCard(masterPaper)}
          </>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    fontSize: 14,
    color: '#94A3B8',
    marginTop: 12,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  backButton: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  headerContent: {
    flex: 1,
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#F8FAFC',
  },
  headerSubtitle: {
    fontSize: 13,
    color: '#94A3B8',
    marginTop: 2,
  },
  tabContainer: {
    flexDirection: 'row',
    paddingHorizontal: 16,
    paddingVertical: 12,
  },
  tab: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 12,
    borderRadius: 12,
    backgroundColor: '#1E293B',
    marginHorizontal: 6,
  },
  tabActive: {
    backgroundColor: '#1E3A5F',
  },
  tabText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
    marginLeft: 8,
  },
  tabTextActive: {
    color: '#F8FAFC',
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: 16,
    paddingBottom: 24,
  },
  sectionInfo: {
    fontSize: 13,
    color: '#64748B',
    marginBottom: 16,
  },
  extremeSection: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 24,
    marginBottom: 8,
  },
  extremeSectionTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#EF4444',
    marginLeft: 8,
  },
  extremeInfo: {
    fontSize: 13,
    color: '#94A3B8',
    marginBottom: 16,
    lineHeight: 18,
  },
  masterInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#422006',
    padding: 16,
    borderRadius: 12,
    marginBottom: 16,
  },
  masterInfoText: {
    flex: 1,
    fontSize: 13,
    color: '#FCD34D',
    lineHeight: 18,
    marginLeft: 12,
  },
  paperCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 14,
    marginBottom: 10,
  },
  extremePaperCard: {
    borderWidth: 1,
    borderColor: '#7F1D1D',
    backgroundColor: '#1C1917',
  },
  paperLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  paperIcon: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: '#1E3A5F',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  masterIcon: {
    backgroundColor: '#422006',
  },
  extremeIcon: {
    backgroundColor: '#450A0A',
  },
  paperInfo: {
    flex: 1,
  },
  paperTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  paperMeta: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  paperMetaText: {
    fontSize: 12,
    color: '#64748B',
  },
  paperMetaDot: {
    fontSize: 12,
    color: '#64748B',
    marginHorizontal: 6,
  },
  paperRight: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  scoreContainer: {
    alignItems: 'flex-end',
    marginRight: 8,
  },
  scoreText: {
    fontSize: 16,
    fontWeight: '700',
  },
  scoreGood: {
    color: '#22C55E',
  },
  scoreMedium: {
    color: '#F59E0B',
  },
  scoreLow: {
    color: '#EF4444',
  },
  scoreBest: {
    fontSize: 10,
    color: '#64748B',
  },
  newBadge: {
    backgroundColor: '#1E3A5F',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
    marginRight: 8,
  },
  newBadgeText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#3B82F6',
  },
  extremeBadge: {
    backgroundColor: '#450A0A',
  },
  extremeBadgeText: {
    color: '#EF4444',
  },
});
