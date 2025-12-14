def is_python_related(prompt: str) -> bool:
    keywords = [
        "python", "palindrome", "list", "loop", "function",
        "sort", "array", "string", "algorithm", "code"
    ]
    p = prompt.lower()
    return any(k in p for k in keywords)
