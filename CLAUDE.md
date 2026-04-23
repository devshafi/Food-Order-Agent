# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

Activate the existing virtual environment before running anything:

```bash
source .venv/bin/activate
```

Ollama must be running locally with the `gemma4:31b` model pulled:

```bash
ollama pull gemma4:31b
```

To add new dependencies:

```bash
pip install <package>
```

There is no `requirements.txt` or `pyproject.toml` — dependencies live only in `.venv`.

## Running

**Gradio web UI:**

```bash
python app.py
# Opens http://localhost:7860
```

**CLI REPL (terminal only):**

```bash
python react_langchain.py
```

## Architecture

A LangChain/LangGraph restaurant ordering agent with a Gradio frontend.

### `react_langchain.py` — agent definition

Uses `ChatOllama` with `gemma4:31b` and LangChain's `@tool` decorator. Exposes three tools: `search_menu`, `get_weather`, `order_food`. The `agent` object is created at module level so it can be imported. The CLI REPL loop is guarded by `if __name__ == "__main__":`.

### `app.py` — Gradio frontend

Imports `agent` from `react_langchain` and wraps it in `gr.ChatInterface`. Gradio 6 passes history as `{"role", "content"}` dicts, which is directly compatible with LangChain's message format — no conversion needed.

### Key pattern: stateful message history

Each turn reconstructs the full message list from Gradio's history plus the new user message, then passes it to `agent.invoke({"messages": messages})`.
