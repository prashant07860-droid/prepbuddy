import React, { useEffect, useState, useCallback, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  Dimensions,
  Modal,
} from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';

const { width } = Dimensions.get('window');

interface Question {
  id: string;
  paper_id: string;
  subject_id: string;
  question_number: number;
  question_text: string;
  options: string[];
  correct_option: number;
  explanation?: string;
  difficulty: string;
  topic: string;
}

interface Paper {
  id: string;
  subject_id: string;
  paper_number: number;
  is_master: boolean;
  title: string;
  total_questions: number;
  duration_minutes: number;
}

// Sample questions generator
const generateSampleQuestions = (paperId: string, count: number = 100): Question[] => {
  const questions: Question[] = [];
  const topics = ['Constitution', 'Governance', 'Rights', 'Duties', 'Institutions', 'Parliament', 'Judiciary'];
  const difficulties = ['easy', 'medium', 'hard'];
  
  for (let i = 1; i <= count; i++) {
    questions.push({
      id: `${paperId}-q-${i}`,
      paper_id: paperId,
      subject_id: '',
      question_number: i,
      question_text: `Sample Question ${i}: Which of the following statements is correct regarding the ${topics[i % topics.length]}?`,
      options: [
        `Option A - Related to ${topics[i % topics.length]}`,
        `Option B - Alternative answer`,
        `Option C - Another possibility`,
        `Option D - Different perspective`,
      ],
      correct_option: i % 4,
      explanation: `This question tests knowledge of ${topics[i % topics.length]}. The correct answer demonstrates understanding of key concepts.`,
      difficulty: difficulties[i % 3],
      topic: topics[i % topics.length],
    });
  }
  
  return questions;
};

