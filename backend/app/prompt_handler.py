from app.config import SUPPORTED_MODES


def build_prompt(user_input: str, mode: str = "resposta") -> str:
    mode_prompt = SUPPORTED_MODES.get(mode, SUPPORTED_MODES["resposta"])
    return f"{mode_prompt}\n\n{user_input}"
