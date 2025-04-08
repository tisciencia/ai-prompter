.PHONY: build up down api tui cli

# Constrói a imagem Docker a partir do Dockerfile presente no diretório backend
build:
	docker-compose build

# Inicia o container utilizando o docker-compose (modo API por padrão)
up:
	docker-compose up

# Para os containers iniciados pelo docker-compose
down:
	docker-compose down

# Executa a aplicação no modo API (FastAPI) através do comando "python run.py api"
api:
	docker-compose run app python run.py api

# Executa a aplicação no modo TUI (Terminal User Interface)
tui:
	docker-compose run app python run.py tui

# Executa a aplicação no modo CLI (Terminal interativo simples)
cli:
	docker-compose run app python run.py cli

# Executa black, isort, flake8 e mypy
lint:
	black backend/
	isort backend/
	flake8 backend/
	mypy backend/

 # Executa todos os hooks de pre-commit
precommit:
	pre-commit run --all-files

build-dev:
	docker compose -f docker-compose.yml -f docker-compose.override.yml build

up-dev:
	docker compose -f docker-compose.yml -f docker-compose.override.yml up
