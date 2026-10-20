import { Question, ActiveExamQuestion, ExamConfig, ExamAttemptRecord, OptionId, QuestionOption } from '../types';

/**
 * Fisher-Yates array shuffle algorithm
 */
export function shuffleArray<T>(array: T[]): T[] {
  const result = [...array];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

/**
 * Shuffles options of a question while preserving correct answer mapping.
 * Option IDs remain strictly 'A', 'B', 'C', 'D' in order.
 */
export function shuffleQuestionOptions(question: Question): Question {
  // Find the text of the current correct answer
  const correctOption = question.options.find(o => o.id === question.correctAnswer);
  if (!correctOption) return question;

  const correctText = correctOption.text;

  // Shuffle the texts
  const shuffledTexts = shuffleArray(question.options.map(o => o.text));

  // Reassign to stable IDs A, B, C, D
  const optionLetters: OptionId[] = ['A', 'B', 'C', 'D'];
  const newOptions: QuestionOption[] = optionLetters.map((letter, idx) => ({
    id: letter,
    text: shuffledTexts[idx],
  }));

  // Identify new correct letter
  const newCorrectOption = newOptions.find(o => o.text === correctText);
  const newCorrectAnswer: OptionId = newCorrectOption ? newCorrectOption.id : question.correctAnswer;

  return {
    ...question,
    options: newOptions,
    correctAnswer: newCorrectAnswer,
  };
}

/**
 * Filters and prepares questions for an exam session
 */
export function prepareExamQuestions(
  allQuestions: Question[],
  config: ExamConfig,
  specificQuestionIds?: string[]
): { questions: ActiveExamQuestion[]; warning?: string } {
  let pool = [...allQuestions];

  // Specific question IDs (for incorrect or flagged drills)
  if (specificQuestionIds && specificQuestionIds.length > 0) {
    const idSet = new Set(specificQuestionIds);
    pool = pool.filter(q => idSet.has(q.id));
  }

  // Filter by topic
  if (config.topic !== 'All Topics') {
    pool = pool.filter(q => q.topic === config.topic);
  }

  // Filter by subtopic
  if (config.subtopic && config.subtopic !== 'All Subtopics') {
    pool = pool.filter(q => q.subtopic === config.subtopic);
  }

  // Filter by difficulty
  if (config.difficulty !== 'mixed') {
    pool = pool.filter(q => q.difficulty === config.difficulty);
  }

  // Filter by source
  if (config.sourceType !== 'all') {
    pool = pool.filter(q => q.sourceType === config.sourceType);
  }

  let warning: string | undefined;
  if (pool.length === 0) {
    return {
      questions: [],
      warning: 'No questions match the selected filters. Please adjust your criteria.',
    };
  }

  if (pool.length < config.count) {
    warning = `Only ${pool.length} questions are available matching your criteria (requested: ${config.count}).`;
  }

  // Order
  if (config.order === 'random') {
    pool = shuffleArray(pool);
  }

  // Slice count
  const selected = pool.slice(0, Math.min(config.count, pool.length));

  // Shuffle options if requested
  const finalQuestions: ActiveExamQuestion[] = selected.map(q => {
    const processed = config.shuffleOptions ? shuffleQuestionOptions(q) : q;
    return {
      ...processed,
      userSelectedAnswer: undefined,
      isFlagged: false,
      isRevealed: false,
    };
  });

  return { questions: finalQuestions, warning };
}

/**
 * Calculates exam results and statistics
 */
export function calculateExamResults(
  questions: ActiveExamQuestion[],
  config: ExamConfig,
  durationSeconds: number
): ExamAttemptRecord {
  let correctCount = 0;
  let incorrectCount = 0;
  let unansweredCount = 0;

  const topicStats: Record<string, { total: number; correct: number }> = {};
  const difficultyStats: Record<string, { total: number; correct: number }> = {};

  for (const q of questions) {
    // Topic stats init
    if (!topicStats[q.topic]) {
      topicStats[q.topic] = { total: 0, correct: 0 };
    }
    topicStats[q.topic].total += 1;

    // Difficulty stats init
    if (!difficultyStats[q.difficulty]) {
      difficultyStats[q.difficulty] = { total: 0, correct: 0 };
    }
    difficultyStats[q.difficulty].total += 1;

    // Scoring
    if (!q.userSelectedAnswer) {
      unansweredCount++;
    } else if (q.userSelectedAnswer === q.correctAnswer) {
      correctCount++;
      topicStats[q.topic].correct += 1;
      difficultyStats[q.difficulty].correct += 1;
    } else {
      incorrectCount++;
    }
  }

  const total = questions.length;
  const scorePercentage = total > 0 ? Math.round((correctCount / total) * 100) : 0;
  const passed = scorePercentage >= (config.passingScore || 70);

  return {
    id: `attempt-${Date.now()}-${Math.random().toString(36).substring(2, 7)}`,
    timestamp: new Date().toISOString(),
    config,
    totalQuestions: total,
    correctCount,
    incorrectCount,
    unansweredCount,
    scorePercentage,
    passed,
    durationSeconds,
    topicStats,
    difficultyStats,
    questionsSnapshot: questions,
  };
}

/**
 * Format seconds into mm:ss or hh:mm:ss
 */
export function formatTime(seconds: number): string {
  if (seconds < 0) seconds = 0;
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  if (hrs > 0) {
    return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}
