import pytest
from fastapi.testclient import TestClient
from api.server import app
from app import core


# Mock da OpenAI API
def mock_openai_chatcompletion_create(**kwargs):
    class Choice:
        def __init__(self):
            self.message = {"content": "Texto corrigido pela API."}
    return type("MockResponse", (), {"choices": [Choice()]})()


def test_api_process(monkeypatch):
    monkeypatch.setattr(core.openai.ChatCompletion, "create",
                        mock_openai_chatcompletion_create)

    client = TestClient(app)
    response = client.post("/process/",
                          json={"text": "eu fui no mercado ontem"})

    assert response.status_code == 200
    assert response.json()["response"] == "Texto corrigido pela API."
