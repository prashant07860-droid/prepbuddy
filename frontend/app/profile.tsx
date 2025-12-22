import React, { useEffect, useState } from 'react';
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
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useAuth } from '../src/AuthContext';
import Constants from 'expo-constants';

interface SubjectProgress {
  subject_id: string;
  subject_name: string;
  attempts: number;
  accuracy: number;
  average_score: number;
  total_questions_attempted: number;
}

interface ProfileData {
  is_guest: boolean;
  id?: string;
  name?: string;
  email?: string;
  created_at?: string;
  total_attempts: number;
  total_correct: number;
  total_questions_attempted: number;
  overall_accuracy: number;
  subject_progress: SubjectProgress[];
}

const getBackendUrl = () => {
  return Constants.expoConfig?.extra?.EXPO_PUBLIC_BACKEND_URL 
    || process.env.EXPO_PUBLIC_BACKEND_URL 
    || '';
};

export default function ProfileScreen() {
  const router = useRouter();
  const { user, token, isGuest, logout } = useAuth();
  const [profileData, setProfileData] = useState<ProfileData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    fetchProfile();
  }, [token]);

  const fetchProfile = async () => {
    try {
      const backendUrl = getBackendUrl();
      const headers: HeadersInit = {
        'Content-Type': 'application/json',
      };
      
      if (token) {
        headers['Authorization'] = `Bearer ${token}`;
      }

      const response = await fetch(`${backendUrl}/api/auth/me`, {
        headers,
      });

      if (response.ok) {
        const data = await response.json();
        setProfileData(data);
      }
    } catch (error) {
      console.error('Error fetching profile:', error);
    } finally {
      setIsLoading(false);
      setRefreshing(false);
    }
  };

  const handleRefresh = () => {
    setRefreshing(true);
    fetchProfile();
  };

  const handleLogout = async () => {
    await logout();
    router.replace('/auth');
  };

  const handleLogin = () => {
    router.push('/auth');
  };

  if (isLoading) {
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
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
          <MaterialCommunityIcons name="arrow-left" size={24} color="#F8FAFC" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Profile</Text>
        <View style={styles.headerSpacer} />
      </View>

      <ScrollView
        style={styles.content}
        contentContainerStyle={styles.contentContainer}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={handleRefresh} tintColor="#3B82F6" />
        }
      >
        {/* User Info Card */}
        <View style={styles.userCard}>
          <View style={styles.avatarContainer}>
            <MaterialCommunityIcons
              name={isGuest || profileData?.is_guest ? 'account-outline' : 'account'}
              size={48}
              color="#3B82F6"
            />
          </View>
          
          {isGuest || profileData?.is_guest ? (
            <>
              <Text style={styles.userName}>Guest User</Text>
              <Text style={styles.userEmail}>Login to save your progress</Text>
              <TouchableOpacity style={styles.loginButton} onPress={handleLogin}>
                <MaterialCommunityIcons name="login" size={18} color="#FFFFFF" />
                <Text style={styles.loginButtonText}>Login / Sign Up</Text>
              </TouchableOpacity>
            </>
          ) : (
            <>
              <Text style={styles.userName}>{profileData?.name || user?.name}</Text>
              <Text style={styles.userEmail}>{profileData?.email || user?.email}</Text>
              {profileData?.created_at && (
                <Text style={styles.memberSince}>
                  Member since {new Date(profileData.created_at).toLocaleDateString()}
                </Text>
              )}
            </>
          )}
        </View>

        {/* Stats Overview */}
        <View style={styles.statsContainer}>
          <View style={styles.statCard}>
            <MaterialCommunityIcons name="clipboard-check" size={24} color="#3B82F6" />
            <Text style={styles.statValue}>{profileData?.total_attempts || 0}</Text>
            <Text style={styles.statLabel}>Total Exams</Text>
          </View>
          <View style={styles.statCard}>
            <MaterialCommunityIcons name="target" size={24} color="#22C55E" />
            <Text style={styles.statValue}>{profileData?.overall_accuracy || 0}%</Text>
            <Text style={styles.statLabel}>Accuracy</Text>
          </View>
          <View style={styles.statCard}>
            <MaterialCommunityIcons name="help-circle" size={24} color="#F59E0B" />
            <Text style={styles.statValue}>{profileData?.total_questions_attempted || 0}</Text>
            <Text style={styles.statLabel}>Questions</Text>
          </View>
        </View>

        {/* Subject Progress */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Subject Progress</Text>
          
          {profileData?.subject_progress && profileData.subject_progress.length > 0 ? (
            profileData.subject_progress.map((subject, index) => (
              <View key={subject.subject_id || index} style={styles.subjectCard}>
                <View style={styles.subjectHeader}>
                  <Text style={styles.subjectName}>{subject.subject_name}</Text>
                  <Text style={styles.subjectAttempts}>{subject.attempts} attempts</Text>
                </View>
                
                <View style={styles.progressBar}>
                  <View
                    style={[
                      styles.progressFill,
                      { width: `${Math.min(subject.accuracy, 100)}%` },
                      subject.accuracy >= 70 && styles.progressGood,
                      subject.accuracy >= 40 && subject.accuracy < 70 && styles.progressMedium,
                      subject.accuracy < 40 && styles.progressLow,
                    ]}
                  />
                </View>
                
                <View style={styles.subjectStats}>
                  <Text style={styles.subjectStatText}>
                    Accuracy: {subject.accuracy}%
                  </Text>
                  <Text style={styles.subjectStatText}>
                    Avg Score: {subject.average_score}%
                  </Text>
                </View>
              </View>
            ))
          ) : (
            <View style={styles.emptyState}>
              <MaterialCommunityIcons name="chart-line" size={48} color="#475569" />
              <Text style={styles.emptyText}>No exam attempts yet</Text>
              <Text style={styles.emptySubtext}>Start practicing to see your progress</Text>
            </View>
          )}
        </View>

        {/* Actions */}
        {!isGuest && !profileData?.is_guest && (
          <View style={styles.actionsContainer}>
            <TouchableOpacity style={styles.logoutButton} onPress={handleLogout}>
              <MaterialCommunityIcons name="logout" size={20} color="#EF4444" />
              <Text style={styles.logoutButtonText}>Logout</Text>
            </TouchableOpacity>
          </View>
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
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
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
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  headerSpacer: {
    width: 40,
  },
  content: {
    flex: 1,
  },
  contentContainer: {
    padding: 16,
  },
  userCard: {
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 24,
    alignItems: 'center',
    marginBottom: 16,
  },
  avatarContainer: {
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: '#0F172A',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 16,
  },
  userName: {
    fontSize: 22,
    fontWeight: '700',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  userEmail: {
    fontSize: 14,
    color: '#94A3B8',
    marginBottom: 8,
  },
  memberSince: {
    fontSize: 12,
    color: '#64748B',
  },
  loginButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#3B82F6',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 10,
    marginTop: 16,
  },
  loginButtonText: {
    fontSize: 15,
    fontWeight: '600',
    color: '#FFFFFF',
    marginLeft: 8,
  },
  statsContainer: {
    flexDirection: 'row',
    marginBottom: 24,
  },
  statCard: {
    flex: 1,
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    marginHorizontal: 4,
  },
  statValue: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 8,
  },
  statLabel: {
    fontSize: 12,
    color: '#94A3B8',
    marginTop: 4,
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
    marginBottom: 16,
  },
  subjectCard: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
  },
  subjectHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  subjectName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  subjectAttempts: {
    fontSize: 12,
    color: '#94A3B8',
  },
  progressBar: {
    height: 8,
    backgroundColor: '#0F172A',
    borderRadius: 4,
    marginBottom: 12,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    borderRadius: 4,
  },
  progressGood: {
    backgroundColor: '#22C55E',
  },
  progressMedium: {
    backgroundColor: '#F59E0B',
  },
  progressLow: {
    backgroundColor: '#EF4444',
  },
  subjectStats: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  subjectStatText: {
    fontSize: 13,
    color: '#94A3B8',
  },
  emptyState: {
    alignItems: 'center',
    padding: 32,
    backgroundColor: '#1E293B',
    borderRadius: 12,
  },
  emptyText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#F8FAFC',
    marginTop: 12,
  },
  emptySubtext: {
    fontSize: 14,
    color: '#64748B',
    marginTop: 4,
  },
  actionsContainer: {
    marginTop: 8,
  },
  logoutButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#1E293B',
    paddingVertical: 14,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#EF4444',
  },
  logoutButtonText: {
    fontSize: 15,
    fontWeight: '600',
    color: '#EF4444',
    marginLeft: 8,
  },
});
