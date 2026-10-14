# ⚡ Bug Hunter

> Automated runtime error triage and unified patch generation powered by Google Gemini.

Developers spend a significant amount of time deciphering cryptic stack traces, isolating failing logic, and manually testing bug fixes. **Bug Hunter** automates the debugging lifecycle by converting raw runtime errors and source code into verified root-cause diagnoses, unified Git diff patches, and regression unit tests.

---

## 🎯 Features

- **Automated Stack Trace Parsing:** Extracts the failing file, line number, and error type from raw logs.
- **Root-Cause Analysis:** Uses Google Gemini models to explain the exact failure mechanism.
- **Unified Git Diff Generation:** Proposes a clean `diff --git` patch scoped strictly to the bug.
- **Regression Prevention:** Generates ready-to-run `unittest` suites to ensure the bug never returns.
- **Multi-Model High-Availability Fallback:** Automatically cascades across `gemini-3.8-flash`, `gemini-3.5-flash-lite`, and `gemini-3.6-flash` to prevent `503 UNAVAILABLE` downtime during traffic spikes.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn
- **AI & Reasoning:** Google GenAI SDK (`google-genai`)
- **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS

---

## 🚀 Getting Started (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/pawartarun3228/bug-hunter.git
cd bug-hunter
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Your Gemini API Key
Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey) and set it in your terminal before running the server:

- **Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="your_api_key_here"
  ```
- **Windows (Command Prompt):**
  ```cmd
  set GEMINI_API_KEY=your_api_key_here
  ```
- **macOS / Linux:**
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```

### 4. Start the Backend Server
```bash
python main.py
```
The server will start at `http://127.0.0.1:8000`.

### 5. Launch the Web Interface
Open `index.html` directly in your browser (double-click the file in File Explorer).

---

## 🧪 Quick Test Input

Paste the following into the UI to test:

**Stack Trace / Runtime Error:**
```text
ZeroDivisionError: division by zero
  File "app.py", line 3, in calculate_average
```

**Source Code Context:**
```python
def calculate_average(items):
    total = sum(items)
    return total / len(items)
```