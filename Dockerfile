# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta da API
EXPOSE 8000

# Comando default (pode ser sobrescrito no docker-compose)
CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000"]
