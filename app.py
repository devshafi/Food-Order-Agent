import gradio as gr
from react_langchain import agent

def chat(message, history):
    messages = history + [{"role": "user", "content": message}]
    result = agent.invoke({"messages": messages})
    return result["messages"][-1].content


gr.ChatInterface(
    chat,
    title="Restaurant Assistant",
    description="Ask me about the menu, check the weather, or place an order.",
).launch()
