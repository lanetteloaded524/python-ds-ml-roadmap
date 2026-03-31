.PHONY: install install-all test validate clean docs serve-docs help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install core dependencies
	pip install -r requirements.txt

install-all: ## Install all dependencies (including dev tools)
	pip install -e ".[all]"

test: ## Run MLOps project tests
	cd projects/06_mlops_deployment && python train.py && pytest tests/ -v

validate: ## Validate all notebooks execute cleanly
	@for nb in projects/*/[!.]*.ipynb; do \
		echo "Validating $$nb..."; \
		jupyter nbconvert --to notebook --execute \
			--ExecutePreprocessor.timeout=300 \
			--output /dev/null "$$nb" 2>&1 && \
			echo "  ✅ Passed" || echo "  ❌ Failed"; \
	done

clean: ## Remove generated artifacts
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name ".ipynb_checkpoints" -type d -exec rm -rf {} + 2>/dev/null || true

docs: ## Build documentation site
	mkdocs build

serve-docs: ## Serve documentation locally
	mkdocs serve

lint: ## Run pre-commit hooks on all files
	pre-commit run --all-files

setup-dev: ## Set up development environment
	pip install -e ".[all]"
	pre-commit install
	nbstripout --install
	@echo "✅ Dev environment ready!"
