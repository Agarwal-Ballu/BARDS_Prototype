import re

def extract_python_code(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text)}")

    # Remove markdown if present
    blocks = re.findall(r"```(?:python)?(.*?)```", text, re.S)
    if blocks:
        return blocks[0].strip()

    return text.strip()
