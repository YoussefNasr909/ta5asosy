import React from 'react';
import { Layers, BookOpen, AlertCircle, Bookmark, Sun, Moon, RotateCcw, HelpCircle } from 'lucide-react';
import { UserPreferences } from '../types';

interface NavbarProps {
  currentView: 'dashboard' | 'explorer' | 'incorrect' | 'flagged';
  onNavigate: (view: 'dashboard' | 'explorer' | 'incorrect' | 'flagged') => void;
  preferences: UserPreferences;
  onUpdatePreferences: (prefs: Partial<UserPreferences>) => void;
  incorrectCount: number;
  flaggedCount: number;
  onOpenShortcuts: () => void;
  onResetProgress: () => void;
  isExamActive: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentView,
  onNavigate,
  preferences,
  onUpdatePreferences,
  incorrectCount,
  flaggedCount,
  onOpenShortcuts,
  onResetProgress,
  isExamActive,
}) => {
  const toggleTheme = () => {
    const nextTheme = preferences.theme === 'dark' ? 'light' : 'dark';
    onUpdatePreferences({ theme: nextTheme });
    document.documentElement.setAttribute('data-theme', nextTheme);
  };

  return (
    <header className="navbar">
      <div className="navbar-inner">
        <div className="brand-badge" onClick={() => !isExamActive && onNavigate('dashboard')}>
          <div className="brand-icon">
            <Layers size={22} />
          </div>
          <div>
            <div className="brand-title">TechExam Pro</div>
            <div className="brand-subtitle">Technical MCQ Exam Simulator</div>
          </div>
        </div>

        {!isExamActive && (
          <nav className="nav-links">
            <button
              className={`nav-btn ${currentView === 'dashboard' ? 'active' : ''}`}
              onClick={() => onNavigate('dashboard')}
            >
              <Layers size={16} />
              <span>Dashboard</span>
            </button>

            <button
              className={`nav-btn ${currentView === 'explorer' ? 'active' : ''}`}
              onClick={() => onNavigate('explorer')}
            >
              <BookOpen size={16} />
              <span>Question Explorer</span>
            </button>

            <button
              className={`nav-btn ${currentView === 'incorrect' ? 'active' : ''}`}
              onClick={() => onNavigate('incorrect')}
            >
              <AlertCircle size={16} />
              <span>Weak Spots</span>
              {incorrectCount > 0 && (
                <span className="badge badge-hard" style={{ padding: '0.1rem 0.45rem', fontSize: '0.7rem' }}>
                  {incorrectCount}
                </span>
              )}
            </button>

            <button
              className={`nav-btn ${currentView === 'flagged' ? 'active' : ''}`}
              onClick={() => onNavigate('flagged')}
            >
              <Bookmark size={16} />
              <span>Flagged</span>
              {flaggedCount > 0 && (
                <span className="badge badge-medium" style={{ padding: '0.1rem 0.45rem', fontSize: '0.7rem' }}>
                  {flaggedCount}
                </span>
              )}
            </button>
          </nav>
        )}

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <button
            className="btn btn-ghost btn-sm"
            onClick={onOpenShortcuts}
            title="Keyboard Shortcuts (?)"
          >
            <HelpCircle size={18} />
          </button>

          <button
            className="btn btn-ghost btn-sm"
            onClick={toggleTheme}
            title={`Switch to ${preferences.theme === 'dark' ? 'Light' : 'Dark'} mode`}
          >
            {preferences.theme === 'dark' ? <Sun size={18} color="#f59e0b" /> : <Moon size={18} color="#3b82f6" />}
          </button>

          {!isExamActive && (
            <button
              className="btn btn-ghost btn-sm"
              onClick={onResetProgress}
              title="Reset All Progress"
              style={{ color: 'var(--text-muted)' }}
            >
              <RotateCcw size={16} />
            </button>
          )}
        </div>
      </div>
    </header>
  );
};
