from fastapi import APIRouter
from pydantic import BaseModel
from app.llm.hybrid import hybrid_engine
from app.core.tests_generator import generate_tests
from app.core.accuracy import score_code

router = APIRouter()

class Request(BaseModel):
    prompt: str
    generate_tests: bool = False


@router.post("/generate")
async def generate(req: Request):
    code = await hybrid_engine(req.prompt)

    tests = ""
    accuracy = 0

    if req.generate_tests:
        tests = await generate_tests(code)
        accuracy = score_code(code, tests)
    else:
        accuracy = score_code(code, "")

    return {
        "code": code,
        "tests": tests,
        "accuracy": accuracy
    }
