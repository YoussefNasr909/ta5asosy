import test from 'node:test';
import assert from 'node:assert/strict';

// Test implementation of the pure engine logic
function shuffleQuestionOptions(question) {
  const correctOption = question.options.find(o => o.id === question.correctAnswer);
  if (!correctOption) return question;

  const correctText = correctOption.text;
  const texts = question.options.map(o => o.text);
  
  // Shuffle texts
  for (let i = texts.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [texts[i], texts[j]] = [texts[j], texts[i]];
  }

  const optionLetters = ['A', 'B', 'C', 'D'];
  const newOptions = optionLetters.map((letter, idx) => ({
    id: letter,
    text: texts[idx],
  }));

  const newCorrectOption = newOptions.find(o => o.text === correctText);
  const newCorrectAnswer = newCorrectOption ? newCorrectOption.id : question.correctAnswer;

  return {
    ...question,
    options: newOptions,
    correctAnswer: newCorrectAnswer,
  };
}

function calculateExamResults(questions, config, durationSeconds) {
  let correctCount = 0;
  let incorrectCount = 0;
  let unansweredCount = 0;

  const topicStats = {};
  const difficultyStats = {};

  for (const q of questions) {
    if (!topicStats[q.topic]) topicStats[q.topic] = { total: 0, correct: 0 };
    topicStats[q.topic].total += 1;

    if (!difficultyStats[q.difficulty]) difficultyStats[q.difficulty] = { total: 0, correct: 0 };
    difficultyStats[q.difficulty].total += 1;

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
    totalQuestions: total,
    correctCount,
    incorrectCount,
    unansweredCount,
    scorePercentage,
    passed,
    durationSeconds,
    topicStats,
    difficultyStats,
  };
}

function formatTime(seconds) {
  if (seconds < 0) seconds = 0;
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  if (hrs > 0) {
    return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

test('Option shuffling preserves correct answer mapping 100% of the time', () => {
  const original = {
    id: 'net-01',
    topic: 'Computer Networking',
    question: 'What does LAN stand for?',
    options: [
      { id: 'A', text: 'Local Access Network' },
      { id: 'B', text: 'Local Area Network' },
      { id: 'C', text: 'Large Area Network' },
      { id: 'D', text: 'Linked Access Node' },
    ],
    correctAnswer: 'B',
  };

  // Run 100 trials to verify that the text designated as correct answer matches the new correctAnswer ID
  for (let i = 0; i < 100; i++) {
    const shuffled = shuffleQuestionOptions(original);
    assert.strictEqual(shuffled.options.length, 4);
    assert.deepStrictEqual(shuffled.options.map(o => o.id), ['A', 'B', 'C', 'D']);
    
    // The option matching the new correctAnswer must be 'Local Area Network'
    const chosenOption = shuffled.options.find(o => o.id === shuffled.correctAnswer);
    assert.ok(chosenOption, 'Chosen option must exist');
    assert.strictEqual(chosenOption.text, 'Local Area Network', 'Correct text must align with updated letter');
  }
});

test('calculateExamResults handles perfect score, passing threshold and topic breakdown', () => {
  const questions = [
    { id: '1', topic: 'SQL', difficulty: 'easy', correctAnswer: 'B', userSelectedAnswer: 'B' },
    { id: '2', topic: 'SQL', difficulty: 'hard', correctAnswer: 'A', userSelectedAnswer: 'A' },
    { id: '3', topic: 'Computer Networking', difficulty: 'medium', correctAnswer: 'C', userSelectedAnswer: 'C' },
    { id: '4', topic: 'Database Fundamentals', difficulty: 'easy', correctAnswer: 'D', userSelectedAnswer: 'D' },
  ];

  const results = calculateExamResults(questions, { passingScore: 75 }, 120);
  assert.strictEqual(results.totalQuestions, 4);
  assert.strictEqual(results.correctCount, 4);
  assert.strictEqual(results.incorrectCount, 0);
  assert.strictEqual(results.unansweredCount, 0);
  assert.strictEqual(results.scorePercentage, 100);
  assert.strictEqual(results.passed, true);
  assert.strictEqual(results.topicStats['SQL'].correct, 2);
  assert.strictEqual(results.topicStats['SQL'].total, 2);
});

test('calculateExamResults accurately records incorrect and unanswered questions', () => {
  const questions = [
    { id: '1', topic: 'SQL', difficulty: 'easy', correctAnswer: 'A', userSelectedAnswer: 'B' }, // incorrect
    { id: '2', topic: 'SQL', difficulty: 'medium', correctAnswer: 'C', userSelectedAnswer: undefined }, // unanswered
    { id: '3', topic: 'Computer Networking', difficulty: 'hard', correctAnswer: 'D', userSelectedAnswer: 'D' }, // correct
    { id: '4', topic: 'Database Fundamentals', difficulty: 'easy', correctAnswer: 'A', userSelectedAnswer: undefined }, // unanswered
  ];

  const results = calculateExamResults(questions, { passingScore: 70 }, 65);
  assert.strictEqual(results.totalQuestions, 4);
  assert.strictEqual(results.correctCount, 1);
  assert.strictEqual(results.incorrectCount, 1);
  assert.strictEqual(results.unansweredCount, 2);
  assert.strictEqual(results.scorePercentage, 25);
  assert.strictEqual(results.passed, false);
});

test('formatTime formats seconds properly across thresholds', () => {
  assert.strictEqual(formatTime(0), '00:00');
  assert.strictEqual(formatTime(59), '00:59');
  assert.strictEqual(formatTime(60), '01:00');
  assert.strictEqual(formatTime(125), '02:05');
  assert.strictEqual(formatTime(3600), '01:00:00');
  assert.strictEqual(formatTime(3665), '01:01:05');
});
