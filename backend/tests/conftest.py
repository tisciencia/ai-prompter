import pytest
from fastapi.testclient import TestClient
from app.api import app
from unittest.mock import AsyncMock, patch


@pytest.fixture
def async_client():
    return TestClient(app)


@pytest.fixture
def mock_openai():
    with patch("app.chatgpt_client.openai.ChatCompletion.acreate", new_callable=AsyncMock) as mock:
        mock.return_value = {
            "choices": [{"message": {"content": "Texto corrigido mockado"}}]
        }
        yield mock
