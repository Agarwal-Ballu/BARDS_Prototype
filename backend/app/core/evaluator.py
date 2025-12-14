from app.core.guardrails import validate_python
from app.llm.gemini import gemini


async def fix_code(code: str):
    if validate_python(code):
        return code

    return await gemini(
        f"Fix Python errors. Output only corrected code:\n{code}"
    )
