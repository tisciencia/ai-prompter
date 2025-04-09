from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Button, Input, Select, Static

from app.chatgpt_client import call_chatgpt
from app.config import SUPPORTED_MODELS, SUPPORTED_MODES
from app.prompt_handler import build_prompt


class ChatGPTTUI(App):
    # Define atalhos de teclado
    BINDINGS = [
        Binding("q", "quit", "Sair"),
        Binding("escape", "quit", "Sair"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("🤖 ChatGPT TUI")
        yield Select(
            options=[(m, m) for m in SUPPORTED_MODES], prompt="Modo:", id="mode"
        )
        yield Select(
            options=[(m, m) for m in SUPPORTED_MODELS], prompt="Modelo:", id="model"
        )
        yield Input(placeholder="Digite sua mensagem e pressione Enter")
        yield Button("Sair", variant="error", id="quit-button")

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        user_input = message.value.strip()
        if not user_input:
            return
        mode = self.query_one("#mode", Select).value
        model = self.query_one("#model", Select).value
        prompt = build_prompt(user_input, mode)
        response = call_chatgpt(prompt, model=model)
        await self.mount(Static(f"Você: {user_input}\nChatGPT: {response}\n"))

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit-button":
            self.exit()


def run_tui():
    app = ChatGPTTUI()
    app.run()
