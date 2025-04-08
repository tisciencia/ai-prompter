import openai
import os
import yaml

DEFAULT_MODEL = os.getenv("OPENAI_API_MODEL", "gpt-3.5-turbo")

# Carrega os prompts do arquivo YAML
with open("app/prompts.yaml", "r", encoding="utf-8") as f:
    PROMPTS = yaml.safe_load(f)


def process_text(text: str, mode: str = "corrigir", model: str = DEFAULT_MODEL) -> str:
    if mode not in PROMPTS:
        raise ValueError(f"Modo inválido: {mode}. Modos disponíveis: {list(PROMPTS.keys())}")

    system_prompt = PROMPTS.get(mode, PROMPTS["corrigir"])

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message["content"]
