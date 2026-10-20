import React from 'react';
import { X, Command } from 'lucide-react';

interface KeyboardShortcutsModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const KeyboardShortcutsModal: React.FC<KeyboardShortcutsModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  const shortcuts = [
    { keys: ['1', '2', '3', '4'], desc: 'Select option A, B, C, or D respectively' },
    { keys: ['A', 'B', 'C', 'D'], desc: 'Select option by letter' },
    { keys: ['→', 'N'], desc: 'Jump to Next question' },
    { keys: ['←', 'P'], desc: 'Jump to Previous question' },
    { keys: ['F'], desc: 'Toggle flag for review on current question' },
    { keys: ['Enter'], desc: 'Check answer immediately (in Practice Mode)' },
    { keys: ['?'], desc: 'Open / close this shortcuts guide' },
    { keys: ['Esc'], desc: 'Close dialogs or cancel actions' },
  ];

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '480px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '0.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Command size={20} color="var(--accent-primary)" />
            <h2 style={{ fontSize: '1.25rem' }}>Keyboard Shortcuts</h2>
          </div>
          <button className="btn btn-ghost btn-sm" onClick={onClose}>
            <X size={18} />
          </button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
          {shortcuts.map((sc, i) => (
            <div 
              key={i} 
              style={{ 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'space-between', 
                padding: '0.5rem 0',
                borderBottom: i < shortcuts.length - 1 ? '1px solid var(--border-subtle)' : 'none',
                fontSize: '0.875rem'
              }}
            >
              <span style={{ color: 'var(--text-secondary)' }}>{sc.desc}</span>
              <div style={{ display: 'flex', gap: '0.35rem' }}>
                {sc.keys.map((k, j) => (
                  <kbd 
                    key={j}
                    style={{
                      padding: '0.2rem 0.5rem',
                      borderRadius: '6px',
                      background: 'var(--bg-secondary)',
                      border: '1px solid var(--border-prominent)',
                      fontFamily: 'var(--font-mono)',
                      fontSize: '0.75rem',
                      fontWeight: 700,
                      color: 'var(--text-primary)',
                      boxShadow: '0 1px 0 rgba(0,0,0,0.2)',
                    }}
                  >
                    {k}
                  </kbd>
                ))}
              </div>
            </div>
          ))}
        </div>

        <button className="btn btn-primary" style={{ width: '100%', marginTop: '1.5rem' }} onClick={onClose}>
          Got it
        </button>
      </div>
    </div>
  );
};
