import React, { useState, useEffect } from 'react';
import questionsData from './data/questions.json';
import { 
  Question, ExamConfig, ActiveExamQuestion, ExamAttemptRecord, 
  TopicType, UserProgress, ActiveExamState, UserPreferences 
} from './types';
import { 
  loadProgress, recordExamAttempt, saveActiveExamState, 
  toggleQuestionFlag, updatePreferences, clearAllProgress 
} from './services/storage';
import { prepareExamQuestions, calculateExamResults } from './services/examEngine';
import { Navbar } from './components/Navbar';
import { Dashboard } from './components/Dashboard';
import { ExamConfigModal } from './components/ExamConfigModal';
import { ExamInterface } from './components/ExamInterface';
import { ExamResults } from './components/ExamResults';
import { QuestionExplorer } from './components/QuestionExplorer';
import { KeyboardShortcutsModal } from './components/KeyboardShortcutsModal';
import { ResetConfirmModal } from './components/ResetConfirmModal';

export const App: React.FC = () => {
  const allQuestions = questionsData as Question[];

  const [progress, setProgress] = useState<UserProgress>(loadProgress);
  const [currentView, setCurrentView] = useState<'dashboard' | 'explorer' | 'incorrect' | 'flagged' | 'exam' | 'results'>('dashboard');
  
  const [activeExam, setActiveExam] = useState<ActiveExamState | undefined>(progress.activeExam);
  const [lastAttempt, setLastAttempt] = useState<ExamAttemptRecord | undefined>(progress.attempts[0]);
  
  const [isConfigModalOpen, setIsConfigModalOpen] = useState(false);
  const [configModalInitial, setConfigModalInitial] = useState<Partial<ExamConfig>>({});
  const [isShortcutsOpen, setIsShortcutsOpen] = useState(false);
  const [isResetConfirmOpen, setIsResetConfirmOpen] = useState(false);

  // Sync theme
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', progress.preferences.theme);
  }, [progress.preferences.theme]);

  // Start exam from config
  const handleStartExam = (config: ExamConfig, specificIds?: string[]) => {
    const { questions: prepared, warning } = prepareExamQuestions(allQuestions, config, specificIds);
    if (prepared.length === 0) {
      alert(warning || 'No questions available matching criteria.');
      return;
    }

    const newExamState: ActiveExamState = {
      config,
      questions: prepared,
      currentIndex: 0,
      startTime: Date.now(),
      timeRemainingSeconds: config.timed ? config.timeLimitMinutes * 60 : 0,
      isSubmitted: false,
    };

    setActiveExam(newExamState);
    saveActiveExamState(newExamState);
    setIsConfigModalOpen(false);
    setCurrentView('exam');
  };

  // Quick launch helper from dashboard cards
  const handleQuickLaunch = (topic?: TopicType | 'All Topics', mode: 'practice' | 'exam' = 'exam') => {
    const config: ExamConfig = {
      topic: topic || 'All Topics',
      difficulty: 'mixed',
      sourceType: 'all',
      count: 20,
      mode,
      order: 'random',
      shuffleOptions: true,
      timed: mode === 'exam',
      timeLimitMinutes: 20,
      passingScore: 70,
    };
    handleStartExam(config);
  };

  // Open custom configuration modal
  const handleOpenCustomConfig = (initial?: Partial<ExamConfig>) => {
    setConfigModalInitial(initial || {});
    setIsConfigModalOpen(true);
  };

  // Update question during exam
  const handleUpdateExamQuestion = (index: number, updated: ActiveExamQuestion) => {
    if (!activeExam) return;
    const nextQuestions = [...activeExam.questions];
    nextQuestions[index] = updated;

    const nextState: ActiveExamState = {
      ...activeExam,
      questions: nextQuestions,
      currentIndex: index,
    };

    setActiveExam(nextState);
    saveActiveExamState(nextState);
  };

  // Submit exam and view results
  const handleSubmitExam = (finalQuestions: ActiveExamQuestion[], timeSpentSeconds: number) => {
    if (!activeExam) return;

    const record = calculateExamResults(finalQuestions, activeExam.config, timeSpentSeconds);
    const updatedProgress = recordExamAttempt(record);

    setProgress(updatedProgress);
    setActiveExam(undefined);
    setLastAttempt(record);
    setCurrentView('results');
  };

  // Exit exam session
  const handleExitExam = () => {
    setActiveExam(undefined);
    saveActiveExamState(undefined);
    setCurrentView('dashboard');
  };

  // Retry only incorrect questions from results
  const handleRetryIncorrect = (incorrectQuestions: ActiveExamQuestion[]) => {
    const config: ExamConfig = {
      topic: 'All Topics',
      difficulty: 'mixed',
      sourceType: 'all',
      count: incorrectQuestions.length,
      mode: 'practice',
      order: 'random',
      shuffleOptions: true,
      timed: false,
      timeLimitMinutes: 0,
      passingScore: 70,
    };
    handleStartExam(config, incorrectQuestions.map(q => q.id));
  };

  // Retake exam with identical config
  const handleRetakeSameConfig = () => {
    if (!lastAttempt) return;
    handleStartExam(lastAttempt.config);
  };

  // Drill specifically on all recorded weak spots
  const handleStartIncorrectDrill = () => {
    if (progress.incorrectQuestionIds.length === 0) {
      alert('You have no recorded weak spots! All answered questions have been answered correctly.');
      return;
    }
    const config: ExamConfig = {
      topic: 'All Topics',
      difficulty: 'mixed',
      sourceType: 'all',
      count: progress.incorrectQuestionIds.length,
      mode: 'practice',
      order: 'random',
      shuffleOptions: true,
      timed: false,
      timeLimitMinutes: 0,
      passingScore: 70,
    };
    handleStartExam(config, progress.incorrectQuestionIds);
  };

  // Drill on flagged questions
  const handleStartFlaggedDrill = () => {
    if (progress.flaggedQuestionIds.length === 0) {
      alert('You have no flagged questions. Bookmark questions during practice or in the explorer to review them here.');
      return;
    }
    const config: ExamConfig = {
      topic: 'All Topics',
      difficulty: 'mixed',
      sourceType: 'all',
      count: progress.flaggedQuestionIds.length,
      mode: 'practice',
      order: 'random',
      shuffleOptions: true,
      timed: false,
      timeLimitMinutes: 0,
      passingScore: 70,
    };
    handleStartExam(config, progress.flaggedQuestionIds);
  };

  // Practice a single question from explorer
  const handlePracticeSingleQuestion = (q: Question) => {
    const config: ExamConfig = {
      topic: q.topic,
      difficulty: q.difficulty,
      sourceType: q.sourceType,
      count: 1,
      mode: 'practice',
      order: 'sequential',
      shuffleOptions: false,
      timed: false,
      timeLimitMinutes: 0,
      passingScore: 70,
    };
    handleStartExam(config, [q.id]);
  };

  // Toggle flag on question
  const handleToggleFlag = (id: string) => {
    toggleQuestionFlag(id);
    setProgress(loadProgress());
  };

  // Reset all user progress
  const handleConfirmReset = () => {
    clearAllProgress();
    setProgress(loadProgress());
    setActiveExam(undefined);
    setLastAttempt(undefined);
    setIsResetConfirmOpen(false);
    setCurrentView('dashboard');
  };

  const handleUpdatePrefs = (newPrefs: Partial<UserPreferences>) => {
    const updated = updatePreferences(newPrefs);
    setProgress(prev => ({ ...prev, preferences: updated }));
  };

  return (
    <div className="app-container">
      <Navbar
        currentView={currentView === 'exam' || currentView === 'results' ? 'dashboard' : currentView}
        onNavigate={view => {
          if (activeExam) {
            if (confirm('An exam is currently in progress. Exit and discard current session?')) {
              handleExitExam();
              setCurrentView(view);
            }
          } else {
            setCurrentView(view);
          }
        }}
        preferences={progress.preferences}
        onUpdatePreferences={handleUpdatePrefs}
        incorrectCount={progress.incorrectQuestionIds.length}
        flaggedCount={progress.flaggedQuestionIds.length}
        onOpenShortcuts={() => setIsShortcutsOpen(true)}
        onResetProgress={() => setIsResetConfirmOpen(true)}
        isExamActive={currentView === 'exam'}
      />

      <main className="main-content">
        {currentView === 'dashboard' && (
          <Dashboard
            questions={allQuestions}
            attempts={progress.attempts}
            incorrectCount={progress.incorrectQuestionIds.length}
            flaggedCount={progress.flaggedQuestionIds.length}
            onStartExam={handleQuickLaunch}
            onOpenCustomConfig={handleOpenCustomConfig}
            onStartIncorrectDrill={handleStartIncorrectDrill}
            onStartFlaggedDrill={handleStartFlaggedDrill}
            onNavigateExplorer={() => setCurrentView('explorer')}
            onViewAttempt={att => {
              setLastAttempt(att);
              setCurrentView('results');
            }}
          />
        )}

        {currentView === 'explorer' && (
          <QuestionExplorer
            questions={allQuestions}
            flaggedQuestionIds={progress.flaggedQuestionIds}
            onToggleFlag={handleToggleFlag}
            onPracticeSingleQuestion={handlePracticeSingleQuestion}
          />
        )}

        {currentView === 'incorrect' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div className="card" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
              <div>
                <h1 style={{ fontSize: '1.75rem' }}>Weak Spots (Missed Questions)</h1>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                  Targeted practice bank containing {progress.incorrectQuestionIds.length} questions previously answered incorrectly.
                </p>
              </div>

              {progress.incorrectQuestionIds.length > 0 && (
                <button className="btn btn-primary btn-lg" onClick={handleStartIncorrectDrill}>
                  Start Weak Spots Practice Drill
                </button>
              )}
            </div>

            <QuestionExplorer
              questions={allQuestions.filter(q => progress.incorrectQuestionIds.includes(q.id))}
              flaggedQuestionIds={progress.flaggedQuestionIds}
              onToggleFlag={handleToggleFlag}
              onPracticeSingleQuestion={handlePracticeSingleQuestion}
            />
          </div>
        )}

        {currentView === 'flagged' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div className="card" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
              <div>
                <h1 style={{ fontSize: '1.75rem' }}>Flagged Questions for Review</h1>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                  {progress.flaggedQuestionIds.length} bookmarked items saved for focused revision.
                </p>
              </div>

              {progress.flaggedQuestionIds.length > 0 && (
                <button className="btn btn-primary btn-lg" onClick={handleStartFlaggedDrill}>
                  Start Flagged Questions Drill
                </button>
              )}
            </div>

            <QuestionExplorer
              questions={allQuestions.filter(q => progress.flaggedQuestionIds.includes(q.id))}
              flaggedQuestionIds={progress.flaggedQuestionIds}
              onToggleFlag={handleToggleFlag}
              onPracticeSingleQuestion={handlePracticeSingleQuestion}
            />
          </div>
        )}

        {currentView === 'exam' && activeExam && (
          <ExamInterface
            config={activeExam.config}
            questions={activeExam.questions}
            initialIndex={activeExam.currentIndex}
            initialTimeRemaining={activeExam.timeRemainingSeconds}
            onUpdateQuestion={handleUpdateExamQuestion}
            onSubmitExam={handleSubmitExam}
            onExitExam={handleExitExam}
            onOpenShortcuts={() => setIsShortcutsOpen(true)}
          />
        )}

        {currentView === 'results' && lastAttempt && (
          <ExamResults
            attempt={lastAttempt}
            onRetryIncorrect={handleRetryIncorrect}
            onRetakeSameConfig={handleRetakeSameConfig}
            onBackToDashboard={() => setCurrentView('dashboard')}
            onNavigateExplorer={() => setCurrentView('explorer')}
          />
        )}
      </main>

      {/* Global Modals */}
      <ExamConfigModal
        allQuestions={allQuestions}
        initialConfig={configModalInitial}
        isOpen={isConfigModalOpen}
        onClose={() => setIsConfigModalOpen(false)}
        onStartExam={handleStartExam}
      />

      <KeyboardShortcutsModal
        isOpen={isShortcutsOpen}
        onClose={() => setIsShortcutsOpen(false)}
      />

      <ResetConfirmModal
        isOpen={isResetConfirmOpen}
        onClose={() => setIsResetConfirmOpen(false)}
        onConfirm={handleConfirmReset}
      />
    </div>
  );
};
