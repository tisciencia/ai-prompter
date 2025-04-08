from fastapi import FastAPI
from pydantic import BaseModel
from app.core import process_text
import os


class Input(BaseModel):
    text: str
    model: str | None = None
    mode: str | None = None


app = FastAPI()


@app.post("/process/")
async def process(input: Input):
    model = input.model or os.getenv("OPENAI_API_MODEL")
    mode = input.mode or "traduzir"
    response = process_text(input.text, mode=mode, model=model)
    return {"response": response}
