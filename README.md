# Food Order Agent

A conversational restaurant ordering agent built with LangChain, FastAPI, and React. Chat naturally to browse the menu, check nutrition, find a table, and place an order — with a simulated payment step before confirmation.

## Stack

| Layer | Tech |
|-------|------|
| LLM | Ollama (`gemma4:31b`) via LangChain |
| Backend | FastAPI |
| Frontend | React + Vite + Tailwind CSS |
| Legacy UI | Gradio (`app.py`) |

## Project Structure

```
Agents/
├── api.py               # FastAPI server (chat + payment endpoints)
├── react_langchain.py   # LangChain agent definition
├── app.py               # Gradio UI (fallback)
├── tools/
│   ├── db.py            # Menu items, prices, nutrition, tables data
│   └── restaurant.py    # LangChain tools (@tool decorated functions)
└── frontend/
    ├── src/
    │   ├── App.jsx      # Chat UI + inline payment card
    │   └── App.css      # Tailwind + typography imports
    ├── vite.config.js
    └── package.json
```

## Prerequisites

- Python 3.11+
- Node.js 18+
- [Ollama](https://ollama.com) running locally with `gemma4:31b` pulled

```bash
ollama pull gemma4:31b
```

## Setup

```bash
# Python deps (inside existing venv)
source .venv/bin/activate
pip install fastapi uvicorn langchain langchain-ollama gradio

# Frontend deps
cd frontend && npm install
```

## Running

**Terminal 1 — Backend:**
```bash
source .venv/bin/activate
uvicorn api:app --reload
# Runs on http://localhost:8000
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm run dev
# Opens http://localhost:5173
```

**Alternative — Gradio UI:**
```bash
source .venv/bin/activate
python app.py
# Opens http://localhost:7860
```

## Agent Tools

| Tool | Description |
|------|-------------|
| `search_menu` | Find menu items matching a keyword |
| `get_best_items` | Return the 2 best-selling items |
| `get_menu_with_prices` | List items with prices, filtered by category |
| `get_nutritional_info` | Calories, macros, and allergens for an item |
| `check_table_availability` | Show 2–3 available tables, optionally by party size |
| `order_food` | Place an order (called only after payment is confirmed) |

## Order Flow

```
1. User chats → browsing agent responds (cannot place orders)
2. User says "that's all" / "checkout" / "place my order"
3. Agent summarises order → payment card appears inline in chat
4. User enters card details → POST /pay
5. Ordering agent calls order_food → confirmation appears in chat
```

## API Endpoints

### `POST /chat`
```json
{ "message": "what pizzas do you have?", "history": [] }
```
Returns `{ "response", "ready_for_payment", "history" }`

### `POST /pay`
```json
{ "history": [...] }
```
Returns `{ "confirmation" }`
