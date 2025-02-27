SHELL := /bin/zsh

VENV := .venv

PYTHON := python
PIP := $(VENV)/bin/pip

.PHONY: all
all: help

# Show helpful usage info
.PHONY: help
help:
	@echo "Common make targets:"
	@echo "  make venv        Create/upgrade the virtual environment"
	@echo "  make install     Install dependencies from requirements.txt"
	@echo "  make dev-install Install dev/testing deps from requirements-dev.txt"
	@echo "  make pre-commit  Run pre-commit checks on all files"
	@echo "  make clean       Remove venv and any __pycache__ directories"

.PHONY: venv
venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment in $(VENV)"; \
		$(PYTHON) -m venv $(VENV); \
	fi
	@echo "Upgrading pip in $(VENV)..."
	@$(PIP) install --upgrade pip

.PHONY: install
install: venv
	@echo "Installing dependencies..."
	@$(PIP) install -r requirements.txt

.PHONY: dev-install
dev-install: install
	@echo "Installing dev/test dependencies..."
	@$(PIP) install -r requirements-dev.txt

.PHONY: pre-commit
pre-commit: venv
	@pre-commit run --all-files

.PHONY: clean
clean:
	@echo "Removing virtual environment and __pycache__..."
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +

