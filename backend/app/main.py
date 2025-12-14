from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Boosted AI-Driven Refactoring System")
app.include_router(router)


