import React, { useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { useRouter } from 'expo-router';
import { useQuery } from '@tanstack/react-query';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { fetchSubjects, Subject } from '../src/api';

const ICON_MAP: Record<string, keyof typeof MaterialCommunityIcons.glyphMap> = {
  bank: 'bank',
  earth: 'earth',
  'book-open-variant': 'book-open-variant',
  'scale-balance': 'scale-balance',
  atom: 'atom',
  'chart-line': 'chart-line',
  leaf: 'leaf',
  castle: 'castle',
  'account-group': 'account-group',
  'map-marker': 'map-marker',
  newspaper: 'newspaper',
};

export default function HomeScreen() {
  const router = useRouter();

  const {
    data: subjects,
    isLoading,
    error,
    refetch,
  } = useQuery({
    queryKey: ['subjects'],
    queryFn: fetchSubjects,
  });

  useEffect(() => {
    console.log('Subjects data:', subjects);
    console.log('Loading:', isLoading);
    console.log('Error:', error);
  }, [subjects, isLoading, error]);

  const renderSubjectCard = (subject: Subject) => (
    <TouchableOpacity
      key={subject.id}
      style={[styles.subjectCard, { borderLeftColor: subject.color }]}
      onPress={() => router.push(`/subject/${subject.id}`)}
      activeOpacity={0.7}
    >
      <View style={[styles.iconContainer, { backgroundColor: subject.color + '20' }]}>
        <MaterialCommunityIcons
          name={ICON_MAP[subject.icon] || 'book'}
          size={28}
          color={subject.color}
        />
      </View>
      <View style={styles.cardContent}>
        <Text style={styles.subjectName}>{subject.name}</Text>
        <Text style={styles.subjectDescription} numberOfLines={2}>
          {subject.description}
        </Text>
        <View style={styles.statsRow}>
          <View style={styles.statItem}>
            <MaterialCommunityIcons name="file-document-outline" size={14} color="#94A3B8" />
            <Text style={styles.statText}>{subject.total_papers} Papers</Text>
          </View>
          <View style={styles.statItem}>
            <MaterialCommunityIcons name="help-circle-outline" size={14} color="#94A3B8" />
            <Text style={styles.statText}>{subject.total_questions} MCQs</Text>
          </View>
        </View>
      </View>
      <MaterialCommunityIcons name="chevron-right" size={24} color="#64748B" />
    </TouchableOpacity>
  );

  if (isLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
          <Text style={styles.loadingText}>Loading subjects...</Text>
        </View>
      </SafeAreaView>
    );
  }

  if (error) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={48} color="#EF4444" />
          <Text style={styles.errorText}>Failed to load subjects</Text>
          <TouchableOpacity style={styles.retryButton} onPress={() => refetch()}>
            <Text style={styles.retryText}>Retry</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <View>
          <Text style={styles.welcomeText}>OPSC Exam Prep</Text>
          <Text style={styles.subtitle}>Master your preparation</Text>
        </View>
        <View style={styles.headerButtons}>
          <TouchableOpacity
            style={styles.headerButton}
            onPress={() => router.push('/dashboard')}
          >
            <MaterialCommunityIcons name="chart-box" size={24} color="#3B82F6" />
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.headerButton}
            onPress={() => router.push('/settings')}
          >
            <MaterialCommunityIcons name="cog" size={24} color="#94A3B8" />
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl refreshing={isLoading} onRefresh={refetch} tintColor="#3B82F6" />
        }
      >
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>All Subjects</Text>
          <Text style={styles.sectionCount}>{subjects?.length || 0} subjects</Text>
        </View>

        {subjects?.map(renderSubjectCard)}

        <View style={styles.bottomPadding} />
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
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
  },
  subtitle: {
    fontSize: 14,
    color: '#94A3B8',
    marginTop: 2,
  },
  headerButtons: {
    flexDirection: 'row',
    gap: 8,
  },
  headerButton: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: 20,
    paddingTop: 16,
  },
  sectionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  sectionCount: {
    fontSize: 14,
    color: '#64748B',
  },
  subjectCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    borderLeftWidth: 4,
  },
  iconContainer: {
    width: 52,
    height: 52,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 14,
  },
  cardContent: {
    flex: 1,
  },
  subjectName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  subjectDescription: {
    fontSize: 13,
    color: '#94A3B8',
    lineHeight: 18,
    marginBottom: 8,
  },
  statsRow: {
    flexDirection: 'row',
    gap: 16,
  },
  statItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
  },
  statText: {
    fontSize: 12,
    color: '#64748B',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#94A3B8',
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  errorText: {
    marginTop: 12,
    fontSize: 16,
    color: '#94A3B8',
    textAlign: 'center',
  },
  retryButton: {
    marginTop: 16,
    paddingHorizontal: 24,
    paddingVertical: 12,
    backgroundColor: '#3B82F6',
    borderRadius: 8,
  },
  retryText: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
  bottomPadding: {
    height: 24,
  },
});
