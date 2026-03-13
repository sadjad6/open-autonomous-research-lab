.PHONY: install dev test lint format typecheck run-api run-ui docker clean help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	uv sync

dev: ## Install all dependencies including dev tools
	uv sync --extra dev
	uv run pre-commit install

test: ## Run the test suite
	uv run pytest tests/ -v --tb=short

test-cov: ## Run tests with coverage
	uv run pytest tests/ -v --cov=src --cov-report=term-missing

lint: ## Run linter
	uv run ruff check src/ tests/

format: ## Auto-format code
	uv run ruff format src/ tests/

typecheck: ## Run type checker
	uv run mypy src/ --ignore-missing-imports

run-api: ## Start the REST API server
	uv run uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

run-ui: ## Start the Streamlit UI
	uv run streamlit run src/ui/app.py --server.port 8501

docker: ## Build Docker image
	docker build -t oarl:latest .

docker-up: ## Start all services via Docker Compose
	docker compose up -d

docker-down: ## Stop all services
	docker compose down

clean: ## Remove build artifacts and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf dist/ build/ *.egg-info

synth-data: ## Generate synthetic datasets
	uv run python -m synthetic_data.generator
