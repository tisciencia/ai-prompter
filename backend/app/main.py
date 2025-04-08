from app.prompt_handler import build_prompt
from app.chatgpt_client import call_chatgpt
from app.config import SUPPORTED_MODES, SUPPORTED_MODELS, DEFAULT_MODEL, DEFAULT_MODE


def run():
    print("🤖 ChatGPT CLI - Digite 'sair' para encerrar.")
    print("Modos disponíveis:", ", ".join(SUPPORTED_MODES.keys()))
    print("Modelos disponíveis:", ", ".join(SUPPORTED_MODELS))

    modo = input("Escolha o modo de uso: ").strip() or DEFAULT_MODE
    modelo = input("Escolha o modelo: ").strip() or DEFAULT_MODEL

    while True:
        user_input = input("Digite o texto: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            break
        prompt = build_prompt(user_input, modo)
        resposta = call_chatgpt(prompt, model=modelo)
        print(f"ChatGPT: {resposta}\n")
