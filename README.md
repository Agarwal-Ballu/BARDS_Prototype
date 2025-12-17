### Boosted AI-Driven Refactoring System (Hybrid Python Code Generator & Debugger)
This repository contains the **backend service** for **BADRS**, a hybrid AI system that powers a **VS Code extension** for **Python code generation, debugging, refactoring, and evaluation**.
The backend runs **locally** using **FastAPI** and combines:

* **Gemini (Cloud LLM)** → reasoning, planning, validation
* **CodeLlama (via Ollama, Local LLM)** → final Python code generation

🔐 **No API keys are hard-coded** — all secrets are managed via environment variables.

---

## 🚀 Key Features

✅ Hybrid LLM pipeline (Gemini + CodeLlama)
✅ Python-only code generation & debugging
✅ Optional auto-test generation
✅ AI accuracy scoring
✅ Guardrails to reject non-Python prompts
✅ Safe fallback when Gemini quota fails
✅ Environment-based secret management
✅ FastAPI + async execution
✅ Seamless VS Code extension integration

---

## 🧠 Hybrid AI Flow

```
User Prompt
   ↓
Language Guard (Python only)
   ↓
Gemini (Planning / Validation)
   ↓ (fallback if quota fails)
CodeLlama via Ollama (Local Code Generation)
   ↓
Accuracy Scoring
   ↓
VS Code Extension Output
```

---

## 📦 Project Components

### 1️⃣ Backend (FastAPI)

* Handles prompt processing
* Runs hybrid LLM logic
* Scores output accuracy
* Enforces Python guardrails

### 2️⃣ VS Code Extension

* Sends selected code/prompts to backend
* Inserts generated code into editor
* Displays AI accuracy score
* Works fully locally

---

## 🧰 Prerequisites

Make sure you have the following installed:

* **Python 3.9+**
* **Ollama**
* **CodeLlama model**
* **Gemini API Key**
* **VS Code (for extension usage)**

---

## 🦙 Ollama Installation & Setup

### Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Pull CodeLlama Model

```bash
ollama pull codellama:7b-instruct-q4_0
```

### Verify Ollama is Running

```bash
ollama list
```

Ollama API runs locally at:

```
http://127.0.0.1:11434
```

---

## 🌐 (Optional) Expose Ollama via Ngrok

Useful if Gemini or other services need remote access.

### Install pyngrok

```bash
pip install pyngrok
```

### Start Ngrok Tunnel

```python
from pyngrok import ngrok

ngrok.set_auth_token("<YOUR_NGROK_AUTH_TOKEN>")

public_url = ngrok.connect(11434, host_header="localhost:11434")
print("Public Ollama URL:", public_url.public_url)
```

---

## 🔗 Query Ollama Programmatically

```python
import requests

def query_ollama(prompt, model="codellama:7b-instruct-q4_0"):
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json().get("response", "")
```

---

## 🔐 Environment Configuration

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
OLLAMA_BASE_URL=http://127.0.0.1:11434
```

📌 `.env` is ignored by Git (`.env.example` is provided).

---

## ⚙️ Backend Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Run the Backend Server

```bash
uvicorn app.main:app --reload
```

### API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🧩 VS Code Extension Usage

1. Install the `.vsix` extension
2. Open a Python file
3. Select code or place cursor on a line
4. Press:

```
Ctrl + Shift + P → Run Hybrid Python AI
```

The extension will:

* Generate or debug Python code
* Insert output directly into editor
* Show AI accuracy score

---

## 🛡️ Guardrails & Safety

✔️ Only Python-related prompts allowed
❌ Non-Python questions rejected
❌ Unwanted explanations removed
✔️ Code-only output when required
✔️ Automatic fallback to CodeLlama if Gemini fails

Example rejection message:

> *“Aww, thanks for asking! 😊
> I’m built to generate and debug Python code 🐍
> Please try a Python-related question.”*

---

## 📊 Accuracy Scoring

Heuristic scoring based on:

* Structure validity
* Return correctness
* Logic completeness
* Test alignment (if enabled)

Score range: **0–100%**

---

## 🚀 Why BARDS?

Most AI coding tools:

* ❌ Use only one model
* ❌ Leak API keys
* ❌ Break when quota fails

**BARDS is different:**

* ✅ Hybrid & fault-tolerant
* ✅ Local + cloud
* ✅ Secure by design
* ✅ Built for real developers

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## 🔮 Future Roadmap

The current version of **BARDS** focuses on leveraging powerful pre-trained models (Gemini + CodeLlama).
Future updates aim to **eliminate the core limitations of general-purpose LLMs** and move towards a **lean, highly optimized, developer-first AI system**.

### 🚧 Planned Enhancements

#### 1️⃣ Hybrid Fine-Tuned Open-Source Models

* Train and fine-tune **smaller open-source models** specifically for:

  * Python code generation
  * Debugging and refactoring
  * Algorithmic optimization
* Combine multiple specialized models into a **hybrid ensemble** where each model compensates for the weaknesses of others.

#### 2️⃣ Accuracy-First Code Generation

* Focus on producing **logically correct, edge-case-safe code** rather than verbose outputs.
* Automatic optimization for:

  * **Time complexity**
  * **Space complexity**
* Preference for clean, readable, and production-ready code.

#### 3️⃣ Intelligent Model Selection

* Dynamically select the best model based on:

  * Problem type (DSA, scripting, debugging, refactoring)
  * Code size and complexity
  * Performance constraints
* Reduce unnecessary token usage and hallucinations.

#### 4️⃣ Cost-Free & Local-First AI

* Reduce dependency on paid APIs.
* Enable **fully local execution** using fine-tuned lightweight models.
* Ensure high-quality results without subscription-based limitations.

#### 5️⃣ Continuous Self-Improvement Loop

* Use evaluation feedback, test results, and accuracy scores to:

  * Improve model routing logic
  * Identify recurring failure patterns
  * Continuously refine responses

#### 6️⃣ Competitive Alternative to Paid AI Tools

* Deliver **high-quality, optimized code** comparable to premium AI tools.
* Zero or minimal operational cost.
* Transparent, open, and developer-controlled architecture.

---

### 🎯 Long-Term Vision

> To build a **cost-efficient, high-accuracy, developer-grade AI system**
> that generates **optimized, reliable, and minimal Python code**,
> making advanced AI coding assistance accessible to everyone —
> **without locking users behind expensive subscriptions.**

---

## 👤 Author

**Balram Agarwal**

Python • AI • Computer Science Engineering

