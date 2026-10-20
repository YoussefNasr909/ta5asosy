import React, { useState, useMemo } from 'react';
import { Search, Filter, Eye, EyeOff, BookOpen, FileText, Sparkles, ChevronLeft, ChevronRight, Bookmark } from 'lucide-react';
import { Question, TopicType, DifficultyType, SourceType } from '../types';

interface QuestionExplorerProps {
  questions: Question[];
  flaggedQuestionIds: string[];
  onToggleFlag: (id: string) => void;
  onPracticeSingleQuestion: (q: Question) => void;
}

export const QuestionExplorer: React.FC<QuestionExplorerProps> = ({
  questions,
  flaggedQuestionIds,
  onToggleFlag,
  onPracticeSingleQuestion,
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTopic, setSelectedTopic] = useState<TopicType | 'All Topics'>('All Topics');
  const [selectedSubtopic, setSelectedSubtopic] = useState<string>('All Subtopics');
  const [selectedDifficulty, setSelectedDifficulty] = useState<DifficultyType | 'all'>('all');
  const [selectedSource, setSelectedSource] = useState<SourceType | 'all'>('all');
  const [revealedIds, setRevealedIds] = useState<Set<string>>(new Set());
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 12;

  const flaggedSet = useMemo(() => new Set(flaggedQuestionIds), [flaggedQuestionIds]);

  const availableSubtopics = useMemo(() => {
    let list = questions;
    if (selectedTopic !== 'All Topics') {
      list = list.filter(q => q.topic === selectedTopic);
    }
    const subs = Array.from(new Set(list.map(q => q.subtopic))).sort();
    return ['All Subtopics', ...subs];
  }, [questions, selectedTopic]);

  const filteredQuestions = useMemo(() => {
    return questions.filter(q => {
      if (selectedTopic !== 'All Topics' && q.topic !== selectedTopic) return false;
      if (selectedSubtopic !== 'All Subtopics' && q.subtopic !== selectedSubtopic) return false;
      if (selectedDifficulty !== 'all' && q.difficulty !== selectedDifficulty) return false;
      if (selectedSource !== 'all' && q.sourceType !== selectedSource) return false;

      if (searchTerm.trim()) {
        const term = searchTerm.toLowerCase();
        const matchesQ = q.question.toLowerCase().includes(term);
        const matchesExp = q.explanation.toLowerCase().includes(term);
        const matchesSub = q.subtopic.toLowerCase().includes(term);
        const matchesOpt = q.options.some(o => o.text.toLowerCase().includes(term));
        if (!matchesQ && !matchesExp && !matchesSub && !matchesOpt) return false;
      }

      return true;
    });
  }, [questions, selectedTopic, selectedSubtopic, selectedDifficulty, selectedSource, searchTerm]);

  const totalPages = Math.ceil(filteredQuestions.length / pageSize) || 1;
  const paginatedQuestions = filteredQuestions.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  const toggleReveal = (id: string) => {
    const next = new Set(revealedIds);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    setRevealedIds(next);
  };

  const revealAllOnPage = () => {
    const next = new Set(revealedIds);
    paginatedQuestions.forEach(q => next.add(q.id));
    setRevealedIds(next);
  };

  const hideAllOnPage = () => {
    const next = new Set(revealedIds);
    paginatedQuestions.forEach(q => next.delete(q.id));
    setRevealedIds(next);
  };

  const isArabicText = (text: string): boolean => {
    return /[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]/.test(text);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      {/* Header and Controls */}
      <div className="card" style={{ padding: '1.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', flexWrap: 'wrap', gap: '0.75rem' }}>
          <div>
            <h1 style={{ fontSize: '1.75rem' }}>Question Bank Explorer</h1>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Search, filter, and study all 300 technical questions with instant answer reveals
            </p>
          </div>

          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button className="btn btn-secondary btn-sm" onClick={revealAllOnPage}>
              <Eye size={14} /> Reveal All on Page
            </button>
            <button className="btn btn-secondary btn-sm" onClick={hideAllOnPage}>
              <EyeOff size={14} /> Hide All
            </button>
          </div>
        </div>

        {/* Search Input */}
        <div style={{ position: 'relative', marginBottom: '1rem' }}>
          <Search size={18} style={{ position: 'absolute', left: '1rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
          <input
            type="text"
            placeholder="Search keywords in questions, SQL statements, protocols, or explanations..."
            value={searchTerm}
            onChange={e => {
              setSearchTerm(e.target.value);
              setCurrentPage(1);
            }}
            style={{
              width: '100%',
              padding: '0.75rem 1rem 0.75rem 2.75rem',
              borderRadius: '12px',
              border: '1px solid var(--border-prominent)',
              background: 'var(--bg-surface)',
              color: 'var(--text-primary)',
              fontSize: '0.95rem',
              outline: 'none',
            }}
          />
        </div>

        {/* Filters Row */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '0.75rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.25rem' }}>
              Domain Topic
            </label>
            <select
              className="btn btn-secondary btn-sm"
              style={{ width: '100%', textAlign: 'left', borderRadius: '8px' }}
              value={selectedTopic}
              onChange={e => {
                setSelectedTopic(e.target.value as any);
                setSelectedSubtopic('All Subtopics');
                setCurrentPage(1);
              }}
            >
              <option value="All Topics">All Topics</option>
              <option value="Computer Networking">Computer Networking</option>
              <option value="SQL">SQL Fundamentals</option>
              <option value="Database Fundamentals">Database Fundamentals</option>
            </select>
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.25rem' }}>
              Subtopic
            </label>
            <select
              className="btn btn-secondary btn-sm"
              style={{ width: '100%', textAlign: 'left', borderRadius: '8px' }}
              value={selectedSubtopic}
              onChange={e => {
                setSelectedSubtopic(e.target.value);
                setCurrentPage(1);
              }}
            >
              {availableSubtopics.map(s => (
                <option key={s} value={s}>{s}</option>
              ))}
            </select>
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.25rem' }}>
              Difficulty
            </label>
            <select
              className="btn btn-secondary btn-sm"
              style={{ width: '100%', textAlign: 'left', borderRadius: '8px' }}
              value={selectedDifficulty}
              onChange={e => {
                setSelectedDifficulty(e.target.value as any);
                setCurrentPage(1);
              }}
            >
              <option value="all">All Difficulties</option>
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '0.25rem' }}>
              Source Origin
            </label>
            <select
              className="btn btn-secondary btn-sm"
              style={{ width: '100%', textAlign: 'left', borderRadius: '8px' }}
              value={selectedSource}
              onChange={e => {
                setSelectedSource(e.target.value as any);
                setCurrentPage(1);
              }}
            >
              <option value="all">All Sources</option>
              <option value="pdf">Original PDF (30 each)</option>
              <option value="generated">AI-Generated Practice</option>
            </select>
          </div>
        </div>

        {/* Results Counter */}
        <div style={{ marginTop: '1rem', fontSize: '0.85rem', color: 'var(--text-muted)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <span>Showing {paginatedQuestions.length} of {filteredQuestions.length} matching questions</span>
          <span>Page {currentPage} of {totalPages}</span>
        </div>
      </div>

      {/* Questions Cards List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        {paginatedQuestions.length === 0 ? (
          <div className="card" style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            <BookOpen size={40} style={{ margin: '0 auto 1rem auto', opacity: 0.5 }} />
            <h3 style={{ fontSize: '1.2rem', color: 'var(--text-primary)' }}>No Questions Match Your Filters</h3>
            <p style={{ marginTop: '0.25rem' }}>Try clearing the search term or resetting the topic filters.</p>
          </div>
        ) : (
          paginatedQuestions.map((q, idx) => {
            const isRevealed = revealedIds.has(q.id);
            const isFlagged = flaggedSet.has(q.id);
            const globalIndex = (currentPage - 1) * pageSize + idx + 1;

            return (
              <div key={q.id} className="card card-hover" style={{ padding: '1.25rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '0.75rem' }}>
                  <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center', flexWrap: 'wrap' }}>
                    <span style={{ fontWeight: 800, color: 'var(--text-muted)', fontSize: '0.9rem' }}>#{globalIndex}</span>
                    <span className={`badge ${
                      q.topic === 'Computer Networking' ? 'badge-topic-net' :
                      q.topic === 'SQL' ? 'badge-topic-sql' : 'badge-topic-db'
                    }`}>
                      {q.topic}
                    </span>
                    <span className={`badge badge-${q.difficulty}`}>{q.difficulty.toUpperCase()}</span>
                    <span className="badge" style={{ background: 'var(--bg-secondary)', color: 'var(--text-secondary)' }}>{q.subtopic}</span>
                    {q.sourceType === 'pdf' ? (
                      <span className="badge badge-pdf"><FileText size={11} /> {q.sourceFile}</span>
                    ) : (
                      <span className="badge badge-gen"><Sparkles size={11} /> AI Practice</span>
                    )}
                  </div>

                  <div style={{ display: 'flex', gap: '0.4rem', alignItems: 'center' }}>
                    <button
                      className="btn btn-ghost btn-sm"
                      onClick={() => onToggleFlag(q.id)}
                      title={isFlagged ? 'Remove from flagged' : 'Flag this question'}
                      style={{ color: isFlagged ? 'var(--status-warning)' : 'var(--text-muted)' }}
                    >
                      <Bookmark size={16} fill={isFlagged ? 'currentColor' : 'none'} />
                    </button>
                    <button
                      className="btn btn-secondary btn-sm"
                      onClick={() => onPracticeSingleQuestion(q)}
                    >
                      Practice
                    </button>
                    <button
                      className={`btn btn-sm ${isRevealed ? 'btn-primary' : 'btn-secondary'}`}
                      onClick={() => toggleReveal(q.id)}
                    >
                      {isRevealed ? <EyeOff size={14} /> : <Eye size={14} />}
                      <span>{isRevealed ? 'Hide Answer' : 'Reveal Answer'}</span>
                    </button>
                  </div>
                </div>

                <div 
                  className={`question-text ${isArabicText(q.question) ? 'arabic-text' : ''}`}
                  dir={isArabicText(q.question) ? 'rtl' : 'ltr'}
                  style={{ fontSize: '1.05rem', marginBottom: '1rem' }}
                >
                  {q.question}
                </div>

                {/* Options Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '0.5rem', marginBottom: '0.75rem' }}>
                  {q.options.map(opt => {
                    const isCorrect = isRevealed && opt.id === q.correctAnswer;
                    return (
                      <div
                        key={opt.id}
                        style={{
                          padding: '0.65rem 0.85rem',
                          borderRadius: '10px',
                          border: `1px solid ${isCorrect ? 'var(--status-success)' : 'var(--border-subtle)'}`,
                          background: isCorrect ? 'var(--status-success-light)' : 'var(--bg-surface)',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '0.6rem',
                          fontSize: '0.9rem',
                        }}
                      >
                        <span style={{ fontWeight: 700, color: isCorrect ? 'var(--status-success)' : 'inherit' }}>
                          {opt.id})
                        </span>
                        <span 
                          style={{ flex: 1 }}
                          className={isArabicText(opt.text) ? 'arabic-text' : ''}
                          dir={isArabicText(opt.text) ? 'rtl' : 'ltr'}
                        >
                          {opt.text}
                        </span>
                      </div>
                    );
                  })}
                </div>

                {/* Revealed Explanation */}
                {isRevealed && (
                  <div style={{ background: 'var(--bg-secondary)', padding: '0.85rem 1rem', borderRadius: '10px', fontSize: '0.875rem', lineHeight: 1.6, borderLeft: '4px solid var(--accent-primary)' }}>
                    <strong style={{ color: 'var(--accent-primary)' }}>Correct Key ({q.correctAnswer}): </strong>
                    {q.explanation}
                  </div>
                )}
              </div>
            );
          })
        )}
      </div>

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5rem', marginTop: '1rem' }}>
          <button
            className="btn btn-secondary btn-sm"
            disabled={currentPage === 1}
            onClick={() => setCurrentPage(prev => Math.max(1, prev - 1))}
          >
            <ChevronLeft size={16} /> Previous
          </button>

          <span style={{ fontSize: '0.875rem', color: 'var(--text-muted)', margin: '0 0.5rem' }}>
            Page {currentPage} of {totalPages}
          </span>

          <button
            className="btn btn-secondary btn-sm"
            disabled={currentPage === totalPages}
            onClick={() => setCurrentPage(prev => Math.min(totalPages, prev + 1))}
          >
            Next <ChevronRight size={16} />
          </button>
        </div>
      )}
    </div>
  );
};
