import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.api import app
from app.config import API_KEY


@pytest.mark.asyncio
async def test_chat_modes():
    client = TestClient(app)
    headers = {"x-api-key": API_KEY}
    payload = {
        "text": "Corrija este texto por favor",
        "mode": "corrigir",
        "model": "gpt-3.5-turbo"
    }

    with patch("app.api.call_chatgpt") as mock_call:
        mock_call.return_value = "Texto corrigido mockado"
        
        response = client.post(
            "/chat/",
            headers=headers,
            json=payload
        )
        
        assert response.status_code == 200
        assert response.json()["response"] == "Texto corrigido mockado"
