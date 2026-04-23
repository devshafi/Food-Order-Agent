from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from tools import (
    search_menu,
    get_best_items,
    get_menu_with_prices,
    get_nutritional_info,
    check_table_availability,
    order_food,
)

model = ChatOllama(model="gemma4:31b")

agent = create_agent(
    model=model,
    tools=[
        get_best_items,
        search_menu,
        get_menu_with_prices,
        get_nutritional_info,
        check_table_availability,
        order_food,
    ],
    system_prompt=(
        "You are a helpful restaurant order expert. Help customers browse the menu, "
        "answer questions, and build their order. Be concise and use emojis. "
        "When the customer explicitly says they are done selecting (e.g. 'that\\'s all', "
        "'place my order', 'checkout', 'I\\'m done', 'order it'), summarise what they want "
        "and include the exact token [READY_FOR_PAYMENT] at the very end of your response. "
        "Do NOT call order_food yet — wait until the system confirms payment, then call "
        "order_food for each item the customer ordered."
    ),
)

if __name__ == "__main__":
    messages = []

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_input})
        result = agent.invoke({"messages": messages})

        messages = result["messages"]
        print(messages[-1].content)
