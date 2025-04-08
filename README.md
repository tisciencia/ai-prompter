# ChatGPT App

Uma aplicação em Python que integra o ChatGPT via API da OpenAI, preparada para ser utilizada em diversos modos: CLI, TUI e FastAPI. O projeto foi desenvolvido seguindo boas práticas de engenharia de código, organização modular, logging, segurança utilizando autenticação por API Key e suporte a linters, testes e pre-commit hooks.

## Tabela de Conteúdos

- [ChatGPT App](#chatgpt-app)
  - [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [Recursos](#recursos)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Uso](#uso)
    - [Modo CLI](#modo-cli)
    - [Modo TUI](#modo-tui)
    - [Modo API (FastAPI)](#modo-api-fastapi)
  - [Autenticação por API Key](#autenticação-por-api-key)
  - [Docker e Docker Compose](#docker-e-docker-compose)
  - [Qualidade e Validação de Código](#qualidade-e-validação-de-código)
    - [Executar manualmente:](#executar-manualmente)
  - [Testes](#testes)
    - [Executar testes:](#executar-testes)
    - [Estrutura de testes:](#estrutura-de-testes)
  - [Melhorias e Futuras Atualizações](#melhorias-e-futuras-atualizações)
  - [Licença](#licença)

## Recursos

- Integração com a API OpenAI (OpenAI >= 1.0.0)
- Suporte a múltiplos modelos (ex.: `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`)
- Modos customizados: `resposta`, `traduzir`, `corrigir`, `reescrever`, `resumir`
- Múltiplas interfaces:
  - **CLI** (linha de comando simples)
  - **TUI** (Terminal User Interface com `Textual`)
  - **API** usando FastAPI
- Logging estruturado e camada de segurança com autenticação via API Key
- Arquivos de configuração para ambiente e deploy com Docker e Docker Compose
- Suporte a linters, testes automatizados, verificação de tipos e hooks de pre-commit

## Estrutura do Projeto

```
backend/
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── auth.py
│   ├── chatgpt_client.py
│   ├── config.py
│   ├── main.py
│   ├── prompt_handler.py
│   └── tui.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
├── .env
├── .flake8
├── mypy.ini
├── pyproject.toml
├── .pre-commit-config.yaml
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

## Pré-requisitos

- Python 3.9 ou superior
- Docker e Docker Compose (opcional, para deploy containerizado)
- Ambiente virtual (recomendado para instalação local)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd <nome_do_repositório>
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r backend/requirements.txt
   pip install -r backend/requirements-dev.txt
   ```

4. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` no diretório `backend/` com o seguinte conteúdo:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   API_KEY=your-api-key-para-autenticacao
   ```

5. **Configure os hooks de pre-commit:**

   ```bash
   pre-commit install
   ```

## Uso

O projeto suporta três modos de execução:

### Modo CLI

```bash
python backend/run.py cli
```

### Modo TUI

```bash
python backend/run.py tui
```

### Modo API (FastAPI)

```bash
python backend/run.py api
```

## Autenticação por API Key

Utilize o header `x-api-key` para acessar os endpoints da API:

```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-api-key-para-autenticacao" \
  -d '{"text": "Texto de exemplo", "mode": "reescrever", "model": "gpt-3.5-turbo"}'
```

## Docker e Docker Compose

```bash
make build     # Constrói a imagem
make up        # Sobe a aplicação em modo API
make api       # Executa API localmente
make tui       # Executa o modo TUI
make cli       # Executa o modo CLI
make down      # Encerra os containers
```

Para ambiente de desenvolvimento (com requirements-dev):

```bash
make build     # Constrói com Dockerfile (requirements-dev.txt se ENV=dev)
make up        # Inicia a API com reload e mounts locais
```

## Qualidade e Validação de Código

O projeto utiliza os seguintes validadores:

- `black`: formatação de código
- `isort`: organização de imports
- `flake8`: validação de estilo
- `mypy`: verificação de tipos estáticos
- `pre-commit`: ganchos automáticos de validação

### Executar manualmente:

```bash
make lint         # Executa black, isort, flake8 e mypy
make precommit    # Executa todos os hooks de pre-commit
```

## Testes

O projeto usa `pytest` e `httpx` para testar endpoints da API e lógica de negócio.

### Executar testes:

```bash
make test
```

### Estrutura de testes:

- `tests/conftest.py`: fixtures e configurações globais
- `tests/test_api.py`: testes para a API FastAPI

## Melhorias e Futuras Atualizações

- Testes automatizados com cobertura (`pytest-cov`)
- Autenticação JWT para múltiplos usuários
- Execução assíncrona e otimizações
- Frontend Web com React

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

