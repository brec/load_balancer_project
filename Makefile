SHELL := /bin/bash

VENV := .VENV

PYTHON := python3

.PHONY: venv install dev-install pre-commit

venv:
	@if [ ! -d "$(VENV)" ]; then \
		$(PYTHON) -m venv $(VENV); \
		echo "Virtual environment created in $(VENV)"; \
	else \
		echo "Virtual environment already exists in $(VENV)"; \
	fi

install: venv
	. $(VENV)/bin/activate && pip install --upgrade pip
	. $(VENV)/bin/activate && pip install -r requirements.txt

dev-install: venv
	. $(VENV)/bin/activate && pip install --upgrade pip
	. $(VENV)/bin/activate && pip install -r requirements-dev.txt

pre-commit:
	. $(VENV)/bin/activate && pre-commit run --all-files
