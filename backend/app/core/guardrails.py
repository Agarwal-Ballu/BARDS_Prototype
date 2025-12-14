import ast

def validate_prompt(prompt: str):
    forbidden = ["java", "c++", "javascript", "html", "css", "sql", "ruby", "php", "swift", "kotlin","C","Go","Rust"]
    if any(x in prompt.lower() for x in forbidden):
        raise ValueError("Only Python-related tasks allowed")

def validate_python(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False
