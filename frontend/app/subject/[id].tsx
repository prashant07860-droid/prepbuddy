import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { useQuery } from '@tanstack/react-query';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { fetchSubject, fetchPapers, fetchAttempts, Paper } from '../../src/api';

export default function SubjectScreen() {
  const router = useRouter();
  const { id } = useLocalSearchParams<{ id: string }>();
  const [activeTab, setActiveTab] = useState<'practice' | 'master'>('practice');

  const { data: subject, isLoading: subjectLoading } = useQuery({
    queryKey: ['subject', id],
    queryFn: () => fetchSubject(id!),
    enabled: !!id,
  });

  const { data: papers, isLoading: papersLoading } = useQuery({
    queryKey: ['papers', id],
    queryFn: () => fetchPapers(id!),
    enabled: !!id,
  });

  const { data: attempts } = useQuery({
    queryKey: ['attempts', id],
    queryFn: () => fetchAttempts({ subject_id: id }),
    enabled: !!id,
  });

  const practicePapers = papers?.filter((p) => !p.is_master) || [];
  const masterPaper = papers?.find((p) => p.is_master);

  const getAttemptForPaper = (paperId: string) => {
    return attempts?.find((a) => a.paper_id === paperId);
  };

  const getBestScore = (paperId: string) => {
    const paperAttempts = attempts?.filter((a) => a.paper_id === paperId) || [];
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

  if (subjectLoading || papersLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
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
            {subject?.name}
          </Text>
          <Text style={styles.headerSubtitle}>
            {practicePapers.length} Practice + 1 Master
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
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