export default function ExamScreen() {
  const router = useRouter();
  const { paperId } = useLocalSearchParams<{ paperId: string }>();
  const scrollRef = useRef<ScrollView>(null);
  const [showNavigator, setShowNavigator] = useState(false);
  const [examStarted, setExamStarted] = useState(false);
  const [startTime, setStartTime] = useState<number>(0);

  // State management
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [bookmarkedQuestions, setBookmarkedQuestions] = useState<string[]>([]);
  const [timeRemaining, setTimeRemaining] = useState(5400); // 90 minutes
  const [timerMode, setTimerMode] = useState<'total' | 'per_question'>('total');
  const [showTimer, setShowTimerState] = useState(true);

  // Initialize questions
  const [questions, setQuestions] = useState<Question[]>(() => 
    paperId ? generateSampleQuestions(paperId) : []
  );
  const [isLoading, setIsLoading] = useState(false);

  // Get paper info from paperId
  const getPaperTitle = () => {
    if (!paperId) return 'Exam';
    if (paperId.includes('master')) return 'Master Prediction Paper';
    const match = paperId.match(/practice-(\d+)/);
    if (match) return `Practice Paper ${match[1]}`;
    return 'Exam';
  };

  // Timer effect
  useEffect(() => {
    if (!examStarted || !showTimer) return;

    const interval = setInterval(() => {
      setTimeRemaining((prev) => {
        if (prev <= 1) {
          handleSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [examStarted, showTimer]);

  const handleStartExam = useCallback(() => {
    setExamStarted(true);
    setStartTime(Date.now());
    setTimeRemaining(5400); // 90 minutes
    setAnswers({});
    setCurrentQuestionIndex(0);
    setBookmarkedQuestions([]);
  }, []);

  const handleSubmit = useCallback(() => {
    if (!questions || questions.length === 0) return;

    const timeTaken = Math.floor((Date.now() - startTime) / 1000);
    
    // Calculate score
    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    
    questions.forEach((q) => {
      if (answers[q.id] !== undefined) {
        if (answers[q.id] === q.correct_option) {
          correct++;
        } else {
          wrong++;
        }
      } else {
        skipped++;
      }
    });
    
    const scorePercentage = Math.round((correct / questions.length) * 100);

    Alert.alert(
      'Exam Submitted!',
      `Score: ${scorePercentage}%\nCorrect: ${correct}\nWrong: ${wrong}\nSkipped: ${skipped}\nTime: ${formatTime(timeTaken)}`,
      [
        {
          text: 'OK',
          onPress: () => router.replace('/'),
        },
      ]
    );
  }, [questions, answers, startTime, router]);

  const handleExit = () => {
    Alert.alert(
      'Exit Exam',
      'Are you sure you want to exit? Your progress will be lost.',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Exit',
          style: 'destructive',
          onPress: () => router.back(),
        },
      ]
    );
  };

  const formatTime = (seconds: number) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    if (hrs > 0) {
      return `${hrs}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const goToQuestion = (index: number) => {
    setCurrentQuestionIndex(index);
    setShowNavigator(false);
  };

  const setAnswer = (questionId: string, optionIndex: number) => {
    setAnswers((prev) => ({ ...prev, [questionId]: optionIndex }));
  };

  const toggleBookmark = (questionId: string) => {
    setBookmarkedQuestions((prev) =>
      prev.includes(questionId)
        ? prev.filter((id) => id !== questionId)
        : [...prev, questionId]
    );
  };

  if (!questions || questions.length === 0) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
          <Text style={styles.loadingText}>Loading exam...</Text>
        </View>
      </SafeAreaView>
    );
  }

  // Pre-exam screen
  if (!examStarted) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.preExamContainer}>
          <View style={styles.preExamCard}>
            <MaterialCommunityIcons
              name={paperId?.includes('master') ? 'star' : 'file-document'}
              size={48}
              color={paperId?.includes('master') ? '#F59E0B' : '#3B82F6'}
            />
            <Text style={styles.preExamTitle}>{getPaperTitle()}</Text>
            
            <View style={styles.preExamStats}>
              <View style={styles.preExamStat}>
                <MaterialCommunityIcons name="help-circle" size={24} color="#64748B" />
                <Text style={styles.preExamStatValue}>{questions.length}</Text>
                <Text style={styles.preExamStatLabel}>Questions</Text>
              </View>
              <View style={styles.preExamStatDivider} />
              <View style={styles.preExamStat}>
                <MaterialCommunityIcons name="clock" size={24} color="#64748B" />
                <Text style={styles.preExamStatValue}>90</Text>
                <Text style={styles.preExamStatLabel}>Minutes</Text>
              </View>
            </View>

            <View style={styles.preExamInfo}>
              <View style={styles.preExamInfoItem}>
                <MaterialCommunityIcons name="timer" size={18} color="#94A3B8" />
                <Text style={styles.preExamInfoText}>
                  Timer: Total Time (90 min)
                </Text>
              </View>
              <View style={styles.preExamInfoItem}>
                <MaterialCommunityIcons name="check-circle" size={18} color="#94A3B8" />
                <Text style={styles.preExamInfoText}>
                  +1 for correct, 0 for wrong
                </Text>
              </View>
            </View>

            <TouchableOpacity
              style={styles.startButton}
              onPress={handleStartExam}
            >
              <MaterialCommunityIcons name="play" size={24} color="#FFFFFF" />
              <Text style={styles.startButtonText}>Start Exam</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.cancelButton}
              onPress={() => router.back()}
            >
              <Text style={styles.cancelButtonText}>Go Back</Text>
            </TouchableOpacity>
          </View>
        </View>
      </SafeAreaView>
    );
  }

  const currentQuestion = questions[currentQuestionIndex];
  const isBookmarked = bookmarkedQuestions.includes(currentQuestion?.id);
  const selectedAnswer = answers[currentQuestion?.id];

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.exitButton} onPress={handleExit}>
          <MaterialCommunityIcons name="close" size={22} color="#F8FAFC" />
        </TouchableOpacity>
        
        <TouchableOpacity
          style={styles.questionCounter}
          onPress={() => setShowNavigator(true)}
        >
          <Text style={styles.questionCounterText}>
            {currentQuestionIndex + 1} / {questions.length}
          </Text>
          <MaterialCommunityIcons name="menu" size={18} color="#94A3B8" />
        </TouchableOpacity>

        {showTimer && (
          <View style={[
            styles.timerContainer,
            timeRemaining < 300 && styles.timerWarning
          ]}>
            <MaterialCommunityIcons
              name="clock-outline"
              size={18}
              color={timeRemaining < 300 ? '#EF4444' : '#3B82F6'}
            />
            <Text style={[
              styles.timerText,
              timeRemaining < 300 && styles.timerTextWarning
            ]}>
              {formatTime(timeRemaining)}
            </Text>
          </View>
        )}
      </View>

      {/* Question Content */}
      <ScrollView
        ref={scrollRef}
        style={styles.questionContainer}
        contentContainerStyle={styles.questionContent}
        showsVerticalScrollIndicator={false}
      >
        <View style={styles.questionHeader}>
          <View style={styles.questionBadges}>
            <View style={styles.difficultyBadge}>
              <Text style={styles.difficultyText}>
                {currentQuestion?.difficulty?.toUpperCase()}
              </Text>
            </View>
            <View style={styles.topicBadge}>
              <Text style={styles.topicText}>{currentQuestion?.topic}</Text>
            </View>
          </View>
          <TouchableOpacity
            style={styles.bookmarkButton}
            onPress={() => toggleBookmark(currentQuestion.id)}
          >
            <MaterialCommunityIcons
              name={isBookmarked ? 'bookmark' : 'bookmark-outline'}
              size={24}
              color={isBookmarked ? '#F59E0B' : '#64748B'}
            />
          </TouchableOpacity>
        </View>

        <Text style={styles.questionText}>
          Q{currentQuestionIndex + 1}. {currentQuestion?.question_text}
        </Text>

        <View style={styles.optionsContainer}>
          {currentQuestion?.options.map((option, index) => (
            <TouchableOpacity
              key={index}
              style={[
                styles.optionButton,
                selectedAnswer === index && styles.optionSelected,
              ]}
              onPress={() => setAnswer(currentQuestion.id, index)}
            >
              <View style={[
                styles.optionIndex,
                selectedAnswer === index && styles.optionIndexSelected,
              ]}>
                <Text style={[
                  styles.optionIndexText,
                  selectedAnswer === index && styles.optionIndexTextSelected,
                ]}>
                  {String.fromCharCode(65 + index)}
                </Text>
              </View>
              <Text style={[
                styles.optionText,
                selectedAnswer === index && styles.optionTextSelected,
              ]}>
                {option}
              </Text>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>

      {/* Navigation Footer */}
      <View style={styles.footer}>
        <TouchableOpacity
          style={[styles.navButton, currentQuestionIndex === 0 && styles.navButtonDisabled]}
          onPress={() => goToQuestion(Math.max(0, currentQuestionIndex - 1))}
          disabled={currentQuestionIndex === 0}
        >
          <MaterialCommunityIcons
            name="chevron-left"
            size={24}
            color={currentQuestionIndex === 0 ? '#475569' : '#F8FAFC'}
          />
          <Text style={[
            styles.navButtonText,
            currentQuestionIndex === 0 && styles.navButtonTextDisabled
          ]}>Prev</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.submitButton} onPress={handleSubmit}>
          <MaterialCommunityIcons name="check" size={20} color="#FFFFFF" />
          <Text style={styles.submitButtonText}>Submit</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[
            styles.navButton,
            currentQuestionIndex === questions.length - 1 && styles.navButtonDisabled
          ]}
          onPress={() => goToQuestion(Math.min(questions.length - 1, currentQuestionIndex + 1))}
          disabled={currentQuestionIndex === questions.length - 1}
        >
          <Text style={[
            styles.navButtonText,
            currentQuestionIndex === questions.length - 1 && styles.navButtonTextDisabled
          ]}>Next</Text>
          <MaterialCommunityIcons
            name="chevron-right"
            size={24}
            color={currentQuestionIndex === questions.length - 1 ? '#475569' : '#F8FAFC'}
          />
        </TouchableOpacity>
      </View>

      {/* Question Navigator Modal */}
      <Modal
        visible={showNavigator}
        animationType="slide"
        transparent={true}
        onRequestClose={() => setShowNavigator(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.navigatorModal}>
            <View style={styles.navigatorHeader}>
              <Text style={styles.navigatorTitle}>Question Navigator</Text>
              <TouchableOpacity onPress={() => setShowNavigator(false)}>
                <MaterialCommunityIcons name="close" size={24} color="#F8FAFC" />
              </TouchableOpacity>
            </View>

            <View style={styles.legendContainer}>
              <View style={styles.legendItem}>
                <View style={[styles.legendDot, styles.legendAnswered]} />
                <Text style={styles.legendText}>Answered</Text>
              </View>
              <View style={styles.legendItem}>
                <View style={[styles.legendDot, styles.legendBookmarked]} />
                <Text style={styles.legendText}>Bookmarked</Text>
              </View>
              <View style={styles.legendItem}>
                <View style={[styles.legendDot, styles.legendUnanswered]} />
                <Text style={styles.legendText}>Not Answered</Text>
              </View>
            </View>

            <ScrollView style={styles.navigatorScroll}>
              <View style={styles.questionGrid}>
                {questions.map((q, index) => {
                  const isAnswered = answers[q.id] !== undefined;
                  const isMarked = bookmarkedQuestions.includes(q.id);
                  const isCurrent = index === currentQuestionIndex;

                  return (
                    <TouchableOpacity
                      key={q.id}
                      style={[
                        styles.gridItem,
                        isAnswered && styles.gridItemAnswered,
                        isMarked && styles.gridItemBookmarked,
                        isCurrent && styles.gridItemCurrent,
                      ]}
                      onPress={() => goToQuestion(index)}
                    >
                      <Text style={[
                        styles.gridItemText,
                        (isAnswered || isCurrent) && styles.gridItemTextActive,
                      ]}>
                        {index + 1}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </ScrollView>

            <View style={styles.navigatorStats}>
              <Text style={styles.statItem}>
                Answered: {Object.keys(answers).length}/{questions.length}
              </Text>
              <Text style={styles.statItem}>
                Bookmarked: {bookmarkedQuestions.length}
              </Text>
            </View>
          </View>
        </View>
      </Modal>
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
  preExamContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  preExamCard: {
    backgroundColor: '#1E293B',
    borderRadius: 20,
    padding: 24,
    alignItems: 'center',
    width: '100%',
    maxWidth: 400,
  },
  preExamTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#F8FAFC',
    textAlign: 'center',
    marginTop: 16,
    marginBottom: 24,
  },
  preExamStats: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    borderRadius: 12,
    padding: 16,
    marginBottom: 20,
  },
  preExamStat: {
    flex: 1,
    alignItems: 'center',
  },
  preExamStatDivider: {
    width: 1,
    height: 40,
    backgroundColor: '#334155',
    marginHorizontal: 16,
  },
  preExamStatValue: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 8,
  },
  preExamStatLabel: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 4,
  },
  preExamInfo: {
    width: '100%',
    gap: 8,
    marginBottom: 24,
  },
  preExamInfoItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  preExamInfoText: {
    fontSize: 14,
    color: '#94A3B8',
  },
  startButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#3B82F6',
    paddingVertical: 16,
    paddingHorizontal: 32,
    borderRadius: 12,
    width: '100%',
    marginBottom: 12,
  },
  startButtonText: {
    fontSize: 18,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  cancelButton: {
    paddingVertical: 12,
  },
  cancelButtonText: {
    fontSize: 14,
    color: '#64748B',
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
  exitButton: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
  },
  questionCounter: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#1E293B',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 8,
  },
  questionCounterText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  timerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#1E3A5F',
    paddingHorizontal: 12,
    paddingVertical: 8,
    borderRadius: 8,
  },
  timerWarning: {
    backgroundColor: '#450A0A',
  },
  timerText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#3B82F6',
  },
  timerTextWarning: {
    color: '#EF4444',
  },
  questionContainer: {
    flex: 1,
  },
  questionContent: {
    padding: 20,
  },
  questionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 16,
  },
  questionBadges: {
    flexDirection: 'row',
    gap: 8,
    flexWrap: 'wrap',
    flex: 1,
  },
  difficultyBadge: {
    backgroundColor: '#1E293B',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
  },
  difficultyText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#94A3B8',
  },
  topicBadge: {
    backgroundColor: '#1E3A5F',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
  },
  topicText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#3B82F6',
  },
  bookmarkButton: {
    padding: 4,
  },
  questionText: {
    fontSize: 17,
    fontWeight: '500',
    color: '#F8FAFC',
    lineHeight: 26,
    marginBottom: 24,
  },
  optionsContainer: {
    gap: 12,
  },
  optionButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    borderWidth: 2,
    borderColor: 'transparent',
  },
  optionSelected: {
    backgroundColor: '#1E3A5F',
    borderColor: '#3B82F6',
  },
  optionIndex: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#0F172A',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  optionIndexSelected: {
    backgroundColor: '#3B82F6',
  },
  optionIndexText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
  },
  optionIndexTextSelected: {
    color: '#FFFFFF',
  },
  optionText: {
    flex: 1,
    fontSize: 15,
    color: '#CBD5E1',
    lineHeight: 22,
  },
  optionTextSelected: {
    color: '#F8FAFC',
  },
  footer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderTopWidth: 1,
    borderTopColor: '#1E293B',
    backgroundColor: '#0F172A',
  },
  navButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingVertical: 10,
    paddingHorizontal: 16,
    backgroundColor: '#1E293B',
    borderRadius: 10,
  },
  navButtonDisabled: {
    opacity: 0.5,
  },
  navButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  navButtonTextDisabled: {
    color: '#475569',
  },
  submitButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 10,
    paddingHorizontal: 20,
    backgroundColor: '#22C55E',
    borderRadius: 10,
  },
  submitButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    justifyContent: 'flex-end',
  },
  navigatorModal: {
    backgroundColor: '#1E293B',
    borderTopLeftRadius: 24,
    borderTopRightRadius: 24,
    maxHeight: '80%',
    padding: 20,
  },
  navigatorHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  navigatorTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  legendContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingVertical: 12,
    backgroundColor: '#0F172A',
    borderRadius: 12,
    marginBottom: 16,
  },
  legendItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  legendDot: {
    width: 12,
    height: 12,
    borderRadius: 3,
  },
  legendAnswered: {
    backgroundColor: '#22C55E',
  },
  legendBookmarked: {
    backgroundColor: '#F59E0B',
  },
  legendUnanswered: {
    backgroundColor: '#475569',
  },
  legendText: {
    fontSize: 12,
    color: '#94A3B8',
  },
  navigatorScroll: {
    maxHeight: 300,
  },
  questionGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  gridItem: {
    width: (width - 80) / 8,
    aspectRatio: 1,
    borderRadius: 8,
    backgroundColor: '#0F172A',
    justifyContent: 'center',
    alignItems: 'center',
  },
  gridItemAnswered: {
    backgroundColor: '#22C55E',
  },
  gridItemBookmarked: {
    backgroundColor: '#F59E0B',
  },
  gridItemCurrent: {
    backgroundColor: '#3B82F6',
  },
  gridItemText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
  },
  gridItemTextActive: {
    color: '#FFFFFF',
  },
  navigatorStats: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: '#334155',
    marginTop: 16,
  },
  statItem: {
    fontSize: 14,
    color: '#94A3B8',
  },
});
