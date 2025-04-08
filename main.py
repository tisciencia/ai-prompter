import os
from app.core import process_text, PROMPTS


def main():
    print("=== ChatGPT Text Processor ===")
    text = input("Digite o texto:\n> ")

    print("\nModos disponíveis:")
    for key in PROMPTS:
        print(f"- {key}")
    mode = input("Escolha o modo [traduzir]: ").strip() or "traduzir"

    model = input(f"Modelo [default: {os.getenv('OPENAI_API_MODEL')}]: ").strip() or os.getenv("OPENAI_API_MODEL")

    result = process_text(text, mode=mode, model=model)
    print("\n🔍 Resultado:\n", result)


if __name__ == "__main__":
    main()
