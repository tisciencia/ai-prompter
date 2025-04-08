from app.core import process_text


def mock_openai_chatcompletion_create(**kwargs):
    class Choice:
        def __init__(self):
            self.message = {"content": "Texto corrigido."}
    return type("MockResponse", (), {"choices": [Choice()]})()


def test_process_text(monkeypatch):
    from app import core

    monkeypatch.setattr(core.openai.ChatCompletion, "create", mock_openai_chatcompletion_create)
    
    entrada = "eu fui no mercado ontem"
    saida = core.process_text(entrada)

    assert saida == "Texto corrigido."
