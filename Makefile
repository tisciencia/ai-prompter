# Variáveis
IMAGE_NAME=chatgpt_app
SERVICE_NAME=app

# Build da imagem Docker
build:
	docker-compose build

# Sobe a API com Docker Compose
up:
	docker-compose up

# Derruba os containers
down:
	docker-compose down

# Roda a TUI no terminal
tui:
	docker-compose run --rm $(SERVICE_NAME) python main.py

# Roda a API no terminal
run-api:
	docker-compose run --rm $(SERVICE_NAME) uvicorn api.server:app --reload

# Acessa o bash do container (útil para debug)
bash:
	docker-compose run --rm $(SERVICE_NAME) bash

# Remove imagens/containers/paradas
clean:
	docker system prune -af

# Roda os testes
test:
	docker-compose run --rm $(SERVICE_NAME) pytest

# Testes com coverage
cov:
	docker-compose run --rm $(SERVICE_NAME) coverage run --source=app --fail-under=80 -m pytest

# Relatório no terminal
cov-report:
	docker-compose run --rm $(SERVICE_NAME) coverage report -m

# Relatório em HTML (abre o index.html em /htmlcov)
cov-html:
	docker-compose run --rm $(SERVICE_NAME) coverage html