import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface ExamState {
  currentQuestionIndex: number;
  answers: Record<string, number>;
  bookmarkedQuestions: string[];
  timeRemaining: number;
  isExamActive: boolean;
  timerMode: 'total' | 'per_question';
  showTimer: boolean;
  
  setCurrentQuestion: (index: number) => void;
  setAnswer: (questionId: string, optionIndex: number) => void;
  toggleBookmark: (questionId: string) => void;
  setTimeRemaining: (time: number) => void;
  startExam: (totalTime: number, mode: 'total' | 'per_question') => void;
  endExam: () => void;
  resetExam: () => void;
  setTimerMode: (mode: 'total' | 'per_question') => void;
  setShowTimer: (show: boolean) => void;
}

export const useExamStore = create<ExamState>()(
  persist(
    (set) => ({
      currentQuestionIndex: 0,
      answers: {},
      bookmarkedQuestions: [],
      timeRemaining: 0,
      isExamActive: false,
      timerMode: 'total',
      showTimer: true,

      setCurrentQuestion: (index) => set({ currentQuestionIndex: index }),
      
      setAnswer: (questionId, optionIndex) =>
        set((state) => ({
          answers: { ...state.answers, [questionId]: optionIndex },
        })),
      
      toggleBookmark: (questionId) =>
        set((state) => ({
          bookmarkedQuestions: state.bookmarkedQuestions.includes(questionId)
            ? state.bookmarkedQuestions.filter((id) => id !== questionId)
            : [...state.bookmarkedQuestions, questionId],
        })),
      
      setTimeRemaining: (time) => set({ timeRemaining: time }),
      
      startExam: (totalTime, mode) =>
        set({
          isExamActive: true,
          timeRemaining: totalTime,
          answers: {},
          currentQuestionIndex: 0,
          bookmarkedQuestions: [],
          timerMode: mode,
        }),
      
      endExam: () => set({ isExamActive: false }),
      
      resetExam: () =>
        set({
          currentQuestionIndex: 0,
          answers: {},
          bookmarkedQuestions: [],
          timeRemaining: 0,
          isExamActive: false,
        }),
      
      setTimerMode: (mode) => set({ timerMode: mode }),
      setShowTimer: (show) => set({ showTimer: show }),
    }),
    {
      name: 'exam-storage',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({
        timerMode: state.timerMode,
        showTimer: state.showTimer,
      }),
    }
  )
);
