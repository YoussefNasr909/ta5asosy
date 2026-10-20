import React, { useState, useMemo } from 'react';
import { X, Play, Settings, AlertTriangle, Clock, Shuffle, CheckSquare, Sparkles, FileText } from 'lucide-react';
import { Question, ExamConfig, TopicType, DifficultyType, SourceType } from '../types';

interface ExamConfigModalProps {
  allQuestions: Question[];
  initialConfig?: Partial<ExamConfig>;
  isOpen: boolean;
  onClose: () => void;
  onStartExam: (config: ExamConfig) => void;
}

export const ExamConfigModal: React.FC<ExamConfigModalProps> = ({
  allQuestions,
  initialConfig,
  isOpen,
  onClose,
  onStartExam,
}) => {
  const [topic, setTopic] = useState<TopicType | 'All Topics'>(initialConfig?.topic || 'All Topics');
  const [subtopic, setSubtopic] = useState<string>('All Subtopics');
  const [difficulty, setDifficulty] = useState<DifficultyType | 'mixed'>(initialConfig?.difficulty || 'mixed');
  const [sourceType, setSourceType] = useState<SourceType | 'all'>(initialConfig?.sourceType || 'all');
  const [count, setCount] = useState<number>(initialConfig?.count || 20);
  const [mode, setMode] = useState<'practice' | 'exam'>(initialConfig?.mode || 'exam');
  const [order, setOrder] = useState<'random' | 'sequential'>(initialConfig?.order || 'random');
  const [shuffleOptions, setShuffleOptions] = useState<boolean>(initialConfig?.shuffleOptions ?? true);
  const [timed, setTimed] = useState<boolean>(initialConfig?.timed ?? true);
  const [timeLimitMinutes, setTimeLimitMinutes] = useState<number>(initialConfig?.timeLimitMinutes || 20);
  const [passingScore, setPassingScore] = useState<number>(initialConfig?.passingScore || 70);

  // Available subtopics for currently selected topic
  const availableSubtopics = useMemo(() => {
    let list = allQuestions;
    if (topic !== 'All Topics') {
      list = list.filter(q => q.topic === topic);
    }
    const subs = Array.from(new Set(list.map(q => q.subtopic))).sort();
    return ['All Subtopics', ...subs];
  }, [allQuestions, topic]);

  // Live matching question count
  const matchingPoolCount = useMemo(() => {
    let pool = allQuestions;
    if (topic !== 'All Topics') pool = pool.filter(q => q.topic === topic);
    if (subtopic !== 'All Subtopics') pool = pool.filter(q => q.subtopic === subtopic);
    if (difficulty !== 'mixed') pool = pool.filter(q => q.difficulty === difficulty);
    if (sourceType !== 'all') pool = pool.filter(q => q.sourceType === sourceType);
    return pool.length;
  }, [allQuestions, topic, subtopic, difficulty, sourceType]);

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const finalCount = Math.min(count, matchingPoolCount > 0 ? matchingPoolCount : count);
    const config: ExamConfig = {
      topic,
      subtopic,
      difficulty,
      sourceType,
      count: finalCount > 0 ? finalCount : 1,
      mode,
      order,
      shuffleOptions,
      timed: mode === 'exam' ? timed : false,
      timeLimitMinutes: timed ? timeLimitMinutes : 0,
      passingScore,
    };
    onStartExam(config);
  };

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '640px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '0.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Settings size={22} color="var(--accent-primary)" />
            <h2 style={{ fontSize: '1.35rem' }}>Configure Your Exam</h2>
          </div>
          <button className="btn btn-ghost btn-sm" onClick={onClose}>
            <X size={18} />
          </button>
        </div>

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          {/* Mode Selection */}
          <div>
            <label style={{ display: 'block', fontWeight: 600, fontSize: '0.9rem', marginBottom: '0.5rem' }}>
              Exam Mode
            </label>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
              <div
                onClick={() => setMode('practice')}
                style={{
                  border: `2px solid ${mode === 'practice' ? 'var(--accent-primary)' : 'var(--border-subtle)'}`,
                  background: mode === 'practice' ? 'var(--accent-primary-light)' : 'var(--bg-surface)',
                  padding: '0.85rem',
                  borderRadius: '12px',
                  cursor: 'pointer',
                }}
              >
                <div style={{ fontWeight: 700, fontSize: '0.95rem', display: 'flex', alignItems: 'center', gap: '0.4rem', color: mode === 'practice' ? 'var(--accent-primary)' : 'inherit' }}>
                  <Sparkles size={16} /> Practice Mode
                </div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.25rem' }}>
                  Instant answer reveal, explanations after each question, retries enabled.
                </div>
              </div>

              <div
                onClick={() => setMode('exam')}
                style={{
                  border: `2px solid ${mode === 'exam' ? 'var(--accent-primary)' : 'var(--border-subtle)'}`,
                  background: mode === 'exam' ? 'var(--accent-primary-light)' : 'var(--bg-surface)',
                  padding: '0.85rem',
                  borderRadius: '12px',
                  cursor: 'pointer',
                }}
              >
                <div style={{ fontWeight: 700, fontSize: '0.95rem', display: 'flex', alignItems: 'center', gap: '0.4rem', color: mode === 'exam' ? 'var(--accent-primary)' : 'inherit' }}>
                  <Clock size={16} /> Exam Simulation
                </div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.25rem' }}>
                  Formal timed test, no answer leaks until submission, review flags.
                </div>
              </div>
            </div>
          </div>

          {/* Topic & Subtopic */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
            <div>
              <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.35rem' }}>
                Topic Domain
              </label>
              <select
                className="btn btn-secondary"
                style={{ width: '100%', textAlign: 'left', borderRadius: '8px', padding: '0.6rem' }}
                value={topic}
                onChange={e => {
                  setTopic(e.target.value as any);
                  setSubtopic('All Subtopics');
                }}
              >
                <option value="All Topics">All Topics (Networking, SQL, DB)</option>
                <option value="Computer Networking">Computer Networking</option>
                <option value="SQL">SQL Fundamentals</option>
                <option value="Database Fundamentals">Database Fundamentals</option>
              </select>
            </div>

            <div>
              <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.35rem' }}>
                Subtopic
              </label>
              <select
                className="btn btn-secondary"
                style={{ width: '100%', textAlign: 'left', borderRadius: '8px', padding: '0.6rem' }}
                value={subtopic}
                onChange={e => setSubtopic(e.target.value)}
              >
                {availableSubtopics.map(s => (
                  <option key={s} value={s}>{s}</option>
                ))}
              </select>
            </div>
          </div>

          {/* Difficulty & Source Filter */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
            <div>
              <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.35rem' }}>
                Difficulty Level
              </label>
              <select
                className="btn btn-secondary"
                style={{ width: '100%', textAlign: 'left', borderRadius: '8px', padding: '0.6rem' }}
                value={difficulty}
                onChange={e => setDifficulty(e.target.value as any)}
              >
                <option value="mixed">Mixed (All Difficulties)</option>
                <option value="easy">Easy Only</option>
                <option value="medium">Medium Only</option>
                <option value="hard">Hard Only</option>
              </select>
            </div>

            <div>
              <label style={{ display: 'block', fontWeight: 600, fontSize: '0.85rem', marginBottom: '0.35rem' }}>
                Question Origin
              </label>
              <select
                className="btn btn-secondary"
                style={{ width: '100%', textAlign: 'left', borderRadius: '8px', padding: '0.6rem' }}
                value={sourceType}
                onChange={e => setSourceType(e.target.value as any)}
              >
                <option value="all">All Sources (PDF + Generated)</option>
                <option value="pdf">Original PDF Questions Only</option>
                <option value="generated">AI-Generated Practice Bank Only</option>
              </select>
            </div>
          </div>

          {/* Question Count Presets */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.35rem' }}>
              <label style={{ fontWeight: 600, fontSize: '0.85rem' }}>
                Number of Questions
              </label>
              <span style={{ fontSize: '0.8rem', color: matchingPoolCount < count ? 'var(--status-danger)' : 'var(--text-muted)' }}>
                {matchingPoolCount} questions available
              </span>
            </div>

            <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap', marginBottom: '0.5rem' }}>
              {[10, 20, 30, 50, matchingPoolCount].map((presetVal, i) => (
                <button
                  type="button"
                  key={i}
                  className={`btn btn-sm ${count === presetVal ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => setCount(presetVal)}
                >
                  {i === 4 ? `All (${matchingPoolCount})` : presetVal}
                </button>
              ))}
            </div>

            <input
              type="range"
              min="1"
              max={matchingPoolCount > 0 ? matchingPoolCount : 50}
              value={count > matchingPoolCount ? matchingPoolCount : count}
              onChange={e => setCount(parseInt(e.target.value) || 1)}
              style={{ width: '100%', accentColor: 'var(--accent-primary)', cursor: 'pointer' }}
            />
          </div>

          {/* Randomization & Shuffling */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', background: 'var(--bg-secondary)', padding: '0.85rem', borderRadius: '12px' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer', fontSize: '0.85rem', fontWeight: 600 }}>
              <input
                type="checkbox"
                checked={order === 'random'}
                onChange={e => setOrder(e.target.checked ? 'random' : 'sequential')}
                style={{ width: '16px', height: '16px', accentColor: 'var(--accent-primary)' }}
              />
              <span>Randomize Question Order</span>
            </label>

            <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer', fontSize: '0.85rem', fontWeight: 600 }}>
              <input
                type="checkbox"
                checked={shuffleOptions}
                onChange={e => setShuffleOptions(e.target.checked)}
                style={{ width: '16px', height: '16px', accentColor: 'var(--accent-primary)' }}
              />
              <span>Shuffle Answer Options</span>
            </label>
          </div>

          {/* Timer Settings (Exam Mode) */}
          {mode === 'exam' && (
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '1rem', background: 'var(--bg-secondary)', padding: '0.85rem', borderRadius: '12px' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer', fontSize: '0.85rem', fontWeight: 600 }}>
                <input
                  type="checkbox"
                  checked={timed}
                  onChange={e => setTimed(e.target.checked)}
                  style={{ width: '16px', height: '16px', accentColor: 'var(--accent-primary)' }}
                />
                <span>Enable Countdown Timer</span>
              </label>

              {timed && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                  <input
                    type="number"
                    min="1"
                    max="180"
                    value={timeLimitMinutes}
                    onChange={e => setTimeLimitMinutes(Math.max(1, parseInt(e.target.value) || 1))}
                    style={{ width: '60px', padding: '0.3rem', borderRadius: '6px', border: '1px solid var(--border-prominent)', textAlign: 'center', background: 'var(--bg-surface)', color: 'inherit' }}
                  />
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Minutes</span>
                </div>
              )}
            </div>
          )}

          {/* Pool Warning */}
          {matchingPoolCount === 0 && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--status-danger)', fontSize: '0.85rem' }}>
              <AlertTriangle size={16} /> No questions match this combination. Try broadening your criteria.
            </div>
          )}

          {/* Action Buttons */}
          <div style={{ display: 'flex', gap: '0.75rem', marginTop: '0.5rem' }}>
            <button type="button" className="btn btn-secondary" style={{ flex: 1 }} onClick={onClose}>
              Cancel
            </button>
            <button
              type="submit"
              className="btn btn-primary"
              style={{ flex: 2 }}
              disabled={matchingPoolCount === 0}
            >
              <Play size={16} />
              <span>Start {mode === 'practice' ? 'Practice' : 'Exam'} ({Math.min(count, matchingPoolCount)} Questions)</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
