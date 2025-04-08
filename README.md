# 🧠 GPT Text Processor

Aplicacao Python que utiliza a API da OpenAI para processar texto com multiplos prompts (ex: corrigir, traduzir, resumir, etc.), com suporte a:

- ✅ Terminal (TUI)
- ✅ FastAPI
- ✅ Varios modelos da OpenAI
- ✅ Prompt Manager interativo
- ✅ Docker + Docker Compose
- ✅ Testes automatizados com coverage

---

## 🚀 Como rodar

### 1. Ambiente local com `venv`

```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
```

Crie um `.env`:

```env
OPENAI_API_KEY=sk-...
OPENAI_API_MODEL=gpt-3.5-turbo
```

---

### 2. Executar via Terminal (TUI)

```bash
make tui
```

---

### 3. Executar API FastAPI

```bash
make api
# ou manualmente:
uvicorn api.server:app --reload
```

Acesse em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 4. Docker (API)

```bash
docker-compose up --build
```

---

## ✅ Testes

Execute os testes com:

```bash
make test
```

Gere o coverage:

```bash
make cov
```

Abra o relatorio:

```bash
open htmlcov/index.html  # no macOS/Linux
start htmlcov/index.html  # no Windows
```

---

## 📁 Estrutura do Projeto

```text
├── app/
│   ├── core.py            # Funcoes principais
│   └── prompts.yaml       # Prompts customizados
├── api/
│   └── server.py          # FastAPI server
├── tests/
│   └── test_api.py        # Testes automatizados
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Makefile
└── README.md
```

---

## ✨ Futuro (ideias)

- Cache de respostas
- Suporte a outras APIs (Claude, Mistral)
- Versao Web com Frontend

---

Feito com 💻 + ☕
