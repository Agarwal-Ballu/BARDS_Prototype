import httpx
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def gemini(prompt: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(url, headers=headers, params=params, json=payload)

    data = r.json()

    # ✅ HANDLE QUOTA ERROR GRACEFULLY
    if "error" in data:
        return "__GEMINI_ERROR__:" + data["error"].get("message", "Unknown error")

    return data["candidates"][0]["content"]["parts"][0]["text"]
