import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { 
  CheckCircle2, XCircle, Clock, RotateCcw, AlertCircle, 
  ArrowLeft, FileText, Sparkles, Filter, ChevronDown, ChevronUp, Bookmark 
} from 'lucide-react';
import { ExamAttemptRecord, ActiveExamQuestion } from '../types';
import { formatTime } from '../services/examEngine';

interface ExamResultsProps {
  attempt: ExamAttemptRecord;
  onRetryIncorrect: (incorrectQuestions: ActiveExamQuestion[]) => void;
  onRetakeSameConfig: () => void;
  onBackToDashboard: () => void;
  onNavigateExplorer: () => void;
}

export const ExamResults: React.FC<ExamResultsProps> = ({
  attempt,
  onRetryIncorrect,
  onRetakeSameConfig,
  onBackToDashboard,
  onNavigateExplorer,
}) => {
  const [filter, setFilter] = useState<'all' | 'incorrect' | 'correct' | 'flagged'>('all');
  const [expandedIds, setExpandedIds] = useState<Set<string>>(new Set());

  // Trigger celebration confetti on pass!
  useEffect(() => {
    if (attempt.passed) {
      try {
        confetti({
          particleCount: 100,
          spread: 70,
          origin: { y: 0.6 }
        });
      } catch (e) {
        // Safe fallback if confetti isn't available
      }
    }
  }, [attempt.passed]);

  const incorrectQuestions = attempt.questionsSnapshot.filter(
    q => q.userSelectedAnswer !== q.correctAnswer
  );

  const filteredQuestions = attempt.questionsSnapshot.filter(q => {
    if (filter === 'incorrect') return q.userSelectedAnswer !== q.correctAnswer;
    if (filter === 'correct') return q.userSelectedAnswer === q.correctAnswer;
    if (filter === 'flagged') return q.isFlagged;
    return true;
  });

  const toggleExpand = (id: string) => {
    const next = new Set(expandedIds);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    setExpandedIds(next);
  };

  const expandAll = () => {
    setExpandedIds(new Set(attempt.questionsSnapshot.map(q => q.id)));
  };

  const collapseAll = () => {
    setExpandedIds(new Set());
  };

  const isArabicText = (text: string): boolean => {
    return /[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]/.test(text);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      {/* Top Banner & Scorecard */}
      <div 
        className="card" 
        style={{ 
          textAlign: 'center', 
          padding: '2.5rem 1.5rem',
          background: attempt.passed
            ? 'linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(59, 130, 246, 0.1))'
            : 'linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(245, 158, 11, 0.1))',
          borderColor: attempt.passed ? 'var(--status-success-border)' : 'var(--status-danger-border)'
        }}
      >
        <div className={`score-circle ${attempt.passed ? 'pass' : 'fail'}`}>
          <div style={{ fontSize: '3rem', fontWeight: 800, lineHeight: 1 }}>
            {attempt.scorePercentage}%
          </div>
          <div style={{ fontSize: '0.85rem', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.05em', marginTop: '0.25rem' }}>
            {attempt.passed ? 'PASSED' : 'NEEDS PRACTICE'}
          </div>
        </div>

        <h1 style={{ fontSize: '1.85rem', marginBottom: '0.5rem' }}>
          {attempt.passed ? 'Congratulations! Exam Passed' : 'Assessment Completed'}
        </h1>
        <p style={{ color: 'var(--text-secondary)', maxWidth: '540px', margin: '0 auto 1.5rem auto', fontSize: '0.95rem' }}>
          {attempt.passed 
            ? `You scored ${attempt.scorePercentage}%, successfully meeting the passing threshold of ${attempt.config.passingScore}%. Great technical mastery!`
            : `You scored ${attempt.scorePercentage}%, below the passing threshold of ${attempt.config.passingScore}%. Review your weak spots below to master the concepts.`
          }
        </p>

        {/* Action Buttons */}
        <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          {incorrectQuestions.length > 0 && (
            <button 
              className="btn btn-primary"
              onClick={() => onRetryIncorrect(incorrectQuestions)}
            >
              <RotateCcw size={16} />
              <span>Retry {incorrectQuestions.length} Incorrect Questions</span>
            </button>
          )}

          <button className="btn btn-secondary" onClick={onRetakeSameConfig}>
            <RotateCcw size={16} />
            <span>Retake Exam (Same Config)</span>
          </button>

          <button className="btn btn-secondary" onClick={onBackToDashboard}>
            <ArrowLeft size={16} />
            <span>Dashboard</span>
          </button>
        </div>
      </div>

      {/* Metrics Grid */}
      <div className="dashboard-grid">
        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'rgba(59, 130, 246, 0.15)', color: '#3b82f6' }}>
            <FileText size={24} />
          </div>
          <div>
            <div className="stat-val">{attempt.totalQuestions}</div>
            <div className="stat-label">Total Questions</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'var(--status-success-light)', color: 'var(--status-success)' }}>
            <CheckCircle2 size={24} />
          </div>
          <div>
            <div className="stat-val">{attempt.correctCount}</div>
            <div className="stat-label">Correct Answers</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'var(--status-danger-light)', color: 'var(--status-danger)' }}>
            <XCircle size={24} />
          </div>
          <div>
            <div className="stat-val">{attempt.incorrectCount}</div>
            <div className="stat-label">Incorrect Answers</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'var(--bg-secondary)', color: 'var(--text-muted)' }}>
            <Clock size={24} />
          </div>
          <div>
            <div className="stat-val">{formatTime(attempt.durationSeconds)}</div>
            <div className="stat-label">Time Spent</div>
          </div>
        </div>
      </div>

      {/* Topic & Difficulty Breakdown */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.25rem' }}>
        {/* Topic Breakdown */}
        <div className="card">
          <h2 style={{ fontSize: '1.15rem', marginBottom: '1rem' }}>Performance by Subject Topic</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {Object.entries(attempt.topicStats).map(([topicName, stats]) => {
              const pct = stats.total > 0 ? Math.round((stats.correct / stats.total) * 100) : 0;
              return (
                <div key={topicName}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '0.3rem', fontWeight: 600 }}>
                    <span>{topicName}</span>
                    <span>{stats.correct} / {stats.total} ({pct}%)</span>
                  </div>
                  <div style={{ height: '8px', background: 'var(--border-subtle)', borderRadius: '999px', overflow: 'hidden' }}>
                    <div 
                      style={{ 
                        width: `${pct}%`, 
                        height: '100%', 
                        background: pct >= 70 ? 'var(--status-success)' : pct >= 50 ? 'var(--status-warning)' : 'var(--status-danger)',
                        borderRadius: '999px' 
                      }} 
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Difficulty Breakdown */}
        <div className="card">
          <h2 style={{ fontSize: '1.15rem', marginBottom: '1rem' }}>Performance by Difficulty</h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {Object.entries(attempt.difficultyStats).map(([diffName, stats]) => {
              const pct = stats.total > 0 ? Math.round((stats.correct / stats.total) * 100) : 0;
              return (
                <div key={diffName}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '0.3rem', fontWeight: 600, textTransform: 'capitalize' }}>
                    <span>{diffName} Level</span>
                    <span>{stats.correct} / {stats.total} ({pct}%)</span>
                  </div>
                  <div style={{ height: '8px', background: 'var(--border-subtle)', borderRadius: '999px', overflow: 'hidden' }}>
                    <div 
                      style={{ 
                        width: `${pct}%`, 
                        height: '100%', 
                        background: pct >= 70 ? 'var(--status-success)' : pct >= 50 ? 'var(--status-warning)' : 'var(--status-danger)',
                        borderRadius: '999px' 
                      }} 
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Detailed Review Section */}
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '1rem' }}>
          <div>
            <h2 style={{ fontSize: '1.35rem' }}>Question-by-Question Review</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
              Inspect detailed explanations and compare your choices against correct keys
            </p>
          </div>

          <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center', flexWrap: 'wrap' }}>
            <div style={{ display: 'flex', gap: '0.25rem', background: 'var(--bg-secondary)', padding: '0.25rem', borderRadius: '10px' }}>
              <button 
                className={`btn btn-sm ${filter === 'all' ? 'btn-primary' : 'btn-ghost'}`}
                onClick={() => setFilter('all')}
              >
                All ({attempt.questionsSnapshot.length})
              </button>
              <button 
                className={`btn btn-sm ${filter === 'incorrect' ? 'btn-primary' : 'btn-ghost'}`}
                onClick={() => setFilter('incorrect')}
              >
                Incorrect ({incorrectQuestions.length})
              </button>
              <button 
                className={`btn btn-sm ${filter === 'correct' ? 'btn-primary' : 'btn-ghost'}`}
                onClick={() => setFilter('correct')}
              >
                Correct ({attempt.correctCount})
              </button>
              <button 
                className={`btn btn-sm ${filter === 'flagged' ? 'btn-primary' : 'btn-ghost'}`}
                onClick={() => setFilter('flagged')}
              >
                Flagged ({attempt.questionsSnapshot.filter(q => q.isFlagged).length})
              </button>
            </div>

            <button className="btn btn-secondary btn-sm" onClick={expandAll}>Expand All</button>
            <button className="btn btn-secondary btn-sm" onClick={collapseAll}>Collapse All</button>
          </div>
        </div>

        {/* Questions List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {filteredQuestions.map((q, idx) => {
            const isCorrect = q.userSelectedAnswer === q.correctAnswer;
            const isUnanswered = q.userSelectedAnswer === undefined;
            const isExpanded = expandedIds.has(q.id);

            return (
              <div 
                key={q.id}
                style={{
                  border: `1px solid ${isCorrect ? 'var(--status-success-border)' : isUnanswered ? 'var(--border-prominent)' : 'var(--status-danger-border)'}`,
                  borderRadius: '14px',
                  background: 'var(--bg-surface)',
                  overflow: 'hidden',
                }}
              >
                {/* Header Clickable Row */}
                <div 
                  onClick={() => toggleExpand(q.id)}
                  style={{
                    padding: '1rem 1.25rem',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    gap: '1rem',
                    background: isCorrect ? 'var(--status-success-light)' : isUnanswered ? 'var(--bg-secondary)' : 'var(--status-danger-light)',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', flex: 1 }}>
                    {isCorrect ? (
                      <CheckCircle2 size={20} color="var(--status-success)" style={{ flexShrink: 0 }} />
                    ) : isUnanswered ? (
                      <AlertCircle size={20} color="var(--text-muted)" style={{ flexShrink: 0 }} />
                    ) : (
                      <XCircle size={20} color="var(--status-danger)" style={{ flexShrink: 0 }} />
                    )}

                    <div style={{ fontWeight: 600, fontSize: '0.95rem' }}>
                      <span style={{ color: 'var(--text-muted)', marginRight: '0.5rem' }}>Q{idx + 1}.</span>
                      <span className={isArabicText(q.question) ? 'arabic-text' : ''}>{q.question}</span>
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <span className={`badge ${
                      q.topic === 'Computer Networking' ? 'badge-topic-net' :
                      q.topic === 'SQL' ? 'badge-topic-sql' : 'badge-topic-db'
                    }`}>
                      {q.topic}
                    </span>
                    {q.isFlagged && <Bookmark size={15} color="var(--status-warning)" fill="currentColor" />}
                    {isExpanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                  </div>
                </div>

                {/* Expanded Details */}
                {isExpanded && (
                  <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '1rem', borderTop: '1px solid var(--border-subtle)' }}>
                    <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                      <span className={`badge badge-${q.difficulty}`}>{q.difficulty.toUpperCase()}</span>
                      <span className="badge" style={{ background: 'var(--bg-secondary)', color: 'var(--text-secondary)' }}>{q.subtopic}</span>
                      {q.sourceType === 'pdf' ? (
                        <span className="badge badge-pdf"><FileText size={12} /> {q.sourceFile}</span>
                      ) : (
                        <span className="badge badge-gen"><Sparkles size={12} /> AI-Generated</span>
                      )}
                    </div>

                    {/* Options Breakdown */}
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                      {q.options.map(opt => {
                        const isThisCorrect = opt.id === q.correctAnswer;
                        const isThisUserSelected = opt.id === q.userSelectedAnswer;

                        let optBg = 'var(--bg-surface)';
                        let optBorder = 'var(--border-subtle)';
                        if (isThisCorrect) {
                          optBg = 'var(--status-success-light)';
                          optBorder = 'var(--status-success)';
                        } else if (isThisUserSelected) {
                          optBg = 'var(--status-danger-light)';
                          optBorder = 'var(--status-danger)';
                        }

                        return (
                          <div 
                            key={opt.id}
                            style={{
                              display: 'flex',
                              alignItems: 'center',
                              gap: '0.75rem',
                              padding: '0.65rem 1rem',
                              borderRadius: '8px',
                              background: optBg,
                              border: `1px solid ${optBorder}`,
                              fontSize: '0.9rem',
                            }}
                          >
                            <span style={{ fontWeight: 700, width: '22px' }}>{opt.id})</span>
                            <span 
                              style={{ flex: 1 }}
                              className={isArabicText(opt.text) ? 'arabic-text' : ''}
                              dir={isArabicText(opt.text) ? 'rtl' : 'ltr'}
                            >
                              {opt.text}
                            </span>
                            {isThisCorrect && (
                              <span className="badge badge-easy">Correct Answer</span>
                            )}
                            {isThisUserSelected && !isThisCorrect && (
                              <span className="badge badge-hard">Your Choice</span>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {/* Explanation */}
                    <div style={{ background: 'var(--bg-secondary)', padding: '1rem', borderRadius: '10px', fontSize: '0.9rem', lineHeight: 1.6 }}>
                      <strong style={{ color: 'var(--accent-primary)' }}>Explanation: </strong>
                      {q.explanation}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
