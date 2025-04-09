from typing import Optional

from fastapi import Header, HTTPException, status

from app.config import API_KEY


def api_key_auth(x_api_key: Optional[str] = Header(None)):
    """
    Verifica se a API Key enviada no header 'x-api-key' é válida.
    """
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida.",
            headers={"WWW-Authenticate": "API Key"},
        )
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida.",
            headers={"WWW-Authenticate": "API Key"},
        )
    return x_api_key
