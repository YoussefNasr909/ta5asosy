export type OptionId = 'A' | 'B' | 'C' | 'D';

export interface QuestionOption {
  id: OptionId;
  text: string;
}

export type TopicType = 'Computer Networking' | 'Database Fundamentals' | 'SQL';
export type DifficultyType = 'easy' | 'medium' | 'hard';
export type SourceType = 'pdf' | 'generated';

export interface Question {
  id: string;
  topic: TopicType;
  subtopic: string;
  question: string;
  options: QuestionOption[];
  correctAnswer: OptionId;
  explanation: string;
  difficulty: DifficultyType;
  sourceType: SourceType;
  sourceFile: string;
  sourcePage?: number;
  reviewStatus: string;
}

export type ExamMode = 'practice' | 'exam';
export type QuestionOrder = 'random' | 'sequential';

export interface ExamConfig {
  topic: TopicType | 'All Topics';
  subtopic?: string | 'All Subtopics';
  difficulty: DifficultyType | 'mixed';
  sourceType: SourceType | 'all';
  count: number;
  mode: ExamMode;
  order: QuestionOrder;
  shuffleOptions: boolean;
  timed: boolean;
  timeLimitMinutes: number;
  passingScore: number;
}

export interface ActiveExamQuestion extends Question {
  userSelectedAnswer?: OptionId;
  isFlagged?: boolean;
  isRevealed?: boolean;
}

export interface ExamAttemptRecord {
  id: string;
  timestamp: string;
  config: ExamConfig;
  totalQuestions: number;
  correctCount: number;
  incorrectCount: number;
  unansweredCount: number;
  scorePercentage: number;
  passed: boolean;
  durationSeconds: number;
  topicStats: Record<string, { total: number; correct: number }>;
  difficultyStats: Record<string, { total: number; correct: number }>;
  questionsSnapshot: ActiveExamQuestion[];
}

export interface ActiveExamState {
  config: ExamConfig;
  questions: ActiveExamQuestion[];
  currentIndex: number;
  startTime: number;
  timeRemainingSeconds: number;
  isSubmitted: boolean;
}

export interface QuestionHistoryItem {
  attempts: number;
  correct: number;
  lastAnswered?: string;
  lastCorrect?: boolean;
}

export interface UserPreferences {
  theme: 'dark' | 'light';
  soundEnabled: boolean;
  keyboardShortcutsEnabled: boolean;
}

export interface UserProgress {
  attempts: ExamAttemptRecord[];
  incorrectQuestionIds: string[];
  flaggedQuestionIds: string[];
  questionHistory: Record<string, QuestionHistoryItem>;
  activeExam?: ActiveExamState;
  preferences: UserPreferences;
}
