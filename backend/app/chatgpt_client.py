import logging

from openai import OpenAI

from app.config import DEFAULT_MODEL, OPENAI_API_KEY, SUPPORTED_MODELS

logger = logging.getLogger(__name__)

client = OpenAI(api_key=OPENAI_API_KEY)


def call_chatgpt(prompt: str, model: str = DEFAULT_MODEL) -> str:
    if model not in SUPPORTED_MODELS:
        raise ValueError(f"Modelo '{model}' não suportado.")

    logger.info("Chamando a API do ChatGPT com o modelo '%s'", model)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt},
            ],
        )
        resposta = response.choices[0].message.content.strip()
        logger.info("Recebida resposta da API com sucesso")
        return resposta
    except Exception as e:
        logger.exception("Erro ao chamar a API do ChatGPT: %s", str(e))
        return f"Erro ao chamar a API: {str(e)}"
