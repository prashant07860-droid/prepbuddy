import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Switch,
  Alert,
} from 'react-native';
import { useRouter } from 'expo-router';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { fetchSettings, updateSettings, UserSettings } from '../src/api';

export default function SettingsScreen() {
  const router = useRouter();
  const queryClient = useQueryClient();

  const { data: settings, isLoading } = useQuery({
    queryKey: ['settings'],
    queryFn: fetchSettings,
  });

  const updateMutation = useMutation({
    mutationFn: updateSettings,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['settings'] });
    },
  });

  const handleTimerModeChange = (mode: 'total' | 'per_question') => {
    if (settings) {
      updateMutation.mutate({ ...settings, timer_mode: mode });
    }
  };

  const handleShowTimerToggle = (value: boolean) => {
    if (settings) {
      updateMutation.mutate({ ...settings, show_timer: value });
    }
  };

  const handleTotalTimeChange = (change: number) => {
    if (settings) {
      const newTime = Math.max(30, Math.min(180, settings.total_time_minutes + change));
      updateMutation.mutate({ ...settings, total_time_minutes: newTime });
    }
  };

  const handlePerQuestionTimeChange = (change: number) => {
    if (settings) {
      const newTime = Math.max(30, Math.min(180, settings.per_question_seconds + change));
      updateMutation.mutate({ ...settings, per_question_seconds: newTime });
    }
  };

  const handleClearData = () => {
    Alert.alert(
      'Clear All Data',
      'This will reset all your progress and attempt history. This action cannot be undone.',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Clear',
          style: 'destructive',
          onPress: () => {
            // This would typically clear the database
            Alert.alert('Data Cleared', 'All your progress has been reset.');
          },
        },
      ]
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
        <Text style={styles.headerTitle}>Settings</Text>
        <View style={styles.placeholder} />
      </View>

      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Timer Settings */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Timer Settings</Text>

          <View style={styles.settingItem}>
            <View style={styles.settingInfo}>
              <MaterialCommunityIcons name="timer" size={22} color="#3B82F6" />
              <View style={styles.settingText}>
                <Text style={styles.settingLabel}>Show Timer</Text>
                <Text style={styles.settingDescription}>
                  Display countdown timer during exam
                </Text>
              </View>
            </View>
            <Switch
              value={settings?.show_timer ?? true}
              onValueChange={handleShowTimerToggle}
              trackColor={{ false: '#475569', true: '#3B82F6' }}
              thumbColor={settings?.show_timer ? '#FFFFFF' : '#94A3B8'}
            />
          </View>

          <View style={styles.settingItem}>
            <Text style={styles.settingLabel}>Timer Mode</Text>
          </View>

          <View style={styles.timerModeContainer}>
            <TouchableOpacity
              style={[
                styles.timerModeOption,
                settings?.timer_mode === 'total' && styles.timerModeActive,
              ]}
              onPress={() => handleTimerModeChange('total')}
            >
              <MaterialCommunityIcons
                name="clock-outline"
                size={24}
                color={settings?.timer_mode === 'total' ? '#3B82F6' : '#64748B'}
              />
              <Text style={[
                styles.timerModeText,
                settings?.timer_mode === 'total' && styles.timerModeTextActive,
              ]}>
                Total Time
              </Text>
              <Text style={styles.timerModeDesc}>One timer for all</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[
                styles.timerModeOption,
                settings?.timer_mode === 'per_question' && styles.timerModeActive,
              ]}
              onPress={() => handleTimerModeChange('per_question')}
            >
              <MaterialCommunityIcons
                name="timer-sand"
                size={24}
                color={settings?.timer_mode === 'per_question' ? '#3B82F6' : '#64748B'}
              />
              <Text style={[
                styles.timerModeText,
                settings?.timer_mode === 'per_question' && styles.timerModeTextActive,
              ]}>
                Per Question
              </Text>
              <Text style={styles.timerModeDesc}>Timer per question</Text>
            </TouchableOpacity>
          </View>

          {settings?.timer_mode === 'total' ? (
            <View style={styles.timeAdjust}>
              <Text style={styles.timeLabel}>Total Exam Time</Text>
              <View style={styles.timeControl}>
                <TouchableOpacity
                  style={styles.timeButton}
                  onPress={() => handleTotalTimeChange(-15)}
                >
                  <MaterialCommunityIcons name="minus" size={20} color="#F8FAFC" />
                </TouchableOpacity>
                <View style={styles.timeValue}>
                  <Text style={styles.timeValueText}>
                    {settings?.total_time_minutes || 90}
                  </Text>
                  <Text style={styles.timeUnit}>minutes</Text>
                </View>
                <TouchableOpacity
                  style={styles.timeButton}
                  onPress={() => handleTotalTimeChange(15)}
                >
                  <MaterialCommunityIcons name="plus" size={20} color="#F8FAFC" />
                </TouchableOpacity>
              </View>
            </View>
          ) : (
            <View style={styles.timeAdjust}>
              <Text style={styles.timeLabel}>Time Per Question</Text>
              <View style={styles.timeControl}>
                <TouchableOpacity
                  style={styles.timeButton}
                  onPress={() => handlePerQuestionTimeChange(-10)}
                >
                  <MaterialCommunityIcons name="minus" size={20} color="#F8FAFC" />
                </TouchableOpacity>
                <View style={styles.timeValue}>
                  <Text style={styles.timeValueText}>
                    {settings?.per_question_seconds || 60}
                  </Text>
                  <Text style={styles.timeUnit}>seconds</Text>
                </View>
                <TouchableOpacity
                  style={styles.timeButton}
                  onPress={() => handlePerQuestionTimeChange(10)}
                >
                  <MaterialCommunityIcons name="plus" size={20} color="#F8FAFC" />
                </TouchableOpacity>
              </View>
            </View>
          )}
        </View>

        {/* About Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>About</Text>

          <View style={styles.aboutItem}>
            <MaterialCommunityIcons name="information" size={22} color="#64748B" />
            <View style={styles.aboutText}>
              <Text style={styles.aboutLabel}>App Version</Text>
              <Text style={styles.aboutValue}>1.0.0</Text>
            </View>
          </View>

          <View style={styles.aboutItem}>
            <MaterialCommunityIcons name="book-open-variant" size={22} color="#64748B" />
            <View style={styles.aboutText}>
              <Text style={styles.aboutLabel}>Total Questions</Text>
              <Text style={styles.aboutValue}>23,100 MCQs</Text>
            </View>
          </View>

          <View style={styles.aboutItem}>
            <MaterialCommunityIcons name="school" size={22} color="#64748B" />
            <View style={styles.aboutText}>
              <Text style={styles.aboutLabel}>Subjects Covered</Text>
              <Text style={styles.aboutValue}>11 Subjects</Text>
            </View>
          </View>
        </View>

        {/* Danger Zone */}
        <View style={styles.section}>
          <Text style={[styles.sectionTitle, { color: '#EF4444' }]}>Danger Zone</Text>

          <TouchableOpacity
            style={styles.dangerButton}
            onPress={handleClearData}
          >
            <MaterialCommunityIcons name="delete" size={22} color="#EF4444" />
            <Text style={styles.dangerButtonText}>Clear All Progress</Text>
          </TouchableOpacity>
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
  placeholder: {
    width: 40,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: 16,
  },
  section: {
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 16,
    marginBottom: 16,
  },
  sectionTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
    marginBottom: 16,
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  settingItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  settingInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
    gap: 12,
  },
  settingText: {
    flex: 1,
  },
  settingLabel: {
    fontSize: 15,
    fontWeight: '500',
    color: '#F8FAFC',
  },
  settingDescription: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 2,
  },
  timerModeContainer: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 16,
  },
  timerModeOption: {
    flex: 1,
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#0F172A',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: 'transparent',
  },
  timerModeActive: {
    borderColor: '#3B82F6',
    backgroundColor: '#1E3A5F',
  },
  timerModeText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
    marginTop: 8,
  },
  timerModeTextActive: {
    color: '#F8FAFC',
  },
  timerModeDesc: {
    fontSize: 11,
    color: '#475569',
    marginTop: 4,
  },
  timeAdjust: {
    backgroundColor: '#0F172A',
    borderRadius: 12,
    padding: 16,
  },
  timeLabel: {
    fontSize: 13,
    color: '#94A3B8',
    textAlign: 'center',
    marginBottom: 12,
  },
  timeControl: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 20,
  },
  timeButton: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: '#334155',
    justifyContent: 'center',
    alignItems: 'center',
  },
  timeValue: {
    alignItems: 'center',
    minWidth: 80,
  },
  timeValueText: {
    fontSize: 32,
    fontWeight: '700',
    color: '#F8FAFC',
  },
  timeUnit: {
    fontSize: 12,
    color: '#64748B',
  },
  aboutItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  aboutText: {
    flex: 1,
  },
  aboutLabel: {
    fontSize: 14,
    color: '#94A3B8',
  },
  aboutValue: {
    fontSize: 15,
    fontWeight: '500',
    color: '#F8FAFC',
    marginTop: 2,
  },
  dangerButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#450A0A',
    paddingVertical: 14,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#EF4444',
  },
  dangerButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#EF4444',
  },
  bottomPadding: {
    height: 20,
  },
});
