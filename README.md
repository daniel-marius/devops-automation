# DevOps Automation

Python project demonstrating a basic DevOps pipeline and a FastAPI
service. The pipeline composes server and Docker-manager steps; these example
methods currently log the actions they represent rather than connecting to
servers or managing real containers. The API provides a status message and a
health-check endpoint.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup

From the project root, install the project and its development dependencies:

```bash
uv sync --locked --all-groups
```

## Run the pipeline example

Run the configured project command:

```bash
uv run devops-automation
```

The pipeline uses `INFO`-level logs. To display them in the terminal, configure
logging for this run:

```bash
uv run python -c "import logging; logging.basicConfig(level=logging.INFO); from devops_automation import main; main()"
```

## Run the API

Start the development server from the project root:

```bash
uv run uvicorn devops_automation.api:app --reload
```

The service is available at <http://127.0.0.1:8000>. Useful endpoints:

- `GET /` — service message
- `GET /health` — health status
- `/docs` — interactive API documentation

Stop the server with `Ctrl+C`.

## Quality checks

```bash
uv run ruff check .
uv run pytest -v
```