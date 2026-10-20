# TechExam Pro — Interactive Technical MCQ Exam Simulator

[![Live Website](https://img.shields.io/badge/Live_Site-Online-success?style=for-the-badge&logo=github)](https://youssefnasr909.github.io/ta5asosy/)
[![Total Questions](https://img.shields.io/badge/Question_Bank-300_Questions-blue?style=for-the-badge)](https://youssefnasr909.github.io/ta5asosy/)

**🌐 Live Demo:** **[https://youssefnasr909.github.io/ta5asosy/](https://youssefnasr909.github.io/ta5asosy/)**

A local-first, full-stack technical assessment platform and exam simulator covering **Computer Networking**, **SQL Fundamentals**, and **Database Fundamentals**. Built with **React 19**, **TypeScript**, and **Vite**, featuring modern responsive design, dark/light modes, dual exam engines (Practice vs. Exam Simulation), question bank explorer, progress persistence, and 300 rigorously verified questions.

---

## 1. Source Extraction Report

All three original PDF files were parsed, verified, and mapped into structured JSON with 100% data fidelity:

| # | Source PDF File Name | Domain Topic | Questions Extracted | Imported | Review Items / Notes |
|---|----------------------|--------------|---------------------|----------|----------------------|
| 1 | `Networking_Fundamentals_30_MCQ_Questions.pdf` | Computer Networking | 30 / 30 | 30 | 0 ambiguities; font spacing normalized |
| 2 | `Database_Fundamentals_30_MCQ_Questions.pdf` | Database Fundamentals | 30 / 30 | 30 | 0 ambiguities; font spacing normalized |
| 3 | `أسئلة_MCQ_في_أساسيات_SQL.pdf` | SQL Fundamentals | 30 / 30 | 30 | Preserved original Arabic text with full RTL font support and English translations |
| **Total Original** | — | — | **90** | **90** | **0 unresolved ambiguities** |

### Question Bank Expansion Summary
In accordance with the expansion requirements, **210 high-quality practice questions** (70 per topic) were created and labeled as `sourceType: "generated"`:

- **Computer Networking:** 30 PDF Original + 70 AI Practice = **100 Questions**
- **SQL Fundamentals:** 30 PDF Original + 70 AI Practice = **100 Questions**
- **Database Fundamentals:** 30 PDF Original + 70 AI Practice = **100 Questions**
- **Total Question Bank:** **300 Questions** (Easy: 124, Medium: 116, Hard: 60)

---

## 2. Key Features

### A. Home Dashboard
- Real-time statistics: Total Questions, Source breakdown (PDF vs. Generated), Overall accuracy %, and completed attempts.
- Subject track cards for **Networking**, **SQL**, and **Database Fundamentals** with one-click **Practice Mode** or **Exam Mode**.
- Quick launch buttons: Custom Exam setup, Weak Spots Drill (previously incorrect), and Flagged Review.
- Interactive Recent Sessions table with dates, modes, scores, and direct review links.

### B. Custom Exam Configuration
- **Domain Filter:** All Topics, or single domain.
- **Subtopic Filter:** Dynamic list of subtopics based on selected domain.
- **Difficulty Selection:** Mixed (all difficulties), Easy only, Medium only, Hard only.
- **Source Origin:** All Questions, Original PDF Questions Only, or AI-Generated Practice Only.
- **Question Count:** Presets (10, 20, 30, 50, All) or interactive range slider with live pool counter.
- **Exam Modes:**
  - **Practice Mode:** Instant feedback upon checking an answer, correct/incorrect badges, and full explanation.
  - **Exam Simulation:** Formal test with timer, no answer leaks until submission, and review flags.
- **Randomization & Options Shuffling:** Mathematically verified option shuffling preserving correct answer keys.
- **Countdown Timer:** Configurable time limits with automatic submission upon expiration.

### C. Distraction-Free Exam Interface
- Question counter, progress bar, topic badge, difficulty pill, and source origin tag.
- Full RTL and Arabic typography support (Tajawal font) for Arabic SQL questions.
- Question navigation via **Previous/Next** buttons or jumping directly through the **Question Navigator Grid**.
- Keyboard shortcuts:
  - `1`, `2`, `3`, `4` or `A`, `B`, `C`, `D` to select options.
  - `←` / `P` for Previous, `→` / `N` for Next.
  - `F` to toggle review flag.
  - `Enter` to check answer in Practice Mode.
  - `?` to toggle shortcuts cheat sheet.
- Unanswered questions warning dialog before final submission.

### D. Comprehensive Results & Performance Review
- Circular percentage scorecard with celebratory confetti on passing score (default ≥ 70%).
- Subject-wise and difficulty-wise performance breakdown bars.
- Question-by-question review with filters: **All**, **Incorrect Only**, **Correct Only**, **Flagged Only**.
- Direct actions: **Retry Incorrect Questions**, **Retake Same Config**, and **Back to Dashboard**.

### E. Question Bank Explorer
- Search bar filtering by keywords across question text, options, explanations, and subtopics.
- Filter chips by domain, subtopic, difficulty, and source type.
- On-demand **Reveal Answer & Explanation** toggle without taking an exam.
- Individual question practice action.

### F. Persistence & Privacy
- Local-first architecture: All exam attempts, weak spots, flagged items, and theme preferences persist in browser `localStorage`.
- Explicit confirmation dialog for resetting progress.

---

## 3. Technology Stack

- **Frontend Core:** React 19, TypeScript 5, Vite 6
- **Styling:** Vanilla CSS design system (`src/index.css`) with CSS custom properties, glassmorphism, responsive grid layouts, and light/dark theme variables.
- **Typography:** Google Fonts (`Inter`, `Outfit`, `Fira Code`, `Tajawal`).
- **Icons & Effects:** `lucide-react`, `canvas-confetti`.
- **Backend / Data:** Pure local-first architecture (embedded `src/data/questions.json`).

---

## 4. Getting Started Locally

### Prerequisites
- Node.js (v18 or higher recommended, tested on v22.20.0)
- npm (v9 or higher, tested on v11.6.1)

### Installation & Run

1. Clone or navigate to the project directory:
   ```bash
   cd "c:\Users\Youssef Nasr\Downloads\ta5asosy"
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

### Other Available Scripts
- **`npm run build`**: Type-checks and compiles the production bundle into `dist/`.
- **`npm test`**: Runs unit test suite for core exam logic.
- **`python scripts/validate_questions.py`**: Runs schema validation on all 300 questions.
- **`python scripts/build_question_bank.py`**: Recompiles `src/data/questions.json` from extraction sources.

---

## 5. Question Bank Schema

Every question in `src/data/questions.json` adheres to the following interface:

```typescript
interface Question {
  id: string;               // Unique stable identifier (e.g., "net-orig-01", "sql-gen-15")
  topic: TopicType;         // "Computer Networking" | "Database Fundamentals" | "SQL"
  subtopic: string;         // e.g. "OSI & TCP/IP Models", "Joins", "Normalization"
  question: string;         // Clean question statement
  options: [                // Exactly 4 options with stable IDs
    { id: "A", text: string },
    { id: "B", text: string },
    { id: "C", text: string },
    { id: "D", text: string }
  ];
  correctAnswer: "A" | "B" | "C" | "D"; // Matches option id
  explanation: string;      // In-depth technical rationale
  difficulty: "easy" | "medium" | "hard";
  sourceType: "pdf" | "generated";
  sourceFile: string;       // Original PDF filename or "AI Practice Bank"
  sourcePage?: number;
  reviewStatus: string;     // "verified"
}
```

---

## 6. Testing & Quality Assurance Summary

The following test suites were executed and verified:

1. **Automated Unit Tests (`npm test`):**
   - Verified that option shuffling preserves correct-answer mapping across 100 trials without leaking or altering keys.
   - Verified calculation of percentage scores, passing criteria, and domain breakdowns.
   - Verified tracking of answered, incorrect, and skipped questions.
   - Verified edge cases in timer calculations and duration formatting.
2. **Schema & Bank Validation (`python scripts/validate_questions.py`):**
   - Validated 0 duplicate IDs across all 300 items.
   - Validated that all 300 questions contain non-empty questions, explanations, and 4 distinct options.
   - Validated that every `correctAnswer` matches an existing option ID.
   - Validated topic, difficulty, and source type enumerations.
3. **Browser Interactive Testing:**
   - Tested dashboard rendering, metrics counters, and topic learning cards.
   - Tested live search and answer-reveal toggles in Question Explorer.
   - Tested Practice Mode immediate feedback and explanation accordions.
   - Tested question navigator grid, flag toggling, and unanswered question warning modals.
   - Tested exam submission, scorecard calculation, and retry incorrect questions workflows.
