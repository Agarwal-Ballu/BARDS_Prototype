import httpx
import os
from dotenv import load_dotenv

load_dotenv()
BASE = os.getenv("OLLAMA_BASE_URL")
MODEL = os.getenv("OLLAMA_MODEL")

async def ollama(prompt: str) -> str:
    if not BASE or not MODEL:
        raise RuntimeError("OLLAMA_BASE_URL or OLLAMA_MODEL not set in .env")

    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(
            f"{BASE}/api/chat",
            json={
                "model": MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a senior Python developer. you make code based on the complexity of question and try to make simple codes with less time and space complexity. Output ONLY Python code."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False
            }
        )

    try:
        data = r.json()
    except Exception:
        raise RuntimeError(f"Ollama returned non-JSON response: {r.text}")

    print("🔍 Ollama raw response:", data)  # DEBUG

    # Handle Ollama errors
    if "error" in data:
        raise RuntimeError(f"Ollama error: {data['error']}")

    # New Ollama chat format
    if "message" in data and "content" in data["message"]:
        return data["message"]["content"]

    # Older generate format fallback
    if "response" in data:
        return data["response"]

    raise RuntimeError(f"Unexpected Ollama response format: {data}")
