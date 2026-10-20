import React, { useState, useEffect, useRef, useCallback } from 'react';
import { 
  Clock, Bookmark, ChevronLeft, ChevronRight, CheckCircle2, 
  XCircle, AlertTriangle, HelpCircle, RotateCcw, Send, FileText, Sparkles 
} from 'lucide-react';
import { ActiveExamQuestion, ExamConfig, OptionId } from '../types';
import { formatTime } from '../services/examEngine';

interface ExamInterfaceProps {
  config: ExamConfig;
  questions: ActiveExamQuestion[];
  initialIndex?: number;
  initialTimeRemaining?: number;
  onUpdateQuestion: (index: number, updated: ActiveExamQuestion) => void;
  onSubmitExam: (finalQuestions: ActiveExamQuestion[], timeSpentSeconds: number) => void;
  onExitExam: () => void;
  onOpenShortcuts: () => void;
}

export const ExamInterface: React.FC<ExamInterfaceProps> = ({
  config,
  questions,
  initialIndex = 0,
  initialTimeRemaining,
  onUpdateQuestion,
  onSubmitExam,
  onExitExam,
  onOpenShortcuts,
}) => {
  const [currentIndex, setCurrentIndex] = useState<number>(initialIndex);
  const [showConfirmModal, setShowConfirmModal] = useState<boolean>(false);
  const [showExitConfirm, setShowExitConfirm] = useState<boolean>(false);

  // Timer setup
  const totalDurationSeconds = config.timed ? config.timeLimitMinutes * 60 : 0;
  const [secondsRemaining, setSecondsRemaining] = useState<number>(
    initialTimeRemaining !== undefined ? initialTimeRemaining : totalDurationSeconds
  );

  const isSubmittingRef = useRef<boolean>(false);
  const startTimeRef = useRef<number>(Date.now());

  const currentQ = questions[currentIndex];

  // Helper to test if string contains Arabic characters
  const isArabicText = (text: string): boolean => {
    return /[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]/.test(text);
  };

  // Safe idempotent submission handler
  const handleFinalSubmit = useCallback(() => {
    if (isSubmittingRef.current) return;
    isSubmittingRef.current = true;
    setShowConfirmModal(false);

    const elapsedSeconds = config.timed 
      ? Math.max(1, totalDurationSeconds - secondsRemaining)
      : Math.max(1, Math.floor((Date.now() - startTimeRef.current) / 1000));

    onSubmitExam(questions, elapsedSeconds);
  }, [config.timed, totalDurationSeconds, secondsRemaining, questions, onSubmitExam]);

  // Timer interval
  useEffect(() => {
    if (!config.timed) return;

    const timer = setInterval(() => {
      setSecondsRemaining(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          handleFinalSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [config.timed, handleFinalSubmit]);

  // Handle option select — instant feedback on selection
  const handleSelectOption = (optionId: OptionId) => {
    // If already revealed (answered), prevent change until retry
    if (currentQ.isRevealed) {
      return;
    }

    const updated: ActiveExamQuestion = {
      ...currentQ,
      userSelectedAnswer: optionId,
      isRevealed: true, // Instantly reveal correct/incorrect feedback
    };
    onUpdateQuestion(currentIndex, updated);
  };

  // Toggle flag
  const handleToggleFlag = () => {
    const updated: ActiveExamQuestion = {
      ...currentQ,
      isFlagged: !currentQ.isFlagged,
    };
    onUpdateQuestion(currentIndex, updated);
  };

  // Practice mode: check answer
  const handleCheckAnswer = () => {
    if (!currentQ.userSelectedAnswer) return;
    const updated: ActiveExamQuestion = {
      ...currentQ,
      isRevealed: true,
    };
    onUpdateQuestion(currentIndex, updated);
  };

  // Practice mode: retry question
  const handleRetryQuestion = () => {
    const updated: ActiveExamQuestion = {
      ...currentQ,
      userSelectedAnswer: undefined,
      isRevealed: false,
    };
    onUpdateQuestion(currentIndex, updated);
  };

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't trigger if user is in an input
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes((e.target as HTMLElement).tagName)) {
        return;
      }

      if (e.key === 'ArrowLeft' || e.key === 'p' || e.key === 'P') {
        if (currentIndex > 0) setCurrentIndex(prev => prev - 1);
      } else if (e.key === 'ArrowRight' || e.key === 'n' || e.key === 'N') {
        if (currentIndex < questions.length - 1) setCurrentIndex(prev => prev + 1);
      } else if (e.key === '1' || e.key === 'a' || e.key === 'A') {
        handleSelectOption('A');
      } else if (e.key === '2' || e.key === 'b' || e.key === 'B') {
        handleSelectOption('B');
      } else if (e.key === '3' || e.key === 'c' || e.key === 'C') {
        handleSelectOption('C');
      } else if (e.key === '4' || e.key === 'd' || e.key === 'D') {
        handleSelectOption('D');
      } else if (e.key === 'f' || e.key === 'F') {
        handleToggleFlag();
      } else if (e.key === '?') {
        onOpenShortcuts();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentIndex, questions.length, currentQ, config.mode]);

  const answeredCount = questions.filter(q => q.userSelectedAnswer !== undefined).length;
  const unansweredCount = questions.length - answeredCount;
  const flaggedCount = questions.filter(q => q.isFlagged).length;
  const progressPercent = Math.round(((currentIndex + 1) / questions.length) * 100);

  const isLowTime = config.timed && secondsRemaining < 120;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
      {/* Top Status Header */}
      <div 
        className="card" 
        style={{ 
          padding: '0.85rem 1.25rem', 
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '1rem',
          position: 'sticky',
          top: '4.5rem',
          zIndex: 40,
          backdropFilter: 'blur(12px)',
          background: 'var(--bg-surface-glass)'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <button 
            className="btn btn-ghost btn-sm" 
            onClick={() => setShowExitConfirm(true)}
            title="Exit Exam Session"
          >
            <ChevronLeft size={18} /> Exit
          </button>

          <div>
            <span style={{ fontWeight: 800, fontSize: '1.05rem', color: 'var(--text-primary)' }}>
              Question {currentIndex + 1}
            </span>
            <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}> of {questions.length}</span>
          </div>

          <span className={`badge ${
            currentQ.topic === 'Computer Networking' ? 'badge-topic-net' :
            currentQ.topic === 'SQL' ? 'badge-topic-sql' : 'badge-topic-db'
          }`}>
            {currentQ.topic}
          </span>
        </div>

        {/* Center: Timer if applicable */}
        {config.timed && (
          <div 
            style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '0.5rem',
              fontWeight: 700,
              fontSize: '1.1rem',
              color: isLowTime ? 'var(--status-danger)' : 'var(--text-primary)',
              padding: '0.3rem 0.85rem',
              borderRadius: '8px',
              background: isLowTime ? 'var(--status-danger-light)' : 'var(--bg-secondary)',
            }}
            className={isLowTime ? 'animate-pulse' : ''}
          >
            <Clock size={18} />
            <span>{formatTime(secondsRemaining)}</span>
          </div>
        )}

        {/* Right side controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <button
            className={`btn btn-sm ${currentQ.isFlagged ? 'btn-secondary' : 'btn-ghost'}`}
            onClick={handleToggleFlag}
            style={{ color: currentQ.isFlagged ? 'var(--status-warning)' : 'inherit' }}
            title="Flag question for review (F)"
          >
            <Bookmark size={16} fill={currentQ.isFlagged ? 'currentColor' : 'none'} />
            <span>{currentQ.isFlagged ? 'Flagged' : 'Flag'}</span>
          </button>

          <button
            className="btn btn-primary btn-sm"
            onClick={() => setShowConfirmModal(true)}
          >
            <Send size={15} />
            <span>Submit Exam</span>
          </button>
        </div>
      </div>

      {/* Progress Bar */}
      <div style={{ width: '100%', height: '5px', background: 'var(--border-subtle)', borderRadius: '999px', overflow: 'hidden' }}>
        <div 
          style={{ 
            width: `${progressPercent}%`, 
            height: '100%', 
            background: 'linear-gradient(90deg, var(--accent-primary), var(--accent-purple))',
            transition: 'width 0.25s ease' 
          }} 
        />
      </div>

      {/* Main Two-Column Layout */}
      <div className="exam-layout">
        {/* Left Column: Active Question */}
        <div className="question-card">
          {/* Question Meta Header */}
          <div className="question-header">
            <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center', flexWrap: 'wrap' }}>
              <span className={`badge badge-${currentQ.difficulty}`}>
                {currentQ.difficulty.toUpperCase()}
              </span>

              <span className="badge" style={{ background: 'var(--bg-secondary)', color: 'var(--text-secondary)' }}>
                {currentQ.subtopic}
              </span>

              {currentQ.sourceType === 'pdf' ? (
                <span className="badge badge-pdf" title={`Source: ${currentQ.sourceFile}`}>
                  <FileText size={12} /> Original PDF
                </span>
              ) : (
                <span className="badge badge-gen">
                  <Sparkles size={12} /> AI-Generated Practice
                </span>
              )}
            </div>

            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              ID: {currentQ.id}
            </span>
          </div>

          {/* Question Text */}
          <div 
            className={`question-text ${isArabicText(currentQ.question) ? 'arabic-text' : ''}`}
            dir={isArabicText(currentQ.question) ? 'rtl' : 'ltr'}
          >
            {currentQ.question}
          </div>

          {/* Options List */}
          <div className="options-list">
            {currentQ.options.map(option => {
              const isSelected = currentQ.userSelectedAnswer === option.id;
              const isRevealed = currentQ.isRevealed === true;
              const isCorrectAnswer = option.id === currentQ.correctAnswer;
              const isUserWrongChoice = isSelected && !isCorrectAnswer;

              let btnClass = 'option-button';
              if (isRevealed) {
                if (isCorrectAnswer) btnClass += ' correct';
                else if (isUserWrongChoice) btnClass += ' incorrect';
              } else if (isSelected) {
                btnClass += ' selected';
              }

              return (
                <button
                  key={option.id}
                  className={btnClass}
                  onClick={() => handleSelectOption(option.id)}
                  disabled={isRevealed}
                >
                  <span className="option-key">{option.id}</span>
                  <span 
                    className={`option-text ${isArabicText(option.text) ? 'arabic-text' : ''}`}
                    dir={isArabicText(option.text) ? 'rtl' : 'ltr'}
                  >
                    {option.text}
                  </span>

                  {isRevealed && isCorrectAnswer && (
                    <CheckCircle2 size={20} color="var(--status-success)" style={{ marginLeft: 'auto' }} />
                  )}
                  {isRevealed && isUserWrongChoice && (
                    <XCircle size={20} color="var(--status-danger)" style={{ marginLeft: 'auto' }} />
                  )}
                </button>
              );
            })}
          </div>

          {/* Instant Answer Feedback Box — shown in ALL modes */}
          {currentQ.isRevealed && (
            <div 
              style={{ 
                marginTop: '1rem', 
                padding: '1.25rem', 
                borderRadius: '14px', 
                background: currentQ.userSelectedAnswer === currentQ.correctAnswer 
                  ? 'var(--status-success-light)' 
                  : 'var(--status-danger-light)',
                border: `1px solid ${currentQ.userSelectedAnswer === currentQ.correctAnswer 
                  ? 'var(--status-success-border)' 
                  : 'var(--status-danger-border)'}`,
                animation: 'fadeSlideIn 0.3s ease-out',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontWeight: 700 }}>
                  {currentQ.userSelectedAnswer === currentQ.correctAnswer ? (
                    <>
                      <CheckCircle2 size={18} color="var(--status-success)" />
                      <span style={{ color: 'var(--status-success)' }}>Correct!</span>
                    </>
                  ) : (
                    <>
                      <XCircle size={18} color="var(--status-danger)" />
                      <span style={{ color: 'var(--status-danger)' }}>
                        Incorrect! The correct answer is: {currentQ.correctAnswer}
                      </span>
                    </>
                  )}
                </div>

                <button className="btn btn-ghost btn-sm" onClick={handleRetryQuestion}>
                  <RotateCcw size={14} /> Retry
                </button>
              </div>

              <p style={{ fontSize: '0.9rem', lineHeight: 1.6, color: 'var(--text-primary)' }}>
                <strong>Explanation:</strong> {currentQ.explanation}
              </p>
            </div>
          )}

          {/* Previous / Next Navigation Row */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1rem', borderTop: '1px solid var(--border-subtle)', paddingTop: '1.25rem' }}>
            <button
              className="btn btn-secondary"
              disabled={currentIndex === 0}
              onClick={() => setCurrentIndex(prev => prev - 1)}
            >
              <ChevronLeft size={16} /> Previous
            </button>

            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
              Shortcut: 1-4 or A-D to select, Left/Right arrows to navigate
            </span>

            {currentIndex < questions.length - 1 ? (
              <button
                className="btn btn-primary"
                onClick={() => setCurrentIndex(prev => prev + 1)}
              >
                Next <ChevronRight size={16} />
              </button>
            ) : (
              <button
                className="btn btn-success"
                onClick={() => setShowConfirmModal(true)}
              >
                Finish & Submit <Send size={15} />
              </button>
            )}
          </div>
        </div>

        {/* Right Column: Question Navigator Grid */}
        <div className="navigator-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
            <h3 style={{ fontSize: '1rem' }}>Question Navigator</h3>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              {answeredCount}/{questions.length} Answered
            </span>
          </div>

          <div className="nav-grid">
            {questions.map((q, idx) => {
              const isAnswered = q.userSelectedAnswer !== undefined;
              const isCurrent = idx === currentIndex;
              const isFlagged = q.isFlagged;

              let cellClass = 'grid-cell';
              if (isAnswered) cellClass += ' answered';
              if (isCurrent) cellClass += ' current';
              if (isFlagged) cellClass += ' flagged';

              return (
                <button
                  key={q.id}
                  className={cellClass}
                  onClick={() => setCurrentIndex(idx)}
                  title={`Question ${idx + 1} (${isAnswered ? 'Answered: ' + q.userSelectedAnswer : 'Unanswered'})`}
                >
                  {idx + 1}
                </button>
              );
            })}
          </div>

          {/* Navigator Legend */}
          <div style={{ marginTop: '1.25rem', borderTop: '1px solid var(--border-subtle)', paddingTop: '0.75rem', display: 'flex', flexDirection: 'column', gap: '0.4rem', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <div style={{ width: '12px', height: '12px', borderRadius: '3px', background: 'var(--accent-primary-light)', border: '1px solid var(--accent-primary)' }} />
              <span>Answered ({answeredCount})</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <div style={{ width: '12px', height: '12px', borderRadius: '3px', background: 'var(--bg-surface)', border: '1px solid var(--border-subtle)' }} />
              <span>Unanswered ({unansweredCount})</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--status-warning)' }} />
              <span>Flagged for Review ({flaggedCount})</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <div style={{ width: '12px', height: '12px', borderRadius: '3px', border: '2px solid var(--accent-purple)' }} />
              <span>Current Question</span>
            </div>
          </div>
        </div>
      </div>

      {/* Submit Confirmation Modal */}
      {showConfirmModal && (
        <div className="modal-backdrop" onClick={() => setShowConfirmModal(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1rem' }}>
              <AlertTriangle size={24} color="var(--status-warning)" />
              <h2 style={{ fontSize: '1.35rem' }}>Ready to Submit Your Exam?</h2>
            </div>

            <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem', lineHeight: 1.5 }}>
              Are you sure you want to end this attempt and view your detailed score breakdown?
            </p>

            <div style={{ background: 'var(--bg-secondary)', padding: '1rem', borderRadius: '12px', marginBottom: '1.5rem', display: 'flex', justifyContent: 'space-around', textAlign: 'center' }}>
              <div>
                <div style={{ fontWeight: 800, fontSize: '1.25rem', color: 'var(--accent-primary)' }}>{answeredCount}</div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Answered</div>
              </div>
              <div>
                <div style={{ fontWeight: 800, fontSize: '1.25rem', color: unansweredCount > 0 ? 'var(--status-danger)' : 'var(--status-success)' }}>
                  {unansweredCount}
                </div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Unanswered</div>
              </div>
              <div>
                <div style={{ fontWeight: 800, fontSize: '1.25rem', color: 'var(--status-warning)' }}>{flaggedCount}</div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Flagged</div>
              </div>
            </div>

            {unansweredCount > 0 && (
              <div style={{ padding: '0.75rem', borderRadius: '8px', background: 'var(--status-danger-light)', border: '1px solid var(--status-danger-border)', color: 'var(--status-danger)', fontSize: '0.85rem', marginBottom: '1.25rem' }}>
                Warning: You still have {unansweredCount} unanswered questions! Unanswered items will be scored as incorrect.
              </div>
            )}

            <div style={{ display: 'flex', gap: '0.75rem' }}>
              <button className="btn btn-secondary" style={{ flex: 1 }} onClick={() => setShowConfirmModal(false)}>
                Back to Questions
              </button>
              <button className="btn btn-primary" style={{ flex: 1 }} onClick={handleFinalSubmit}>
                Confirm & Submit
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Exit Exam Confirmation */}
      {showExitConfirm && (
        <div className="modal-backdrop" onClick={() => setShowExitConfirm(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2 style={{ fontSize: '1.25rem', marginBottom: '0.75rem' }}>Exit Current Exam?</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem', lineHeight: 1.5 }}>
              Your current session will be discarded and will not be recorded as a completed attempt. Are you sure you want to return to the dashboard?
            </p>
            <div style={{ display: 'flex', gap: '0.75rem' }}>
              <button className="btn btn-secondary" style={{ flex: 1 }} onClick={() => setShowExitConfirm(false)}>
                Stay in Exam
              </button>
              <button className="btn btn-danger" style={{ flex: 1 }} onClick={onExitExam}>
                Discard & Exit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
