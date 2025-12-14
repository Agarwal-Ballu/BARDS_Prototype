This is the backend service for the Boosted AI Driven Refactoring System (Hybrid model code generator/debugger).
It powers the VS Code extension by generating, debugging, and evaluating Python code using a hybrid AI approach:

Gemini → reasoning, planning, validation

CodeLlama (via Ollama) → final code generation (local)

The backend runs locally using FastAPI and does not expose API keys in code.

-------------------------------------------------------------------------------------------------------------------

🚀 Features

✅ Hybrid LLM pipeline (Gemini + CodeLlama)
✅ Python-only code generation & debugging
✅ Optional auto-test generation
✅ AI accuracy scoring
✅ Guardrails to reject non-Python requests
✅ Environment-based secret management
✅ FastAPI + async execution


--------------------------------------------------------------------------------------------------------------------

🧰 Prerequisites

Make sure you have:
---> Python 3.9+
---> Ollama installed and running
---> CodeLlama pulled locally:
        ollama pull codellama
---> A valid Gemini API key

Installation :-
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

-----------------------------------------------------------------------------------------------------------------------

▶️ Run the Server

uvicorn app.main:app --reload
Api docs available at - http://127.0.0.1:8000/docs


🛡️ Guardrails

❌ Non-Python questions are rejected
❌ Explanations removed when not requested
✅ Code-only output enforced
✅ Safe fallback to CodeLlama if Gemini quota fails

------------------------------------------------------------------------------------------------------------------------

Flow :-

 User Prompt -->  Language Guard (Python only) --> Gemini (planning / validation) (fallback if quota fails) --> CodeLlama (code generation) --> Accuracy Scoring --> VS Code Extension
