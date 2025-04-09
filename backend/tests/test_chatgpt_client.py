from unittest.mock import patch

import pytest

from app.chatgpt_client import call_chatgpt
from app.prompt_handler import build_prompt


@pytest.mark.asyncio
async def test_call_chatgpt():
    prompt = build_prompt("Olá mundo", "traduzir")
    result = call_chatgpt(prompt)
    assert result is not None
    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_call_chatgpt_modelo_nao_suportado():
    with pytest.raises(ValueError) as excinfo:
        call_chatgpt("Olá mundo", model="modelo_nao_suportado")
    assert "Modelo 'modelo_nao_suportado' não suportado" in str(excinfo.value)


@pytest.mark.asyncio
async def test_call_chatgpt_erro_api():
    with patch("app.chatgpt_client.client.chat.completions.create") as mock_create:
        mock_create.side_effect = Exception("Erro simulado na API")
        result = call_chatgpt("Olá mundo")
        assert result.startswith("Erro ao chamar a API:")
