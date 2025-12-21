// Use native fetch for API calls

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

const apiCall = async (endpoint: string, options?: RequestInit) => {
  const response = await fetch(`/api${endpoint}`, {
    headers: {
      'Content-Type': 'application/json',
    },
    ...options,
  });
  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }
  return response.json();
};

export const fetchSubjects = async (): Promise<Subject[]> => {
  return apiCall('/subjects');
};

export const fetchSubject = async (id: string): Promise<Subject> => {
  return apiCall(`/subjects/${id}`);
};

export const fetchPapers = async (subjectId: string): Promise<Paper[]> => {
  return apiCall(`/subjects/${subjectId}/papers`);
};

export const fetchPaper = async (paperId: string): Promise<Paper> => {
  return apiCall(`/papers/${paperId}`);
};

export const fetchQuestions = async (paperId: string): Promise<Question[]> => {
  return apiCall(`/papers/${paperId}/questions`);
};

export const submitAttempt = async (data: {
  paper_id: string;
  subject_id: string;
  answers: Record<string, number>;
  time_taken_seconds: number;
  timer_mode: string;
}): Promise<Attempt> => {
  return apiCall('/attempts', {
    method: 'POST',
    body: JSON.stringify(data),
  });
};

export const fetchAttempts = async (params?: {
  subject_id?: string;
  paper_id?: string;
}): Promise<Attempt[]> => {
  const searchParams = new URLSearchParams();
  if (params?.subject_id) searchParams.append('subject_id', params.subject_id);
  if (params?.paper_id) searchParams.append('paper_id', params.paper_id);
  const query = searchParams.toString() ? `?${searchParams.toString()}` : '';
  return apiCall(`/attempts${query}`);
};

export const fetchAnalytics = async (): Promise<Analytics> => {
  return apiCall('/analytics');
};

export const fetchAttemptReview = async (attemptId: string) => {
  return apiCall(`/attempt/${attemptId}/review`);
};

export const fetchSettings = async (): Promise<UserSettings> => {
  return apiCall('/settings');
};

export const updateSettings = async (settings: Partial<UserSettings>): Promise<UserSettings> => {
  return apiCall('/settings', {
    method: 'PUT',
    body: JSON.stringify(settings),
  });
};
