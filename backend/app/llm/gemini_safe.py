from app.llm.gemini import gemini

async def safe_gemini(prompt: str) -> str | None:
    try:
        response = await gemini(prompt)
        if isinstance(response, str) and response.strip():
            return response
    except Exception as e:
        print("⚠️ Gemini failed:", e)

    return None
