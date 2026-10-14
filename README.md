# bug-hunter

# ⚡ Bug Hunter

> An automated runtime error triage engine and unified patch generator.

Developers spend 40–50% of their time deciphering cryptic stack traces, isolating failing logic, and manually testing bug fixes. **Bug Hunter** automates the entire debugging lifecycle by converting raw runtime errors and source code into verified root-cause diagnoses, unified Git diff patches, and regression unit tests.

---

## 🎯 Features

- **Automated Stack Trace Parsing:** Extracts the failing file, line number, and error type from raw logs.
- **Root-Cause Analysis:** Uses Google Gemini models to explain the exact failure mechanism.
- **Unified Git Diff Generation:** Proposes a clean `diff --git` patch scoped strictly to the bug.
- **Regression Prevention:** Generates ready-to-run unit tests to ensure the bug never returns.
- **Smart High-Load Fallback:** Automatically cascades through fallback models if high traffic or rate limits occur.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn
- **AI & Reasoning:** Google Gemini API (`gemini-3.8-flash` with fallback to `gemini-3.5-flash-lite`)
- **Frontend:** HTML5, Modern JavaScript (Fetch API), Tailwind CSS

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/bug-hunter.git](https://github.com/YOUR_GITHUB_USERNAME/bug-hunter.git)
cd bug-hunter
