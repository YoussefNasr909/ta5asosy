import React from 'react';
import { 
  Play, BookOpen, AlertCircle, Bookmark, CheckCircle2, 
  HelpCircle, Sparkles, FileText, BarChart3, Wifi, Database, Terminal, Clock, ChevronRight
} from 'lucide-react';
import { Question, ExamAttemptRecord, TopicType } from '../types';

interface DashboardProps {
  questions: Question[];
  attempts: ExamAttemptRecord[];
  incorrectCount: number;
  flaggedCount: number;
  onStartExam: (topic?: TopicType | 'All Topics', mode?: 'practice' | 'exam') => void;
  onOpenCustomConfig: () => void;
  onStartIncorrectDrill: () => void;
  onStartFlaggedDrill: () => void;
  onNavigateExplorer: () => void;
  onViewAttempt: (attempt: ExamAttemptRecord) => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  questions,
  attempts,
  incorrectCount,
  flaggedCount,
  onStartExam,
  onOpenCustomConfig,
  onStartIncorrectDrill,
  onStartFlaggedDrill,
  onNavigateExplorer,
  onViewAttempt,
}) => {
  const totalQuestions = questions.length;
  const pdfQuestionsCount = questions.filter(q => q.sourceType === 'pdf').length;
  const genQuestionsCount = questions.filter(q => q.sourceType === 'generated').length;

  const totalAttempts = attempts.length;
  const totalAnswered = attempts.reduce((acc, a) => acc + (a.totalQuestions - a.unansweredCount), 0);
  const totalCorrect = attempts.reduce((acc, a) => acc + a.correctCount, 0);
  const overallAccuracy = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;

  const getTopicCount = (t: TopicType) => questions.filter(q => q.topic === t).length;
  const getTopicPdfCount = (t: TopicType) => questions.filter(q => q.topic === t && q.sourceType === 'pdf').length;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      {/* Hero Welcome Banner */}
      <div 
        className="card" 
        style={{ 
          background: 'linear-gradient(135deg, rgba(37,99,235,0.12), rgba(124,58,237,0.12))',
          borderColor: 'var(--border-prominent)',
          position: 'relative',
          overflow: 'hidden'
        }}
      >
        <div style={{ position: 'relative', zIndex: 1, maxWidth: '800px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem' }}>
            <span className="badge badge-pdf">
              <FileText size={12} /> 3 Verified PDF Sources
            </span>
            <span className="badge badge-gen">
              <Sparkles size={12} /> AI-Generated Practice Bank
            </span>
          </div>

          <h1 style={{ fontSize: '2.25rem', marginBottom: '0.75rem' }}>
            Interactive Technical MCQ Simulator
          </h1>

          <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem', lineHeight: 1.6, marginBottom: '1.5rem' }}>
            Master <strong>Computer Networking</strong>, <strong>SQL</strong>, and <strong>Database Fundamentals</strong> with 300 rigorous technical multiple-choice questions, detailed explanations, real-time feedback, and full simulation exams.
          </p>

          <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
            <button className="btn btn-primary btn-lg" onClick={onOpenCustomConfig}>
              <Play size={18} />
              <span>Configure & Start Exam</span>
            </button>
            <button className="btn btn-secondary btn-lg" onClick={() => onStartExam('All Topics', 'practice')}>
              <Sparkles size={18} />
              <span>Quick Practice Drill</span>
            </button>
          </div>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="dashboard-grid">
        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'rgba(59, 130, 246, 0.15)', color: '#3b82f6' }}>
            <FileText size={26} />
          </div>
          <div>
            <div className="stat-val">{totalQuestions}</div>
            <div className="stat-label">Total Questions Bank</div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.2rem' }}>
              {pdfQuestionsCount} PDF • {genQuestionsCount} Generated
            </div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'rgba(16, 185, 129, 0.15)', color: '#10b981' }}>
            <CheckCircle2 size={26} />
          </div>
          <div>
            <div className="stat-val">{overallAccuracy}%</div>
            <div className="stat-label">Overall Accuracy</div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.2rem' }}>
              {totalCorrect} / {totalAnswered} Correct Answers
            </div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon" style={{ background: 'rgba(124, 58, 237, 0.15)', color: '#8b5cf6' }}>
            <BarChart3 size={26} />
          </div>
          <div>
            <div className="stat-val">{totalAttempts}</div>
            <div className="stat-label">Exams Completed</div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.2rem' }}>
              Saved in Local History
            </div>
          </div>
        </div>

        <div className="stat-card" style={{ cursor: 'pointer' }} onClick={onStartIncorrectDrill}>
          <div className="stat-icon" style={{ background: 'rgba(239, 68, 68, 0.15)', color: '#ef4444' }}>
            <AlertCircle size={26} />
          </div>
          <div>
            <div className="stat-val">{incorrectCount}</div>
            <div className="stat-label">Weak Spots To Review</div>
            <div style={{ fontSize: '0.75rem', color: '#ef4444', marginTop: '0.2rem', fontWeight: 600 }}>
              Click to practice missed
            </div>
          </div>
        </div>
      </div>

      {/* Topic Cards */}
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem' }}>Subject Learning Tracks</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Choose a technical domain to start a focused practice or full timed exam simulation.
            </p>
          </div>
          <button className="btn btn-ghost btn-sm" onClick={onNavigateExplorer}>
            Browse All Questions <ChevronRight size={16} />
          </button>
        </div>

        <div className="topic-cards-grid">
          {/* Networking */}
          <div className="topic-card net card-hover">
            <div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span className="badge badge-topic-net">
                  <Wifi size={13} /> Computer Networking
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  {getTopicCount('Computer Networking')} Questions
                </span>
              </div>
              <h3 style={{ fontSize: '1.2rem', marginBottom: '0.5rem' }}>Computer Networking</h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.5 }}>
                OSI & TCP/IP models, routing & switching, subnetting/CIDR, DNS, DHCP, ARP, TCP/UDP sockets, ports, Wireshark, and security protocols.
              </p>
              <div style={{ marginTop: '0.75rem', display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
                <span className="badge badge-pdf">{getTopicPdfCount('Computer Networking')} Original PDF</span>
                <span className="badge badge-gen">70 Practice</span>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '0.5rem', marginTop: '1rem' }}>
              <button 
                className="btn btn-secondary btn-sm" 
                style={{ flex: 1 }}
                onClick={() => onStartExam('Computer Networking', 'practice')}
              >
                Practice Mode
              </button>
              <button 
                className="btn btn-primary btn-sm" 
                style={{ flex: 1 }}
                onClick={() => onStartExam('Computer Networking', 'exam')}
              >
                Simulate Exam
              </button>
            </div>
          </div>

          {/* SQL */}
          <div className="topic-card sql card-hover">
            <div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span className="badge badge-topic-sql">
                  <Terminal size={13} /> SQL Fundamentals
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  {getTopicCount('SQL')} Questions
                </span>
              </div>
              <h3 style={{ fontSize: '1.2rem', marginBottom: '0.5rem' }}>SQL (Structured Query Language)</h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.5 }}>
                Complex JOINs, aggregates & GROUP BY, correlated subqueries, window functions, NULL 3VL logic, CTEs, indexes, DDL/DML, and query optimization.
              </p>
              <div style={{ marginTop: '0.75rem', display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
                <span className="badge badge-pdf">{getTopicPdfCount('SQL')} Original PDF (Arabic/En)</span>
                <span className="badge badge-gen">70 Practice</span>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '0.5rem', marginTop: '1rem' }}>
              <button 
                className="btn btn-secondary btn-sm" 
                style={{ flex: 1 }}
                onClick={() => onStartExam('SQL', 'practice')}
              >
                Practice Mode
              </button>
              <button 
                className="btn btn-primary btn-sm" 
                style={{ flex: 1 }}
                onClick={() => onStartExam('SQL', 'exam')}
              >
                Simulate Exam
              </button>
            </div>
          </div>

          {/* Database Fundamentals */}
          <div className="topic-card db card-hover">
            <div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                <span className="badge badge-topic-db">
                  <Database size={13} /> Database Fundamentals
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  {getTopicCount('Database Fundamentals')} Questions
                </span>
              </div>
              <h3 style={{ fontSize: '1.2rem', marginBottom: '0.5rem' }}>Database Fundamentals</h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.5 }}>
                Relational model theory, normalization (1NF-BCNF), ER modeling, ACID properties, 2PL locking, ARIES recovery, B+ trees, and relational algebra.
              </p>
              <div style={{ marginTop: '0.75rem', display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
                <span className="badge badge-pdf">{getTopicPdfCount('Database Fundamentals')} Original PDF</span>
                <span className="badge badge-gen">70 Practice</span>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '0.5rem', marginTop: '1rem' }}>
              <button 
                className="btn btn-secondary btn-sm" 
                style={{ flex: 1 }}
                onClick={() => onStartExam('Database Fundamentals', 'practice')}
              >
                Practice Mode
              </button>
              <button 
                className="btn btn-primary btn-sm" 
                style={{ flex: 1 }}
                onClick={() => onStartExam('Database Fundamentals', 'exam')}
              >
                Simulate Exam
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Recent Exam History */}
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem' }}>
          <div>
            <h2 style={{ fontSize: '1.25rem' }}>Recent Exam Sessions</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem' }}>
              Your latest simulation attempts and test results
            </p>
          </div>
          {attempts.length > 0 && (
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              Showing last {Math.min(attempts.length, 5)} attempts
            </span>
          )}
        </div>

        {attempts.length === 0 ? (
          <div style={{ padding: '2.5rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            <FileText size={36} style={{ margin: '0 auto 0.75rem auto', opacity: 0.5 }} />
            <p style={{ fontWeight: 600, fontSize: '1rem', color: 'var(--text-secondary)' }}>No exam attempts recorded yet</p>
            <p style={{ fontSize: '0.875rem', marginTop: '0.25rem' }}>
              Start your first practice session or simulated exam to track your mastery.
            </p>
            <button className="btn btn-primary btn-sm" style={{ marginTop: '1rem' }} onClick={onOpenCustomConfig}>
              Start First Exam
            </button>
          </div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.9rem' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid var(--border-subtle)', color: 'var(--text-muted)' }}>
                  <th style={{ padding: '0.75rem 1rem' }}>Date & Time</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Topic</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Mode</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Questions</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Score</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Time</th>
                  <th style={{ padding: '0.75rem 1rem', textAlign: 'right' }}>Action</th>
                </tr>
              </thead>
              <tbody>
                {attempts.slice(0, 5).map(att => (
                  <tr key={att.id} style={{ borderBottom: '1px solid var(--border-subtle)' }}>
                    <td style={{ padding: '0.75rem 1rem', whiteSpace: 'nowrap' }}>
                      {new Date(att.timestamp).toLocaleDateString()} {new Date(att.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </td>
                    <td style={{ padding: '0.75rem 1rem' }}>
                      <strong>{att.config.topic}</strong>
                    </td>
                    <td style={{ padding: '0.75rem 1rem' }}>
                      <span className="badge" style={{ textTransform: 'capitalize' }}>
                        {att.config.mode}
                      </span>
                    </td>
                    <td style={{ padding: '0.75rem 1rem' }}>
                      {att.correctCount} / {att.totalQuestions}
                    </td>
                    <td style={{ padding: '0.75rem 1rem' }}>
                      <span className={`badge ${att.passed ? 'badge-easy' : 'badge-hard'}`}>
                        {att.scorePercentage}% {att.passed ? 'PASS' : 'FAIL'}
                      </span>
                    </td>
                    <td style={{ padding: '0.75rem 1rem', color: 'var(--text-secondary)' }}>
                      {Math.floor(att.durationSeconds / 60)}m {att.durationSeconds % 60}s
                    </td>
                    <td style={{ padding: '0.75rem 1rem', textAlign: 'right' }}>
                      <button className="btn btn-secondary btn-sm" onClick={() => onViewAttempt(att)}>
                        Review Results
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
