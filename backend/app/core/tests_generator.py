from app.llm.gemini import gemini

async def generate_tests(code: str) -> str:
    return await gemini(
        f"""
Generate pytest tests for the following Python code.

RULES:
- Output ONLY Python code
- Don't include any explanations or comments
- Give code in proper syntax and formatting , don't make complex
- No markdown

CODE:
{code}
"""
    )
