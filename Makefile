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
	docker-compose exec app black /app
	docker-compose exec app isort /app
	docker-compose exec app flake8 /app
#	docker-compose exec app mypy /app

# Executa todos os hooks de pre-commit
precommit:
	docker-compose exec app pre-commit run --all-files

# Constrói a imagem Docker com as configurações de desenvolvimento
build-dev:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml build

# Inicia o container com as configurações de desenvolvimento
up-dev:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml up

# Executa os testes usando pytest
test:
	docker-compose exec app pytest tests

# Executa os testes com cobertura de código usando pytest-cov
test-cov:
	docker-compose exec app pytest --cov=app --cov-report=term-missing tests/