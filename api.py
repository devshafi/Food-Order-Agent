from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from react_langchain import agent as ordering_agent
from tools import (
    search_menu,
    get_best_items,
    get_menu_with_prices,
    get_nutritional_info,
    check_table_availability,
)

PAYMENT_TRIGGER = "[READY_FOR_PAYMENT]"

# Browsing agent has NO order_food — it cannot place orders, only help browse
browsing_agent = create_agent(
    model=ChatOllama(model="gemma4:31b"),
    tools=[get_best_items, search_menu, get_menu_with_prices, get_nutritional_info, check_table_availability],
    system_prompt=(
        "You are a helpful restaurant order expert. Help customers browse the menu, "
        "answer questions, and build their order. Be concise and use emojis. "
        "When the customer explicitly says they are done selecting (e.g. 'that\\'s all', "
        "'place my order', 'checkout', 'I\\'m done', 'order it'), summarise exactly what "
        "they want and include the exact token [READY_FOR_PAYMENT] at the very end of your "
        "response. Do NOT place or confirm the order yourself — payment must happen first."
    ),
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    history: list


class PayRequest(BaseModel):
    history: list


@app.post("/chat")
def chat(req: ChatRequest):
    messages = req.history + [{"role": "user", "content": req.message}]
    result = browsing_agent.invoke({"messages": messages})
    response = result["messages"][-1].content
    ready_for_payment = PAYMENT_TRIGGER in response
    clean = response.replace(PAYMENT_TRIGGER, "").strip()
    new_history = messages + [{"role": "assistant", "content": clean}]
    return {"response": clean, "ready_for_payment": ready_for_payment, "history": new_history}


@app.post("/pay")
def pay(req: PayRequest):
    messages = req.history + [{
        "role": "user",
        "content": "Payment completed successfully. Please confirm and place the order now using the order_food tool.",
    }]
    result = ordering_agent.invoke({"messages": messages})
    confirmation = result["messages"][-1].content
    return {"confirmation": confirmation}
