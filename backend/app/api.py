from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from app.auth import api_key_auth
from app.chatgpt_client import call_chatgpt
from app.config import SUPPORTED_MODELS, SUPPORTED_MODES
from app.prompt_handler import build_prompt

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

origins = [
    "http://localhost",
    "http://localhost:3000",  # exemplo, se for um front-end em React
    # Adicione aqui os domínios autorizados
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    text: str
    mode: str = "resposta"
    model: str = "gpt-3.5-turbo"


@app.get("/health")
def health_check():
    return {"status": "ok"}


@limiter.limit("5/minute")
@app.post("/chat/")
def chat(request: PromptRequest, api_key: str = Depends(api_key_auth)):
    if request.mode not in SUPPORTED_MODES:
        return {"error": f"Modo '{request.mode}' não suportado"}
    if request.model not in SUPPORTED_MODELS:
        return {"error": f"Modelo '{request.model}' não suportado"}

    prompt = build_prompt(request.text, request.mode)
    response = call_chatgpt(prompt, model=request.model)
    return {"response": response}


@limiter.limit("5/minute")
@app.get("/limited/")
def limited_endpoint(request: Request):
    return {"message": "Esse endpoint é limitado a 5 requisições por minuto."}


@limiter.limit("5/minute")
@app.get("/secure-info/")
def secure_info(request: Request, api_key: str = Depends(api_key_auth)):
    return {"message": "Você acessou um endpoint protegido com API Key."}
