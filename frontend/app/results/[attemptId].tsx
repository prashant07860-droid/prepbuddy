import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Share,
} from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { useQuery } from '@tanstack/react-query';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { fetchAttemptReview, fetchSubject } from '../../src/api';

export default function ResultsScreen() {
  const router = useRouter();
  const { attemptId } = useLocalSearchParams<{ attemptId: string }>();
  const [showReview, setShowReview] = React.useState(false);

  const { data, isLoading, error } = useQuery({
    queryKey: ['attemptReview', attemptId],
    queryFn: () => fetchAttemptReview(attemptId!),
    enabled: !!attemptId,
  });

  const { data: subject } = useQuery({
    queryKey: ['subject', data?.attempt?.subject_id],
    queryFn: () => fetchSubject(data?.attempt?.subject_id!),
    enabled: !!data?.attempt?.subject_id,
  });

  const formatTime = (seconds: number) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    if (hrs > 0) {
      return `${hrs}h ${mins}m ${secs}s`;
    }
    return `${mins}m ${secs}s`;
  };

  const handleShare = async () => {
    try {
      await Share.share({
        message: `I scored ${data?.attempt?.score_percentage}% in ${subject?.name} OPSC Exam Practice! ${data?.attempt?.correct_count}/${data?.attempt?.total_questions} correct answers.`,
      });
    } catch (error) {
      console.log('Error sharing:', error);
    }
  };

  if (isLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
          <Text style={styles.loadingText}>Loading results...</Text>
        </View>
      </SafeAreaView>
    );
  }

  if (error || !data) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={48} color="#EF4444" />
          <Text style={styles.errorText}>Failed to load results</Text>
          <TouchableOpacity style={styles.backBtn} onPress={() => router.replace('/')}>
            <Text style={styles.backBtnText}>Go Home</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    );
  }

  const { attempt, review } = data;
  const scoreColor = attempt.score_percentage >= 70 ? '#22C55E' : attempt.score_percentage >= 40 ? '#F59E0B' : '#EF4444';

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Score Card */}
        <View style={styles.scoreCard}>
          <View style={[styles.scoreCircle, { borderColor: scoreColor }]}>
            <Text style={[styles.scorePercentage, { color: scoreColor }]}>
              {attempt.score_percentage}%
            </Text>
            <Text style={styles.scoreLabel}>Score</Text>
          </View>

          <Text style={styles.congratsText}>
            {attempt.score_percentage >= 70
              ? 'Excellent Work!'
              : attempt.score_percentage >= 40
              ? 'Good Effort!'
              : 'Keep Practicing!'}
          </Text>
          <Text style={styles.subjectName}>{subject?.name}</Text>
        </View>

        {/* Stats Grid */}
        <View style={styles.statsGrid}>
          <View style={[styles.statCard, styles.statCorrect]}>
            <MaterialCommunityIcons name="check-circle" size={28} color="#22C55E" />
            <Text style={styles.statValue}>{attempt.correct_count}</Text>
            <Text style={styles.statLabel}>Correct</Text>
          </View>
          <View style={[styles.statCard, styles.statWrong]}>
            <MaterialCommunityIcons name="close-circle" size={28} color="#EF4444" />
            <Text style={styles.statValue}>{attempt.wrong_count}</Text>
            <Text style={styles.statLabel}>Wrong</Text>
          </View>
          <View style={[styles.statCard, styles.statSkipped]}>
            <MaterialCommunityIcons name="minus-circle" size={28} color="#64748B" />
            <Text style={styles.statValue}>{attempt.skipped_count}</Text>
            <Text style={styles.statLabel}>Skipped</Text>
          </View>
          <View style={[styles.statCard, styles.statTime]}>
            <MaterialCommunityIcons name="clock" size={28} color="#3B82F6" />
            <Text style={styles.statValue}>{formatTime(attempt.time_taken_seconds)}</Text>
            <Text style={styles.statLabel}>Time Taken</Text>
          </View>
        </View>

        {/* Action Buttons */}
        <View style={styles.actionButtons}>
          <TouchableOpacity
            style={styles.reviewButton}
            onPress={() => setShowReview(!showReview)}
          >
            <MaterialCommunityIcons
              name={showReview ? 'eye-off' : 'eye'}
              size={20}
              color="#3B82F6"
            />
            <Text style={styles.reviewButtonText}>
              {showReview ? 'Hide Answers' : 'Review Answers'}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.shareButton} onPress={handleShare}>
            <MaterialCommunityIcons name="share-variant" size={20} color="#F8FAFC" />
            <Text style={styles.shareButtonText}>Share</Text>
          </TouchableOpacity>
        </View>

        {/* Answer Review */}
        {showReview && (
          <View style={styles.reviewSection}>
            <Text style={styles.reviewTitle}>Answer Review</Text>
            {review.map((item: any, index: number) => (
              <View key={item.question.id} style={styles.reviewItem}>
                <View style={styles.reviewHeader}>
                  <Text style={styles.reviewNumber}>Q{index + 1}</Text>
                  <View style={[
                    styles.reviewStatus,
                    item.is_skipped
                      ? styles.reviewStatusSkipped
                      : item.is_correct
                      ? styles.reviewStatusCorrect
                      : styles.reviewStatusWrong,
                  ]}>
                    <MaterialCommunityIcons
                      name={item.is_skipped ? 'minus' : item.is_correct ? 'check' : 'close'}
                      size={14}
                      color="#FFFFFF"
                    />
                  </View>
                </View>
                <Text style={styles.reviewQuestion}>
                  {item.question.question_text}
                </Text>
                <View style={styles.reviewOptions}>
                  {item.question.options.map((option: string, optIndex: number) => (
                    <View
                      key={optIndex}
                      style={[
                        styles.reviewOption,
                        optIndex === item.question.correct_option && styles.reviewOptionCorrect,
                        optIndex === item.user_answer && optIndex !== item.question.correct_option && styles.reviewOptionWrong,
                      ]}
                    >
                      <Text style={styles.reviewOptionIndex}>
                        {String.fromCharCode(65 + optIndex)}
                      </Text>
                      <Text style={[
                        styles.reviewOptionText,
                        optIndex === item.question.correct_option && styles.reviewOptionTextCorrect,
                        optIndex === item.user_answer && optIndex !== item.question.correct_option && styles.reviewOptionTextWrong,
                      ]}>
                        {option}
                      </Text>
                      {optIndex === item.question.correct_option && (
                        <MaterialCommunityIcons name="check" size={16} color="#22C55E" />
                      )}
                      {optIndex === item.user_answer && optIndex !== item.question.correct_option && (
                        <MaterialCommunityIcons name="close" size={16} color="#EF4444" />
                      )}
                    </View>
                  ))}
                </View>
                {item.question.explanation && (
                  <View style={styles.explanationBox}>
                    <MaterialCommunityIcons name="lightbulb" size={16} color="#F59E0B" />
                    <Text style={styles.explanationText}>
                      {item.question.explanation}
                    </Text>
                  </View>
                )}
              </View>
            ))}
          </View>
        )}

        {/* Bottom Buttons */}
        <View style={styles.bottomButtons}>
          <TouchableOpacity
            style={styles.homeButton}
            onPress={() => router.replace('/')}
          >
            <MaterialCommunityIcons name="home" size={20} color="#3B82F6" />
            <Text style={styles.homeButtonText}>Home</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.retryButton}
            onPress={() => router.replace(`/subject/${attempt.subject_id}`)}
          >
            <MaterialCommunityIcons name="refresh" size={20} color="#FFFFFF" />
            <Text style={styles.retryButtonText}>Try Another</Text>
          </TouchableOpacity>
        </View>
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
  },
  backBtn: {
    marginTop: 16,
    paddingHorizontal: 24,
    paddingVertical: 12,
    backgroundColor: '#3B82F6',
    borderRadius: 8,
  },
  backBtnText: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: 20,
  },
  scoreCard: {
    alignItems: 'center',
    backgroundColor: '#1E293B',
    borderRadius: 20,
    padding: 32,
    marginBottom: 20,
  },
  scoreCircle: {
    width: 140,
    height: 140,
    borderRadius: 70,
    borderWidth: 6,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    marginBottom: 16,
  },
  scorePercentage: {
    fontSize: 36,
    fontWeight: '700',
  },
  scoreLabel: {
    fontSize: 14,
    color: '#64748B',
    marginTop: 4,
  },
  congratsText: {
    fontSize: 22,
    fontWeight: '700',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  subjectName: {
    fontSize: 14,
    color: '#94A3B8',
  },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    marginBottom: 20,
  },
  statCard: {
    flex: 1,
    minWidth: '45%',
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
  },
  statCorrect: {
    borderLeftWidth: 3,
    borderLeftColor: '#22C55E',
  },
  statWrong: {
    borderLeftWidth: 3,
    borderLeftColor: '#EF4444',
  },
  statSkipped: {
    borderLeftWidth: 3,
    borderLeftColor: '#64748B',
  },
  statTime: {
    borderLeftWidth: 3,
    borderLeftColor: '#3B82F6',
  },
  statValue: {
    fontSize: 20,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 8,
  },
  statLabel: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 4,
  },
  actionButtons: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 20,
  },
  reviewButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#1E293B',
    paddingVertical: 14,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#3B82F6',
  },
  reviewButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#3B82F6',
  },
  shareButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#334155',
    paddingVertical: 14,
    paddingHorizontal: 20,
    borderRadius: 12,
  },
  shareButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  reviewSection: {
    marginBottom: 20,
  },
  reviewTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
    marginBottom: 16,
  },
  reviewItem: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
  },
  reviewHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 12,
  },
  reviewNumber: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
  },
  reviewStatus: {
    width: 22,
    height: 22,
    borderRadius: 6,
    justifyContent: 'center',
    alignItems: 'center',
  },
  reviewStatusCorrect: {
    backgroundColor: '#22C55E',
  },
  reviewStatusWrong: {
    backgroundColor: '#EF4444',
  },
  reviewStatusSkipped: {
    backgroundColor: '#64748B',
  },
  reviewQuestion: {
    fontSize: 15,
    color: '#F8FAFC',
    lineHeight: 22,
    marginBottom: 12,
  },
  reviewOptions: {
    gap: 8,
  },
  reviewOption: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    borderRadius: 8,
    padding: 12,
    gap: 10,
  },
  reviewOptionCorrect: {
    backgroundColor: '#14532D',
    borderWidth: 1,
    borderColor: '#22C55E',
  },
  reviewOptionWrong: {
    backgroundColor: '#450A0A',
    borderWidth: 1,
    borderColor: '#EF4444',
  },
  reviewOptionIndex: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
    width: 20,
  },
  reviewOptionText: {
    flex: 1,
    fontSize: 14,
    color: '#94A3B8',
  },
  reviewOptionTextCorrect: {
    color: '#4ADE80',
  },
  reviewOptionTextWrong: {
    color: '#FCA5A5',
  },
  explanationBox: {
    flexDirection: 'row',
    gap: 8,
    backgroundColor: '#422006',
    borderRadius: 8,
    padding: 12,
    marginTop: 12,
  },
  explanationText: {
    flex: 1,
    fontSize: 13,
    color: '#FCD34D',
    lineHeight: 18,
  },
  bottomButtons: {
    flexDirection: 'row',
    gap: 12,
    paddingBottom: 20,
  },
  homeButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#1E293B',
    paddingVertical: 16,
    borderRadius: 12,
  },
  homeButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#3B82F6',
  },
  retryButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#3B82F6',
    paddingVertical: 16,
    borderRadius: 12,
  },
  retryButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
  },
});
