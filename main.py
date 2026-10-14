import os
import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

app = FastAPI(title="Bug Hunter API")

# Enable CORS for local web interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Gemini Client (set GEMINI_API_KEY in your environment)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class BugReportRequest(BaseModel):
    stack_trace: str
    source_code: str
    runtime_language: str = "python"

def parse_error_location(stack_trace: str):
    """Isolates the most recent file, line number, and error message from stack trace."""
    lines = stack_trace.strip().split("\n")
    error_summary = lines[-1] if lines else "Unknown Error"
    
    # Matches common Python stack trace patterns: File "app.py", line 42
    match = re.findall(r'File "([^"]+)", line (\d+)', stack_trace)
    file_info = match[-1] if match else ("unknown", "unknown")
    
    return {
        "file": file_info[0],
        "line": file_info[1],
        "error_type": error_summary
    }

@app.post("/api/analyze-bug")
async def analyze_bug(payload: BugReportRequest):
    if not payload.stack_trace or not payload.source_code:
        raise HTTPException(status_code=400, detail="Stack trace and source code are required.")

    parsed_meta = parse_error_location(payload.stack_trace)

    prompt = f"""
You are Bug Hunter, an expert automated code debugger and patch generator.

Language: {payload.runtime_language}
Target File: {parsed_meta['file']}
Estimated Failure Line: {parsed_meta['line']}
Error Header: {parsed_meta['error_type']}

Stack Trace:
{payload.stack_trace}

Source Code:
{payload.source_code}

Task:
1. Identify the root cause of the crash.
2. Provide a unified Git diff (`diff --git ...`) fixing the error without breaking unrelated logic.
3. Provide a minimal unit test to prevent regression.

Return response in strict JSON format:
{{
  "root_cause": "concise explanation of the bug",
  "diff_patch": "unified git diff block",
  "fixed_code": "complete updated source code",
  "unit_test": "minimal unit test code"
}}
"""

# Models to try in order of preference
    candidate_models = [
        "gemini-3.8-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.6-flash",
    ]

    last_error = None
    for model_name in candidate_models:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            return {
                "metadata": parsed_meta,
                "analysis": response.text,
                "model_used": model_name
            }
        except Exception as e:
            last_error = e
            print(f"Model {model_name} failed: {e}. Trying next fallback...")
            continue

    raise HTTPException(status_code=503, detail=f"All models busy: {last_error}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)