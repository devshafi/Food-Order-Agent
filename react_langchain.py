from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from tools import search_menu, get_weather, order_food

model = ChatOllama(model="gemma4:31b")

agent = create_agent(
    model=model,
    tools=[get_weather, search_menu, order_food],
    system_prompt="You are a helpful restaurant order expert. Assist customers with menu recommendations, orders, and dining inquiries. Be concise and accurate.",
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
