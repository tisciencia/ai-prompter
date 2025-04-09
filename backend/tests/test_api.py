import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.config import API_KEY


@pytest.mark.asyncio
async def test_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_chat_modo_nao_suportado():
    client = TestClient(app)
    headers = {"x-api-key": API_KEY}
    payload = {"text": "Olá", "mode": "modo_nao_suportado", "model": "gpt-3.5-turbo"}
    response = client.post("/chat/", headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json() == {"error": "Modo 'modo_nao_suportado' não suportado"}


@pytest.mark.asyncio
async def test_chat_modelo_nao_suportado():
    client = TestClient(app)
    headers = {"x-api-key": API_KEY}
    payload = {"text": "Olá", "mode": "traduzir", "model": "modelo_nao_suportado"}
    response = client.post("/chat/", headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json() == {"error": "Modelo 'modelo_nao_suportado' não suportado"}


@pytest.mark.asyncio
async def test_limited_endpoint():
    client = TestClient(app)
    response = client.get("/limited/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Esse endpoint é limitado a 5 requisições por minuto."
    }


@pytest.mark.asyncio
async def test_secure_info_endpoint():
    client = TestClient(app)
    headers = {"x-api-key": API_KEY}
    response = client.get("/secure-info/", headers=headers)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Você acessou um endpoint protegido com API Key."
    }
