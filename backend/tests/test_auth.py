import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.config import API_KEY


@pytest.mark.asyncio
async def test_reject_request_without_api_key():
    client = TestClient(app)
    payload = {"text": "Olá", "mode": "traduzir", "model": "gpt-3.5-turbo"}
    response = client.post("/chat/", json=payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "API Key inválida."


@pytest.mark.asyncio
async def test_accept_request_with_valid_api_key():
    client = TestClient(app)
    headers = {"x-api-key": API_KEY}
    payload = {"text": "Olá mundo", "mode": "traduzir", "model": "gpt-3.5-turbo"}

    response = client.post("/chat/", headers=headers, json=payload)

    # A resposta será 200 se a chave for válida e a API da OpenAI estiver respondendo
    # 422 se payload inválido, 400 se erro de parsing
    assert response.status_code in [200, 400, 422]


@pytest.mark.asyncio
async def test_reject_request_with_invalid_api_key():
    client = TestClient(app)
    headers = {"x-api-key": "chave_invalida"}
    payload = {"text": "Olá", "mode": "traduzir", "model": "gpt-3.5-turbo"}
    response = client.post("/chat/", headers=headers, json=payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "API Key inválida."
