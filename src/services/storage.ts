import { UserProgress, ExamAttemptRecord, ActiveExamState, UserPreferences } from '../types';

const STORAGE_KEY = 'techexam_user_progress_v1';

const defaultPreferences: UserPreferences = {
  theme: 'dark',
  soundEnabled: true,
  keyboardShortcutsEnabled: true,
};

const defaultProgress: UserProgress = {
  attempts: [],
  incorrectQuestionIds: [],
  flaggedQuestionIds: [],
  questionHistory: {},
  preferences: defaultPreferences,
};

export const loadProgress = (): UserProgress => {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultProgress;
    const parsed = JSON.parse(raw);
    return {
      ...defaultProgress,
      ...parsed,
      preferences: {
        ...defaultPreferences,
        ...(parsed.preferences || {}),
      },
      attempts: Array.isArray(parsed.attempts) ? parsed.attempts : [],
      incorrectQuestionIds: Array.isArray(parsed.incorrectQuestionIds) ? parsed.incorrectQuestionIds : [],
      flaggedQuestionIds: Array.isArray(parsed.flaggedQuestionIds) ? parsed.flaggedQuestionIds : [],
      questionHistory: parsed.questionHistory && typeof parsed.questionHistory === 'object' ? parsed.questionHistory : {},
    };
  } catch (err) {
    console.error('Failed to load user progress from localStorage:', err);
    return defaultProgress;
  }
};

export const saveProgress = (progress: UserProgress): void => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (err) {
    console.error('Failed to save user progress to localStorage:', err);
  }
};

export const recordExamAttempt = (record: ExamAttemptRecord): UserProgress => {
  const current = loadProgress();

  // Update question history and incorrect questions list
  const incorrectSet = new Set(current.incorrectQuestionIds);
  const updatedHistory = { ...current.questionHistory };

  for (const q of record.questionsSnapshot) {
    const isCorrect = q.userSelectedAnswer === q.correctAnswer;
    const prev = updatedHistory[q.id] || { attempts: 0, correct: 0 };
    
    updatedHistory[q.id] = {
      attempts: prev.attempts + 1,
      correct: prev.correct + (isCorrect ? 1 : 0),
      lastAnswered: record.timestamp,
      lastCorrect: isCorrect,
    };

    if (isCorrect) {
      incorrectSet.delete(q.id);
    } else if (q.userSelectedAnswer) {
      incorrectSet.add(q.id);
    }
  }

  const updated: UserProgress = {
    ...current,
    attempts: [record, ...current.attempts].slice(0, 50), // keep recent 50
    incorrectQuestionIds: Array.from(incorrectSet),
    questionHistory: updatedHistory,
    activeExam: undefined, // Clear active attempt upon completion
  };

  saveProgress(updated);
  return updated;
};

export const saveActiveExamState = (state: ActiveExamState | undefined): void => {
  const current = loadProgress();
  const updated: UserProgress = {
    ...current,
    activeExam: state,
  };
  saveProgress(updated);
};

export const toggleQuestionFlag = (questionId: string): boolean => {
  const current = loadProgress();
  const set = new Set(current.flaggedQuestionIds);
  let isFlagged: boolean;
  if (set.has(questionId)) {
    set.delete(questionId);
    isFlagged = false;
  } else {
    set.add(questionId);
    isFlagged = true;
  }
  saveProgress({
    ...current,
    flaggedQuestionIds: Array.from(set),
  });
  return isFlagged;
};

export const updatePreferences = (prefs: Partial<UserPreferences>): UserPreferences => {
  const current = loadProgress();
  const updatedPrefs: UserPreferences = {
    ...current.preferences,
    ...prefs,
  };
  saveProgress({
    ...current,
    preferences: updatedPrefs,
  });
  return updatedPrefs;
};

export const clearAllProgress = (): void => {
  try {
    localStorage.removeItem(STORAGE_KEY);
  } catch (err) {
    console.error('Failed to clear progress:', err);
  }
};
