def score_code(code: str, tests: str | None) -> int:
    score = 50  # base score

    if not isinstance(code, str) or not code.strip():
        return 0

    if "def " in code or "class " in code:
        score += 15

    if "return" in code:
        score += 10

    if tests and isinstance(tests, str):
        if "assert" in tests:
            score += 15
        if "pytest" in tests:
            score += 10

    return min(score, 100)
