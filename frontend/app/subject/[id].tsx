import React, { useState, useEffect, useCallback } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Pressable,
} from 'react-native';
import { useRouter, useLocalSearchParams, Link } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';

interface Paper {
  id: string;
  subject_id: string;
  paper_number: number;
  is_master: boolean;
  title: string;
  total_questions: number;
  duration_minutes: number;
}

interface Attempt {
  id: string;
  paper_id: string;
  score_percentage: number;
}

// Subject data mapping
const SUBJECTS_MAP: Record<string, { name: string; color: string }> = {
  'bf517fa7-5aac-4639-8363-2aeaa198b915': { name: 'Polity', color: '#3B82F6' },
  'a41db799-f11b-44cb-b987-c8b744353ee9': { name: 'Geography', color: '#10B981' },
  'bb219476-4e4c-4337-ac93-0022a1b0116f': { name: 'History of Modern India', color: '#F59E0B' },
  '0e3373c7-aee7-433c-9922-ff1da0806a3f': { name: 'Ethics', color: '#8B5CF6' },
  'c32206e4-4f15-4c7e-a6c7-227361d90a76': { name: 'Science and Technology', color: '#EC4899' },
  '138bb0a1-4b12-4eac-838b-b02d7ba2f192': { name: 'Economics', color: '#06B6D4' },
  'da991167-40b5-43d6-b8fd-4b913d3da04a': { name: 'Environment and Ecology', color: '#22C55E' },
  '5cf4e1e2-2d0a-41df-b06b-1a7ed058278d': { name: 'Ancient & Medieval History', color: '#D97706' },
  'ff1a2f17-6ca0-4c83-b58d-22b3280b4f04': { name: 'Indian Society', color: '#EF4444' },
  '6d0a547e-ed97-4741-ba10-8c9d2a3aed2f': { name: 'Odisha Studies', color: '#7C3AED' },
  '8b5a7f40-4cec-45fb-a2c6-80bbb339a5b7': { name: 'Current Affairs', color: '#0EA5E9' },
};

// Generate initial papers data
const generatePapers = (subjectId: string): Paper[] => {
  const subjectName = SUBJECTS_MAP[subjectId]?.name || 'Subject';
  const papers: Paper[] = [];
  
  // Generate 20 practice papers
  for (let i = 1; i <= 20; i++) {
    papers.push({
      id: `${subjectId}-practice-${i}`,
      subject_id: subjectId,
      paper_number: i,
      is_master: false,
      title: `${subjectName} Practice Paper ${i}`,
      total_questions: 100,
      duration_minutes: 90,
    });
  }
  
  // Add master paper
  papers.push({
    id: `${subjectId}-master`,
    subject_id: subjectId,
    paper_number: 0,
    is_master: true,
    title: `${subjectName} Master Prediction Paper`,
    total_questions: 100,
    duration_minutes: 90,
  });
  
  return papers;
};

export default function SubjectScreen() {
  const router = useRouter();
  const { id } = useLocalSearchParams<{ id: string }>();
  const [activeTab, setActiveTab] = useState<'practice' | 'master'>('practice');
  
  const subjectInfo = id ? SUBJECTS_MAP[id] : null;
  const [papers, setPapers] = useState<Paper[]>(() => id ? generatePapers(id) : []);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = useCallback(async () => {
    if (!id) return;
    
    try {
      setIsLoading(true);
      
      // Fetch papers from API
      const papersRes = await fetch(`/api/subjects/${id}/papers`);
      if (papersRes.ok) {
        const papersData = await papersRes.json();
        if (papersData.length > 0) {
          setPapers(papersData);
        }
      }

      // Fetch attempts
      const attemptsRes = await fetch(`/api/attempts?subject_id=${id}`);
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

  const practicePapers = papers.filter((p) => !p.is_master);
  const masterPaper = papers.find((p) => p.is_master);

  const getBestScore = (paperId: string) => {
    const paperAttempts = attempts.filter((a) => a.paper_id === paperId);
    if (paperAttempts.length === 0) return null;
    return Math.max(...paperAttempts.map((a) => a.score_percentage));
  };

  const renderPaperCard = (paper: Paper) => {
    const bestScore = getBestScore(paper.id);
    const hasAttempt = bestScore !== null;

    return (
      <TouchableOpacity
        key={paper.id}
        style={styles.paperCard}
        onPress={() => router.push(`/exam/${paper.id}`)}
        activeOpacity={0.7}
      >
        <View style={styles.paperLeft}>
          <View style={[styles.paperIcon, paper.is_master && styles.masterIcon]}>
            <MaterialCommunityIcons
              name={paper.is_master ? 'star' : 'file-document'}
              size={20}
              color={paper.is_master ? '#F59E0B' : '#3B82F6'}
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
            <View style={styles.newBadge}>
              <Text style={styles.newBadgeText}>NEW</Text>
            </View>
          )}
          <MaterialCommunityIcons name="chevron-right" size={20} color="#64748B" />
        </View>
      </TouchableOpacity>
    );
  };

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
            {subjectInfo?.name || 'Subject'}
          </Text>
          <Text style={styles.headerSubtitle}>
            {practicePapers.length} Practice + {masterPaper ? '1 Master' : '0 Master'}
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
            {practicePapers.map(renderPaperCard)}
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
    gap: 12,
  },
  tab: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 12,
    borderRadius: 12,
    backgroundColor: '#1E293B',
  },
  tabActive: {
    backgroundColor: '#1E3A5F',
  },
  tabText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
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
  masterInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
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
    gap: 8,
  },
  scoreContainer: {
    alignItems: 'flex-end',
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
  },
  newBadgeText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#3B82F6',
  },
});
