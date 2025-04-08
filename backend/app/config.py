import os
import logging
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEFAULT_MODEL = "gpt-3.5-turbo"
SUPPORTED_MODELS = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4-turbo",
]

DEFAULT_MODE = "resposta"
SUPPORTED_MODES = {
    "resposta": "Responda de forma clara e objetiva.",
    "traduzir": "Traduza o seguinte texto para português do Brasil.",
    "corrigir": "Corrija erros gramaticais e melhore a clareza do texto.",
    "reescrever": "Reescreva o texto para torná-lo mais natural e fluido.",
    "resumir": "Resuma o conteúdo a seguir mantendo os pontos principais.",
}

# API Key para autenticação via header
API_KEY = os.getenv("API_KEY")

# Configuração do logging: nível INFO e formato com data/hora
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)