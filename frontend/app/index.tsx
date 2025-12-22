import React, { useState, useCallback, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
  Linking,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useAuth } from '../src/AuthContext';

interface Subject {
  id: string;
  name: string;
  description: string;
  icon: string;
  color: string;
  total_papers: number;
  total_questions: number;
}

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

const INITIAL_SUBJECTS: Subject[] = [
  {
    id: 'bf517fa7-5aac-4639-8363-2aeaa198b915',
    name: 'Polity',
    description: 'Constitution of India, governance, rights, duties, institutions',
    icon: 'bank',
    color: '#3B82F6',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: 'a41db799-f11b-44cb-b987-c8b744353ee9',
    name: 'Geography',
    description: 'Physical Geography, Indian Geography, Odisha Geography',
    icon: 'earth',
    color: '#10B981',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: 'bb219476-4e4c-4337-ac93-0022a1b0116f',
    name: 'History of Modern India',
    description: 'Freedom struggle, reforms, movements (1757-1947)',
    icon: 'book-open-variant',
    color: '#F59E0B',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: '0e3373c7-aee7-433c-9922-ff1da0806a3f',
    name: 'Ethics',
    description: 'Ethics & Human Values, integrity, aptitude, moral thinkers',
    icon: 'scale-balance',
    color: '#8B5CF6',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: 'c32206e4-4f15-4c7e-a6c7-227361d90a76',
    name: 'Science and Technology',
    description: 'General science, emerging technologies, space, defence',
    icon: 'atom',
    color: '#EC4899',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: '138bb0a1-4b12-4eac-838b-b02d7ba2f192',
    name: 'Economics',
    description: 'Indian economy basics, growth, inflation, budgeting',
    icon: 'chart-line',
    color: '#06B6D4',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: 'da991167-40b5-43d6-b8fd-4b913d3da04a',
    name: 'Environment and Ecology',
    description: 'Ecology basics, climate change, environmental laws',
    icon: 'leaf',
    color: '#22C55E',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: '5cf4e1e2-2d0a-41df-b06b-1a7ed058278d',
    name: 'Ancient & Medieval History',
    description: 'Pre-independence Indian history, dynasties, culture',
    icon: 'castle',
    color: '#D97706',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: 'ff1a2f17-6ca0-4c83-b58d-22b3280b4f04',
    name: 'Indian Society',
    description: 'Social structure, issues, diversity, communalism',
    icon: 'account-group',
    color: '#EF4444',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: '6d0a547e-ed97-4741-ba10-8c9d2a3aed2f',
    name: 'Odisha Studies',
    description: 'History & culture of Odisha, economy, state schemes',
    icon: 'map-marker',
    color: '#7C3AED',
    total_papers: 20,
    total_questions: 2000,
  },
  {
    id: '8b5a7f40-4cec-45fb-a2c6-80bbb339a5b7',
    name: 'Current Affairs',
    description: 'National, International current events',
    icon: 'newspaper',
    color: '#0EA5E9',
    total_papers: 20,
    total_questions: 2000,
  },
];

export default function HomeScreen() {
  const router = useRouter();
  const { user, isGuest, isLoading: authLoading } = useAuth();
  const [subjects, setSubjects] = useState<Subject[]>(INITIAL_SUBJECTS);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Redirect to auth if not logged in and not guest
  useEffect(() => {
    if (!authLoading && !user && !isGuest) {
      router.replace('/auth');
    }
  }, [authLoading, user, isGuest]);

  const fetchSubjects = useCallback(async () => {
    try {
      setIsLoading(true);
      setError(null);
      
      const response = await fetch('/api/subjects');
      
      if (!response.ok) {
        throw new Error(`Failed to fetch subjects: ${response.status}`);
      }
      const data = await response.json();
      if (data && data.length > 0) {
        setSubjects(data);
      }
    } catch (err) {
      // Keep initial data on error
      console.log('Using initial data');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      fetchSubjects();
    }
  }, []);

  const navigateToSubject = (subjectId: string) => {
    router.push(`/subject/${subjectId}`);
  };

  const renderSubjectCard = (subject: Subject) => (
    <TouchableOpacity
      key={subject.id}
      style={[styles.subjectCard, { borderLeftColor: subject.color }]}
      onPress={() => navigateToSubject(subject.id)}
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

  if (error && subjects.length === 0) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={48} color="#EF4444" />
          <Text style={styles.errorText}>{error}</Text>
          <TouchableOpacity style={styles.retryButton} onPress={fetchSubjects}>
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
          <Text style={styles.subtitle}>
            {user ? `Welcome, ${user.name}` : isGuest ? 'Guest Mode' : 'Master your preparation'}
          </Text>
        </View>
        <View style={styles.headerButtons}>
          <TouchableOpacity
            style={styles.headerButton}
            onPress={() => router.push('/dashboard')}
          >
            <MaterialCommunityIcons name="chart-box" size={24} color="#3B82F6" />
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.headerButton, user && styles.profileButtonActive]}
            onPress={() => router.push('/profile')}
          >
            <MaterialCommunityIcons 
              name={user ? 'account' : 'account-outline'} 
              size={24} 
              color={user ? '#22C55E' : '#94A3B8'} 
            />
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl refreshing={isLoading} onRefresh={fetchSubjects} tintColor="#3B82F6" />
        }
      >
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>All Subjects</Text>
          <Text style={styles.sectionCount}>{subjects.length} subjects</Text>
        </View>

        {subjects.map(renderSubjectCard)}

        {/* Footer */}
        <View style={styles.footer}>
          <Text style={styles.footerText}>
            Made with ❤️ by{' '}
            <Text
              style={styles.footerLink}
              onPress={() => Linking.openURL('https://www.linkedin.com/in/prashantranaofficial/')}
            >
              Prashant (Sean) Rana
            </Text>
          </Text>
        </View>

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
  },
  headerButton: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 8,
  },
  profileButtonActive: {
    borderWidth: 2,
    borderColor: '#22C55E',
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
  },
  statItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 16,
  },
  statText: {
    fontSize: 12,
    color: '#64748B',
    marginLeft: 4,
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
  footer: {
    alignItems: 'center',
    paddingVertical: 20,
    marginTop: 16,
    borderTopWidth: 1,
    borderTopColor: '#1E293B',
  },
  footerText: {
    fontSize: 14,
    color: '#64748B',
  },
  footerLink: {
    color: '#3B82F6',
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
});
