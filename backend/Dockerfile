# Imagem base com Python (versão leve)
FROM python:3.9-slim

# Instala dependências do sistema se necessário (por exemplo, gcc para compilações nativas)
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o restante do código da aplicação
COPY . .

# Define a variável de ambiente para ambiente padrão
ARG ENV=prod
ENV ENV=${ENV}

# Instala as dependências com base no ambiente
RUN pip install --upgrade pip && \
    if [ "$ENV" = "dev" ]; then \
        pip install -r requirements-dev.txt; \
    else \
        pip install -r requirements.txt; \
    fi

# Expõe a porta usada pela FastAPI (modo API)
EXPOSE 8000

# Comando padrão: executa a aplicação no modo API com uvicorn
CMD ["python", "run.py", "api"]
