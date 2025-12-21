import axios from 'axios';
import Constants from 'expo-constants';

const API_URL = process.env.EXPO_PUBLIC_BACKEND_URL || 'http://localhost:8001';

const api = axios.create({
  baseURL: `${API_URL}/api`,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Subject {
  id: string;
  name: string;
  description: string;
  icon: string;
  color: string;
  total_papers: number;
  total_questions: number;
}

export interface Paper {
  id: string;
  subject_id: string;
  paper_number: number;
  is_master: boolean;
  title: string;
  total_questions: number;
  duration_minutes: number;
}

export interface Question {
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

export interface Attempt {
  id: string;
  user_id: string;
  paper_id: string;
  subject_id: string;
  answers: Record<string, number>;
  correct_count: number;
  wrong_count: number;
  skipped_count: number;
  total_questions: number;
  score_percentage: number;
  time_taken_seconds: number;
  timer_mode: string;
  created_at: string;
}

export interface Analytics {
  total_attempts: number;
  total_questions_attempted: number;
  overall_accuracy: number;
  subject_performance: {
    subject_id: string;
    subject_name: string;
    attempts: number;
    accuracy: number;
    best_score: number;
    average_score: number;
  }[];
  recent_scores: { date: string; score: number }[];
  best_score: number;
  average_score: number;
}

export interface UserSettings {
  id: string;
  user_id: string;
  timer_mode: 'total' | 'per_question';
  total_time_minutes: number;
  per_question_seconds: number;
  show_timer: boolean;
}

export const fetchSubjects = async (): Promise<Subject[]> => {
  const response = await api.get('/subjects');
  return response.data;
};

export const fetchSubject = async (id: string): Promise<Subject> => {
  const response = await api.get(`/subjects/${id}`);
  return response.data;
};

export const fetchPapers = async (subjectId: string): Promise<Paper[]> => {
  const response = await api.get(`/subjects/${subjectId}/papers`);
  return response.data;
};

export const fetchPaper = async (paperId: string): Promise<Paper> => {
  const response = await api.get(`/papers/${paperId}`);
  return response.data;
};

export const fetchQuestions = async (paperId: string): Promise<Question[]> => {
  const response = await api.get(`/papers/${paperId}/questions`);
  return response.data;
};

export const submitAttempt = async (data: {
  paper_id: string;
  subject_id: string;
  answers: Record<string, number>;
  time_taken_seconds: number;
  timer_mode: string;
}): Promise<Attempt> => {
  const response = await api.post('/attempts', data);
  return response.data;
};

export const fetchAttempts = async (params?: {
  subject_id?: string;
  paper_id?: string;
}): Promise<Attempt[]> => {
  const response = await api.get('/attempts', { params });
  return response.data;
};

export const fetchAnalytics = async (): Promise<Analytics> => {
  const response = await api.get('/analytics');
  return response.data;
};

export const fetchAttemptReview = async (attemptId: string) => {
  const response = await api.get(`/attempt/${attemptId}/review`);
  return response.data;
};

export const fetchSettings = async (): Promise<UserSettings> => {
  const response = await api.get('/settings');
  return response.data;
};

export const updateSettings = async (settings: Partial<UserSettings>): Promise<UserSettings> => {
  const response = await api.put('/settings', settings);
  return response.data;
};

export default api;
