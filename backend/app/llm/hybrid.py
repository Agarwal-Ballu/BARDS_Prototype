from app.llm.ollama import ollama
from app.llm.gemini_safe import safe_gemini
from app.core.language_guard import is_python_related
from app.core.code_parser import extract_python_code


async def hybrid_engine(user_prompt: str) -> str:
    #Reject non-Python question s
    if not is_python_related(user_prompt):
        return (
            "Aww, thanks for asking! \n"
            "I’m a Python-only code generator and debugger. \n" 
            "Please ask something related to Python so I can help you properly."
        )

    # Try Gemini
    plan = await safe_gemini(
        f"""
You are a senior Python engineer.
Plan the solution briefly.
make it simple and efficient.
RULES:
- Output ONLY plan for Python code
- No markdown
- can give steps and pseiudocode and algorithm
- help to understand the problem better
- Don't make complex plans if not needed , keep it simple and efficient as per the question complexity 
Do NOT write code.

TASK:
{user_prompt}
"""
    )

    #CodeLlama ALWAYS generates code
    if plan:
        prompt = f"""
You are a expert senior Python code generator.
You are expert in converting plans into efficient Python code and you can debugg codes as well.
You generate code based on the plan provided and helps user to get the best possible solution.
RULES:
- Output ONLY Python code
- Only generete code provide based on the plan
- No markdown
- No explanation

PLAN:
{plan}

TASK:
{user_prompt}
"""
    else:
        # Gemini failed then will use only CodeLlama
        prompt = f"""
You are a Python code generator.
You are expert in converting plans into efficient Python code and you can debugg codes as well.
You generate code based on the plan provided and helps user to get the best possible solution.
RULES:
- Output ONLY Python code
- Only generete code provide based on the plan
- No markdown
- No explanation

TASK:
{user_prompt}
"""

    raw = await ollama(prompt)

    #Clean output
    if isinstance(raw, dict):
        raw = raw.get("message", {}).get("content", "")

    return extract_python_code(raw)
