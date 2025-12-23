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
  Platform,
} from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import Constants from 'expo-constants';

const { width } = Dimensions.get('window');

// Get backend URL from environment
const getBackendUrl = () => {
  const backendUrl = Constants.expoConfig?.extra?.EXPO_PUBLIC_BACKEND_URL 
    || process.env.EXPO_PUBLIC_BACKEND_URL 
    || '';
  return backendUrl;
};

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

export default function ExamScreen() {
  const router = useRouter();
  const { paperId } = useLocalSearchParams<{ paperId: string }>();
  const scrollRef = useRef<ScrollView>(null);
  const [showNavigator, setShowNavigator] = useState(false);
  const [examStarted, setExamStarted] = useState(false);
  const [startTime, setStartTime] = useState<number>(0);
  const [showCompleteModal, setShowCompleteModal] = useState(false);
  const [showResultModal, setShowResultModal] = useState(false);
  const [showAnswerKey, setShowAnswerKey] = useState(false);
  const [finalResult, setFinalResult] = useState<{
    correct: number;
    wrong: number;
    skipped: number;
    scorePercentage: number;
    rawScore: string;
    maxScore: number;
    timeTaken: string;
  } | null>(null);

  // State management
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [bookmarkedQuestions, setBookmarkedQuestions] = useState<string[]>([]);
  const [timeRemaining, setTimeRemaining] = useState(5400); // 90 minutes
  const [showTimer, setShowTimerState] = useState(true);
  const [showingFeedback, setShowingFeedback] = useState(false);
  const [feedbackAnswer, setFeedbackAnswer] = useState<number | null>(null);
  const [allowResubmission, setAllowResubmission] = useState(true); // Allow changing answers by default

  // Data states
  const [questions, setQuestions] = useState<Question[]>([]);
  const [paper, setPaper] = useState<Paper | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch questions from backend
  useEffect(() => {
    const fetchQuestions = async () => {
      if (!paperId) return;
      
      setIsLoading(true);
      setError(null);
      
      try {
        const backendUrl = getBackendUrl();
        
        // Fetch paper details
        const paperResponse = await fetch(`${backendUrl}/api/papers/${paperId}`);
        if (paperResponse.ok) {
          const paperData = await paperResponse.json();
          setPaper(paperData);
        }
        
        // Fetch questions
        const questionsResponse = await fetch(`${backendUrl}/api/papers/${paperId}/questions`);
        if (!questionsResponse.ok) {
          throw new Error('Failed to fetch questions');
        }
        
        const questionsData = await questionsResponse.json();
        
        if (questionsData && questionsData.length > 0) {
          setQuestions(questionsData);
        } else {
          setError('No questions found for this paper');
        }
      } catch (err) {
        console.error('Error fetching questions:', err);
        setError('Failed to load questions. Please try again.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchQuestions();
  }, [paperId]);

  // Timer effect
  useEffect(() => {
    if (!examStarted || !showTimer) return;

    const interval = setInterval(() => {
      setTimeRemaining((prev) => {
        if (prev <= 1) {
          handleTimeUp();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [examStarted, showTimer]);

  const handleTimeUp = useCallback(() => {
    calculateAndShowResult();
  }, [questions, answers, startTime]);

  const handleStartExam = useCallback(() => {
    setExamStarted(true);
    setStartTime(Date.now());
    setTimeRemaining(5400); // 90 minutes
    setAnswers({});
    setCurrentQuestionIndex(0);
    setBookmarkedQuestions([]);
  }, []);

  const calculateAndShowResult = useCallback(() => {
    if (!questions || questions.length === 0) return;

    const timeTaken = Math.floor((Date.now() - startTime) / 1000);
    
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
    
    // Calculate score with negative marking: +1 for correct, -0.25 for wrong
    const rawScore = correct - (wrong * 0.25);
    const maxScore = questions.length; // Maximum possible score
    const scorePercentage = Math.round((Math.max(0, rawScore) / maxScore) * 100);

    setFinalResult({
      correct,
      wrong,
      skipped,
      scorePercentage,
      rawScore: rawScore.toFixed(2),
      maxScore,
      timeTaken: formatTime(timeTaken),
    });
    
    setShowCompleteModal(false);
    setShowResultModal(true);
  }, [questions, answers, startTime]);

  const handleCompleteTest = useCallback(() => {
    setShowCompleteModal(true);
  }, []);

  const handleConfirmComplete = useCallback(() => {
    calculateAndShowResult();
  }, [calculateAndShowResult]);

  const handleExit = () => {
    if (Platform.OS === 'web') {
      if (window.confirm('Are you sure you want to exit? Your progress will be lost.')) {
        router.back();
      }
    } else {
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
    }
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
    scrollRef.current?.scrollTo({ y: 0, animated: true });
  };

  const setAnswer = (questionId: string, optionIndex: number) => {
    // Don't allow changing answer while showing feedback
    if (showingFeedback) return;
    
    setAnswers((prev) => ({ ...prev, [questionId]: optionIndex }));
    setFeedbackAnswer(optionIndex);
    setShowingFeedback(true);
    
    // Show feedback for 1.2 seconds, then advance to next question
    setTimeout(() => {
      setShowingFeedback(false);
      setFeedbackAnswer(null);
      
      if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        scrollRef.current?.scrollTo({ y: 0, animated: true });
      }
    }, 1200);
  };

  const toggleBookmark = (questionId: string) => {
    setBookmarkedQuestions((prev) =>
      prev.includes(questionId)
        ? prev.filter((id) => id !== questionId)
        : [...prev, questionId]
    );
  };

  // Loading state
  if (isLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
          <Text style={styles.loadingText}>Loading exam questions...</Text>
        </View>
      </SafeAreaView>
    );
  }

  // Error state
  if (error || !questions || questions.length === 0) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={64} color="#EF4444" />
          <Text style={styles.errorTitle}>Unable to Load Questions</Text>
          <Text style={styles.errorText}>{error || 'No questions available for this paper.'}</Text>
          <TouchableOpacity style={styles.retryButton} onPress={() => router.back()}>
            <Text style={styles.retryButtonText}>Go Back</Text>
          </TouchableOpacity>
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
              name={paper?.is_master ? 'star' : 'file-document'}
              size={48}
              color={paper?.is_master ? '#F59E0B' : '#3B82F6'}
            />
            <Text style={styles.preExamTitle}>{paper?.title || 'Exam'}</Text>
            
            <View style={styles.preExamStats}>
              <View style={styles.preExamStat}>
                <MaterialCommunityIcons name="help-circle" size={24} color="#64748B" />
                <Text style={styles.preExamStatValue}>{questions.length}</Text>
                <Text style={styles.preExamStatLabel}>Questions</Text>
              </View>
              <View style={styles.preExamStatDivider} />
              <View style={styles.preExamStat}>
                <MaterialCommunityIcons name="clock" size={24} color="#64748B" />
                <Text style={styles.preExamStatValue}>{paper?.duration_minutes || 90}</Text>
                <Text style={styles.preExamStatLabel}>Minutes</Text>
              </View>
            </View>

            <View style={styles.preExamInfo}>
              <View style={styles.preExamInfoItem}>
                <MaterialCommunityIcons name="timer" size={18} color="#94A3B8" />
                <Text style={styles.preExamInfoText}>
                  Timer: Total Time ({paper?.duration_minutes || 90} min)
                </Text>
              </View>
              <View style={styles.preExamInfoItem}>
                <MaterialCommunityIcons name="check-circle" size={18} color="#94A3B8" />
                <Text style={styles.preExamInfoText}>
                  +1 for correct, 0 for wrong
                </Text>
              </View>
              <View style={styles.preExamInfoItem}>
                <MaterialCommunityIcons name="auto-fix" size={18} color="#94A3B8" />
                <Text style={styles.preExamInfoText}>
                  Auto-advance after selecting answer
                </Text>
              </View>
            </View>

            {/* Resubmission Toggle */}
            <TouchableOpacity
              style={styles.resubmissionToggle}
              onPress={() => setAllowResubmission(!allowResubmission)}
              activeOpacity={0.7}
            >
              <View style={[
                styles.checkbox,
                allowResubmission && styles.checkboxChecked
              ]}>
                {allowResubmission && (
                  <MaterialCommunityIcons name="check" size={16} color="#FFFFFF" />
                )}
              </View>
              <Text style={styles.resubmissionText}>
                Allow resubmission of previously answered questions
              </Text>
            </TouchableOpacity>

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
  const answeredCount = Object.keys(answers).length;
  const unansweredCount = questions.length - answeredCount;

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
            <View style={[
              styles.difficultyBadge,
              currentQuestion?.difficulty === 'hard' && styles.difficultyHard,
              currentQuestion?.difficulty === 'easy' && styles.difficultyEasy,
            ]}>
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
          {currentQuestion?.options.map((option, index) => {
            const isSelected = selectedAnswer === index;
            const isCorrectOption = currentQuestion.correct_option === index;
            const isWrongSelection = showingFeedback && feedbackAnswer === index && !isCorrectOption;
            const showCorrectHighlight = showingFeedback && isCorrectOption;
            const showWrongHighlight = isWrongSelection;
            
            return (
              <TouchableOpacity
                key={index}
                style={[
                  styles.optionButton,
                  isSelected && !showingFeedback && styles.optionSelected,
                  showCorrectHighlight && styles.optionCorrect,
                  showWrongHighlight && styles.optionWrong,
                ]}
                onPress={() => setAnswer(currentQuestion.id, index)}
                disabled={showingFeedback}
              >
                <View style={[
                  styles.optionIndex,
                  isSelected && !showingFeedback && styles.optionIndexSelected,
                  showCorrectHighlight && styles.optionIndexCorrect,
                  showWrongHighlight && styles.optionIndexWrong,
                ]}>
                  <Text style={[
                    styles.optionIndexText,
                    isSelected && !showingFeedback && styles.optionIndexTextSelected,
                    (showCorrectHighlight || showWrongHighlight) && styles.optionIndexTextFeedback,
                  ]}>
                    {String.fromCharCode(65 + index)}
                  </Text>
                </View>
                <Text style={[
                  styles.optionText,
                  isSelected && !showingFeedback && styles.optionTextSelected,
                  showCorrectHighlight && styles.optionTextCorrect,
                  showWrongHighlight && styles.optionTextWrong,
                ]}>
                  {option}
                </Text>
                {showCorrectHighlight && (
                  <MaterialCommunityIcons name="check-circle" size={24} color="#22C55E" style={styles.feedbackIcon} />
                )}
                {showWrongHighlight && (
                  <MaterialCommunityIcons name="close-circle" size={24} color="#EF4444" style={styles.feedbackIcon} />
                )}
              </TouchableOpacity>
            );
          })}
        </View>
      </ScrollView>

      {/* Navigation Footer */}
      <View style={styles.footer}>
        {allowResubmission ? (
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
        ) : (
          <View style={styles.navButtonPlaceholder} />
        )}

        <TouchableOpacity style={styles.completeButton} onPress={handleCompleteTest}>
          <MaterialCommunityIcons name="flag-checkered" size={18} color="#FFFFFF" />
          <Text style={styles.completeButtonText}>Complete</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[
            styles.nextButton,
            currentQuestionIndex === questions.length - 1 && styles.nextButtonDisabled
          ]}
          onPress={() => goToQuestion(Math.min(questions.length - 1, currentQuestionIndex + 1))}
          disabled={currentQuestionIndex === questions.length - 1}
        >
          <Text style={[
            styles.nextButtonText,
            currentQuestionIndex === questions.length - 1 && styles.nextButtonTextDisabled
          ]}>Next</Text>
          <MaterialCommunityIcons
            name="chevron-right"
            size={24}
            color={currentQuestionIndex === questions.length - 1 ? '#475569' : '#FFFFFF'}
          />
        </TouchableOpacity>
      </View>

      {/* Complete Test Confirmation Modal */}
      <Modal
        visible={showCompleteModal}
        animationType="fade"
        transparent={true}
        onRequestClose={() => setShowCompleteModal(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.confirmModal}>
            <MaterialCommunityIcons name="flag-checkered" size={48} color="#EF4444" />
            <Text style={styles.confirmTitle}>Complete Test?</Text>
            <Text style={styles.confirmText}>
              You have answered {answeredCount} out of {questions.length} questions.
            </Text>
            {unansweredCount > 0 && (
              <Text style={styles.confirmWarning}>
                ⚠️ {unansweredCount} question{unansweredCount > 1 ? 's are' : ' is'} still unanswered!
              </Text>
            )}
            <Text style={styles.confirmSubtext}>
              This will be your final submission. Are you sure?
            </Text>
            
            <View style={styles.confirmButtons}>
              <TouchableOpacity
                style={styles.confirmCancelButton}
                onPress={() => setShowCompleteModal(false)}
              >
                <Text style={styles.confirmCancelText}>Cancel</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.confirmSubmitButton}
                onPress={handleConfirmComplete}
              >
                <Text style={styles.confirmSubmitText}>Submit Test</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* Result Modal */}
      <Modal
        visible={showResultModal}
        animationType="fade"
        transparent={true}
        onRequestClose={() => {}}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.resultModal}>
            <MaterialCommunityIcons 
              name={finalResult && finalResult.scorePercentage >= 60 ? "trophy" : "school"} 
              size={64} 
              color={finalResult && finalResult.scorePercentage >= 60 ? "#F59E0B" : "#3B82F6"} 
            />
            <Text style={styles.resultTitle}>Test Completed!</Text>
            
            <View style={styles.scoreCircle}>
              <Text style={styles.scorePercentage}>{finalResult?.scorePercentage}%</Text>
              <Text style={styles.scoreLabel}>Score</Text>
            </View>

            <View style={styles.resultStats}>
              <View style={styles.resultStatItem}>
                <View style={[styles.resultStatDot, { backgroundColor: '#22C55E' }]} />
                <Text style={styles.resultStatText}>Correct: {finalResult?.correct} (+{finalResult?.correct})</Text>
              </View>
              <View style={styles.resultStatItem}>
                <View style={[styles.resultStatDot, { backgroundColor: '#EF4444' }]} />
                <Text style={styles.resultStatText}>Wrong: {finalResult?.wrong} (-{((finalResult?.wrong || 0) * 0.25).toFixed(2)})</Text>
              </View>
              <View style={styles.resultStatItem}>
                <View style={[styles.resultStatDot, { backgroundColor: '#64748B' }]} />
                <Text style={styles.resultStatText}>Skipped: {finalResult?.skipped} (0)</Text>
              </View>
              <View style={styles.resultStatItem}>
                <MaterialCommunityIcons name="calculator" size={16} color="#3B82F6" />
                <Text style={[styles.resultStatText, { color: '#3B82F6', fontWeight: '700' }]}>
                  Final Score: {finalResult?.rawScore}/{finalResult?.maxScore}
                </Text>
              </View>
              <View style={styles.resultStatItem}>
                <MaterialCommunityIcons name="clock-outline" size={16} color="#94A3B8" />
                <Text style={styles.resultStatText}>Time: {finalResult?.timeTaken}</Text>
              </View>
            </View>

            <View style={styles.negativeMarkingNote}>
              <MaterialCommunityIcons name="alert-circle-outline" size={14} color="#F59E0B" />
              <Text style={styles.negativeMarkingText}>
                Negative Marking: -0.25 per wrong answer
              </Text>
            </View>

            <TouchableOpacity
              style={styles.answerKeyButton}
              onPress={() => {
                setShowResultModal(false);
                setShowAnswerKey(true);
              }}
            >
              <MaterialCommunityIcons name="key-variant" size={20} color="#3B82F6" />
              <Text style={styles.answerKeyButtonText}>View Answer Key</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.resultHomeButton}
              onPress={() => router.replace('/')}
            >
              <MaterialCommunityIcons name="home" size={20} color="#FFFFFF" />
              <Text style={styles.resultHomeText}>Go to Home</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>

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

      {/* Answer Key Modal */}
      <Modal
        visible={showAnswerKey}
        animationType="slide"
        transparent={false}
        onRequestClose={() => setShowAnswerKey(false)}
      >
        <SafeAreaView style={styles.answerKeyContainer}>
          <View style={styles.answerKeyHeader}>
            <TouchableOpacity
              style={styles.answerKeyBackButton}
              onPress={() => setShowAnswerKey(false)}
            >
              <MaterialCommunityIcons name="arrow-left" size={24} color="#F8FAFC" />
            </TouchableOpacity>
            <Text style={styles.answerKeyTitle}>Answer Key</Text>
            <View style={styles.answerKeyScoreBadge}>
              <Text style={styles.answerKeyScoreText}>{finalResult?.scorePercentage}%</Text>
            </View>
          </View>

          <ScrollView 
            style={styles.answerKeyScroll}
            contentContainerStyle={styles.answerKeyContent}
          >
            {questions.map((question, qIndex) => {
              const userAnswer = answers[question.id];
              const isCorrect = userAnswer === question.correct_option;
              const isSkipped = userAnswer === undefined;

              return (
                <View key={question.id} style={styles.answerKeyItem}>
                  <View style={styles.answerKeyQuestionHeader}>
                    <View style={[
                      styles.answerKeyStatus,
                      isCorrect && styles.answerKeyStatusCorrect,
                      !isCorrect && !isSkipped && styles.answerKeyStatusWrong,
                      isSkipped && styles.answerKeyStatusSkipped,
                    ]}>
                      <MaterialCommunityIcons 
                        name={isCorrect ? 'check' : isSkipped ? 'minus' : 'close'} 
                        size={14} 
                        color="#FFFFFF" 
                      />
                    </View>
                    <Text style={styles.answerKeyQuestionNumber}>Q{qIndex + 1}</Text>
                    {question.difficulty && (
                      <View style={[
                        styles.answerKeyDifficulty,
                        question.difficulty === 'hard' && styles.difficultyHard,
                        question.difficulty === 'easy' && styles.difficultyEasy,
                      ]}>
                        <Text style={styles.answerKeyDifficultyText}>
                          {question.difficulty.toUpperCase()}
                        </Text>
                      </View>
                    )}
                  </View>

                  <Text style={styles.answerKeyQuestionText}>
                    {question.question_text}
                  </Text>

                  <View style={styles.answerKeyOptions}>
                    {question.options.map((option, optIndex) => {
                      const isCorrectOption = optIndex === question.correct_option;
                      const isUserAnswer = optIndex === userAnswer;
                      const showWrong = isUserAnswer && !isCorrectOption;

                      return (
                        <View 
                          key={optIndex} 
                          style={[
                            styles.answerKeyOption,
                            isCorrectOption && styles.answerKeyOptionCorrect,
                            showWrong && styles.answerKeyOptionWrong,
                          ]}
                        >
                          <View style={[
                            styles.answerKeyOptionIndex,
                            isCorrectOption && styles.answerKeyOptionIndexCorrect,
                            showWrong && styles.answerKeyOptionIndexWrong,
                          ]}>
                            <Text style={[
                              styles.answerKeyOptionIndexText,
                              (isCorrectOption || showWrong) && styles.answerKeyOptionIndexTextActive,
                            ]}>
                              {String.fromCharCode(65 + optIndex)}
                            </Text>
                          </View>
                          <Text style={[
                            styles.answerKeyOptionText,
                            isCorrectOption && styles.answerKeyOptionTextCorrect,
                            showWrong && styles.answerKeyOptionTextWrong,
                          ]}>
                            {option}
                          </Text>
                          {isCorrectOption && (
                            <MaterialCommunityIcons name="check-circle" size={18} color="#22C55E" />
                          )}
                          {showWrong && (
                            <MaterialCommunityIcons name="close-circle" size={18} color="#EF4444" />
                          )}
                        </View>
                      );
                    })}
                  </View>

                  {question.explanation && (
                    <View style={styles.answerKeyExplanation}>
                      <MaterialCommunityIcons name="lightbulb-outline" size={16} color="#F59E0B" />
                      <Text style={styles.answerKeyExplanationText}>
                        {question.explanation}
                      </Text>
                    </View>
                  )}
                </View>
              );
            })}
          </ScrollView>

          <View style={styles.answerKeyFooter}>
            <TouchableOpacity
              style={styles.answerKeyHomeButton}
              onPress={() => router.replace('/')}
            >
              <MaterialCommunityIcons name="home" size={20} color="#FFFFFF" />
              <Text style={styles.answerKeyHomeText}>Go to Home</Text>
            </TouchableOpacity>
          </View>
        </SafeAreaView>
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
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  errorTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 16,
    marginBottom: 8,
  },
  errorText: {
    fontSize: 14,
    color: '#94A3B8',
    textAlign: 'center',
    marginBottom: 24,
  },
  retryButton: {
    backgroundColor: '#3B82F6',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
  },
  retryButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
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
    marginBottom: 24,
  },
  preExamInfoItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  preExamInfoText: {
    fontSize: 14,
    color: '#94A3B8',
    marginLeft: 8,
  },
  resubmissionToggle: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    padding: 12,
    borderRadius: 10,
    marginBottom: 24,
    width: '100%',
  },
  checkbox: {
    width: 24,
    height: 24,
    borderRadius: 6,
    borderWidth: 2,
    borderColor: '#475569',
    backgroundColor: 'transparent',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  checkboxChecked: {
    backgroundColor: '#3B82F6',
    borderColor: '#3B82F6',
  },
  resubmissionText: {
    flex: 1,
    fontSize: 13,
    color: '#94A3B8',
    lineHeight: 18,
  },
  startButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
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
    marginLeft: 8,
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
    backgroundColor: '#1E293B',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 8,
  },
  questionCounterText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#F8FAFC',
    marginRight: 8,
  },
  timerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
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
    marginLeft: 6,
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
    flexWrap: 'wrap',
    flex: 1,
  },
  difficultyBadge: {
    backgroundColor: '#1E293B',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
    marginRight: 8,
  },
  difficultyHard: {
    backgroundColor: '#450A0A',
  },
  difficultyEasy: {
    backgroundColor: '#14532D',
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
    marginBottom: 20,
  },
  optionButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    borderWidth: 2,
    borderColor: 'transparent',
    marginBottom: 12,
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
  // Feedback styles for correct/wrong answers
  optionCorrect: {
    backgroundColor: '#14532D',
    borderColor: '#22C55E',
  },
  optionWrong: {
    backgroundColor: '#450A0A',
    borderColor: '#EF4444',
  },
  optionIndexCorrect: {
    backgroundColor: '#22C55E',
  },
  optionIndexWrong: {
    backgroundColor: '#EF4444',
  },
  optionIndexTextFeedback: {
    color: '#FFFFFF',
  },
  optionTextCorrect: {
    color: '#86EFAC',
  },
  optionTextWrong: {
    color: '#FCA5A5',
  },
  feedbackIcon: {
    marginLeft: 8,
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
    paddingVertical: 10,
    paddingHorizontal: 16,
    backgroundColor: '#1E293B',
    borderRadius: 10,
  },
  navButtonPlaceholder: {
    width: 80, // Same approximate width as Prev button
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
  completeButton: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 10,
    paddingHorizontal: 14,
    backgroundColor: '#EF4444',
    borderRadius: 10,
  },
  completeButtonText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#FFFFFF',
    marginLeft: 6,
  },
  nextButton: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 10,
    paddingHorizontal: 16,
    backgroundColor: '#22C55E',
    borderRadius: 10,
  },
  nextButtonDisabled: {
    backgroundColor: '#1E293B',
  },
  nextButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
    marginRight: 4,
  },
  nextButtonTextDisabled: {
    color: '#475569',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  confirmModal: {
    backgroundColor: '#1E293B',
    borderRadius: 20,
    padding: 24,
    alignItems: 'center',
    width: '90%',
    maxWidth: 360,
  },
  confirmTitle: {
    fontSize: 22,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 16,
    marginBottom: 12,
  },
  confirmText: {
    fontSize: 15,
    color: '#CBD5E1',
    textAlign: 'center',
    marginBottom: 8,
  },
  confirmWarning: {
    fontSize: 14,
    color: '#F59E0B',
    textAlign: 'center',
    marginBottom: 8,
    fontWeight: '600',
  },
  confirmSubtext: {
    fontSize: 13,
    color: '#94A3B8',
    textAlign: 'center',
    marginBottom: 24,
  },
  confirmButtons: {
    flexDirection: 'row',
    width: '100%',
  },
  confirmCancelButton: {
    flex: 1,
    paddingVertical: 14,
    backgroundColor: '#334155',
    borderRadius: 10,
    marginRight: 8,
    alignItems: 'center',
  },
  confirmCancelText: {
    fontSize: 15,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  confirmSubmitButton: {
    flex: 1,
    paddingVertical: 14,
    backgroundColor: '#EF4444',
    borderRadius: 10,
    marginLeft: 8,
    alignItems: 'center',
  },
  confirmSubmitText: {
    fontSize: 15,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  resultModal: {
    backgroundColor: '#1E293B',
    borderRadius: 20,
    padding: 24,
    alignItems: 'center',
    width: '90%',
    maxWidth: 360,
  },
  resultTitle: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 16,
    marginBottom: 20,
  },
  scoreCircle: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: '#0F172A',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 4,
    borderColor: '#3B82F6',
    marginBottom: 24,
  },
  scorePercentage: {
    fontSize: 32,
    fontWeight: '700',
    color: '#3B82F6',
  },
  scoreLabel: {
    fontSize: 12,
    color: '#94A3B8',
    marginTop: 2,
  },
  resultStats: {
    width: '100%',
    backgroundColor: '#0F172A',
    borderRadius: 12,
    padding: 16,
    marginBottom: 24,
  },
  resultStatItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  resultStatDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 10,
  },
  resultStatText: {
    fontSize: 14,
    color: '#CBD5E1',
    marginLeft: 4,
  },
  resultHomeButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#3B82F6',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    width: '100%',
  },
  resultHomeText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    marginLeft: 8,
  },
  navigatorModal: {
    backgroundColor: '#1E293B',
    borderTopLeftRadius: 24,
    borderTopRightRadius: 24,
    maxHeight: '80%',
    padding: 20,
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
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
  },
  legendDot: {
    width: 12,
    height: 12,
    borderRadius: 3,
    marginRight: 6,
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
  },
  gridItem: {
    width: (width - 80) / 8,
    aspectRatio: 1,
    borderRadius: 8,
    backgroundColor: '#0F172A',
    justifyContent: 'center',
    alignItems: 'center',
    margin: 4,
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
  // Answer Key Button in Result Modal
  answerKeyButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#1E293B',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    width: '100%',
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#3B82F6',
  },
  answerKeyButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#3B82F6',
    marginLeft: 8,
  },
  // Answer Key Modal Styles
  answerKeyContainer: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  answerKeyHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  answerKeyBackButton: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
  },
  answerKeyTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#F8FAFC',
  },
  answerKeyScoreBadge: {
    backgroundColor: '#1E3A5F',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 8,
  },
  answerKeyScoreText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#3B82F6',
  },
  answerKeyScroll: {
    flex: 1,
  },
  answerKeyContent: {
    padding: 16,
    paddingBottom: 24,
  },
  answerKeyItem: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
  },
  answerKeyQuestionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  answerKeyStatus: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: '#64748B',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 8,
  },
  answerKeyStatusCorrect: {
    backgroundColor: '#22C55E',
  },
  answerKeyStatusWrong: {
    backgroundColor: '#EF4444',
  },
  answerKeyStatusSkipped: {
    backgroundColor: '#64748B',
  },
  answerKeyQuestionNumber: {
    fontSize: 14,
    fontWeight: '700',
    color: '#F8FAFC',
    marginRight: 8,
  },
  answerKeyDifficulty: {
    backgroundColor: '#334155',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 4,
  },
  answerKeyDifficultyText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#94A3B8',
  },
  answerKeyQuestionText: {
    fontSize: 15,
    color: '#E2E8F0',
    lineHeight: 22,
    marginBottom: 12,
  },
  answerKeyOptions: {
    marginBottom: 8,
  },
  answerKeyOption: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    borderRadius: 8,
    padding: 10,
    marginBottom: 6,
    borderWidth: 1,
    borderColor: 'transparent',
  },
  answerKeyOptionCorrect: {
    backgroundColor: '#14532D',
    borderColor: '#22C55E',
  },
  answerKeyOptionWrong: {
    backgroundColor: '#450A0A',
    borderColor: '#EF4444',
  },
  answerKeyOptionIndex: {
    width: 26,
    height: 26,
    borderRadius: 6,
    backgroundColor: '#334155',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 10,
  },
  answerKeyOptionIndexCorrect: {
    backgroundColor: '#22C55E',
  },
  answerKeyOptionIndexWrong: {
    backgroundColor: '#EF4444',
  },
  answerKeyOptionIndexText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#94A3B8',
  },
  answerKeyOptionIndexTextActive: {
    color: '#FFFFFF',
  },
  answerKeyOptionText: {
    flex: 1,
    fontSize: 13,
    color: '#CBD5E1',
    lineHeight: 18,
  },
  answerKeyOptionTextCorrect: {
    color: '#86EFAC',
  },
  answerKeyOptionTextWrong: {
    color: '#FCA5A5',
  },
  answerKeyExplanation: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    backgroundColor: '#422006',
    borderRadius: 8,
    padding: 10,
    marginTop: 8,
  },
  answerKeyExplanationText: {
    flex: 1,
    fontSize: 12,
    color: '#FCD34D',
    lineHeight: 18,
    marginLeft: 8,
  },
  answerKeyFooter: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderTopWidth: 1,
    borderTopColor: '#1E293B',
    backgroundColor: '#0F172A',
  },
  answerKeyHomeButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#3B82F6',
    paddingVertical: 14,
    borderRadius: 12,
  },
  answerKeyHomeText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    marginLeft: 8,
  },
});
