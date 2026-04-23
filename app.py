import gradio as gr
from react_langchain import agent

PAYMENT_TRIGGER = "[READY_FOR_PAYMENT]"


def chat(message, history):
    messages = history + [{"role": "user", "content": message}]
    result = agent.invoke({"messages": messages})
    response = result["messages"][-1].content

    show_payment = PAYMENT_TRIGGER in response
    clean_response = response.replace(PAYMENT_TRIGGER, "").strip()

    new_history = messages + [{"role": "assistant", "content": clean_response}]
    return new_history, "", show_payment


def toggle_payment(show):
    return gr.update(visible=show)


def process_payment(card, exp, cv, history):
    if not all([card.strip(), exp.strip(), cv.strip()]):
        return (
            history,
            gr.update(value="⚠️ Please fill in all fields.", visible=True),
            gr.update(visible=True),
        )

    # Payment done — ask agent to now place the order via order_food tool
    messages = history + [{
        "role": "user",
        "content": "Payment has been completed successfully. Please now confirm and place the order using the order_food tool.",
    }]
    result = agent.invoke({"messages": messages})
    confirmation = result["messages"][-1].content
    new_history = messages + [{"role": "assistant", "content": confirmation}]

    return new_history, gr.update(visible=False), gr.update(visible=False)


with gr.Blocks() as demo:
    gr.Markdown("# 🍽️ Food Order Agent")
    gr.Markdown("Order Food Seamlessly")

    payment_state = gr.State(False)

    chatbot = gr.Chatbot(height=420)
    msg = gr.Textbox(placeholder="Type a message...", show_label=False)
    send_btn = gr.Button("Send", variant="primary")

    with gr.Group(visible=False) as payment_panel:
        gr.Markdown("---\n## 💳 Complete Your Payment")
        card_number = gr.Textbox(label="Card Number", placeholder="1234 5678 9012 3456")
        with gr.Row():
            expiry = gr.Textbox(label="Expiry", placeholder="MM/YY")
            cvv = gr.Textbox(label="CVV", placeholder="123", type="password")
        pay_btn = gr.Button("Pay Now", variant="primary")
        payment_result = gr.Markdown(visible=False)

    send_btn.click(
        chat,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg, payment_state],
    ).then(
        toggle_payment,
        inputs=[payment_state],
        outputs=[payment_panel],
    )
    msg.submit(
        chat,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg, payment_state],
    ).then(
        toggle_payment,
        inputs=[payment_state],
        outputs=[payment_panel],
    )
    pay_btn.click(
        process_payment,
        inputs=[card_number, expiry, cvv, chatbot],
        outputs=[chatbot, payment_result, payment_panel],
    )

demo.launch(css=".gradio-container { max-width: 720px !important; margin: auto !important; }")
