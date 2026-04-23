import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkBreaks from "remark-breaks";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [history, setHistory] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [card, setCard] = useState("");
  const [expiry, setExpiry] = useState("");
  const [cvv, setCvv] = useState("");
  const [payError, setPayError] = useState("");
  const [paying, setPaying] = useState(false);
  const bottomRef = useRef(null);

  const paymentPending = messages.some((m) => m.role === "payment");

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  async function sendMessage() {
    const text = input.trim();
    if (!text || loading || paymentPending) return;
    setInput("");
    setLoading(true);
    const nextMessages = [...messages, { role: "user", content: text }];
    setMessages(nextMessages);

    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, history }),
    });
    const data = await res.json();
    const withResponse = [...nextMessages, { role: "assistant", content: data.response }];
    setHistory(data.history);
    setMessages(data.ready_for_payment ? [...withResponse, { role: "payment" }] : withResponse);
    setLoading(false);
  }

  async function submitPayment() {
    if (!card.trim() || !expiry.trim() || !cvv.trim()) {
      setPayError("Please fill in all fields.");
      return;
    }
    setPayError("");
    setPaying(true);

    const res = await fetch("/pay", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ history }),
    });
    const data = await res.json();
    setMessages((prev) => [
      ...prev.filter((m) => m.role !== "payment"),
      { role: "assistant", content: data.confirmation },
    ]);
    setCard(""); setExpiry(""); setCvv("");
    setPaying(false);
  }

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-4 flex items-center gap-3 shadow-sm">
        <div className="text-2xl">🍽️</div>
        <div>
          <h1 className="text-lg font-semibold text-gray-900">Food Order Agent</h1>
          <p className="text-xs text-gray-400">Order food seamlessly</p>
        </div>
      </header>

      {/* Chat */}
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-3 max-w-2xl w-full mx-auto">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-gray-400 gap-2 select-none">
            <span className="text-4xl">🍕</span>
            <p className="text-sm">Ask about the menu, prices, or place an order.</p>
          </div>
        )}

        {messages.map((m, i) => {
          if (m.role === "payment") {
            return (
              <div key={i} className="bg-white border-2 border-gray-900 rounded-2xl rounded-bl-sm p-5 max-w-sm shadow-sm space-y-3">
                <p className="font-semibold text-gray-900 text-sm">💳 Complete Payment</p>
                <input
                  className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm outline-none focus:border-gray-900 transition"
                  placeholder="Card Number  1234 5678 9012 3456"
                  value={card}
                  onChange={(e) => setCard(e.target.value)}
                />
                <div className="flex gap-2 overflow-hidden">
                  <input
                    className="flex-1 min-w-0 border border-gray-300 rounded-lg px-3 py-2 text-sm outline-none focus:border-gray-900 transition"
                    placeholder="MM/YY"
                    value={expiry}
                    onChange={(e) => setExpiry(e.target.value)}
                  />
                  <input
                    className="flex-1 min-w-0 border border-gray-300 rounded-lg px-3 py-2 text-sm outline-none focus:border-gray-900 transition"
                    placeholder="CVV"
                    type="password"
                    value={cvv}
                    onChange={(e) => setCvv(e.target.value)}
                  />
                </div>
                {payError && <p className="text-red-500 text-xs">{payError}</p>}
                <button
                  onClick={submitPayment}
                  disabled={paying}
                  className="w-full bg-gray-900 text-white text-sm font-medium py-2.5 rounded-lg hover:bg-gray-700 disabled:opacity-40 transition cursor-pointer"
                >
                  {paying ? "Processing…" : "Pay Now"}
                </button>
              </div>
            );
          }

          const isUser = m.role === "user";
          return (
            <div key={i} className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
              <div className={`max-w-[75%] px-4 py-2.5 rounded-2xl text-sm leading-relaxed ${
                isUser
                  ? "bg-gray-900 text-white rounded-br-sm whitespace-pre-wrap"
                  : "bg-white border border-gray-200 text-gray-800 rounded-bl-sm shadow-sm prose prose-sm max-w-none"
              }`}>
                {isUser ? m.content : <ReactMarkdown remarkPlugins={[remarkBreaks]}>{m.content}</ReactMarkdown>}
              </div>
            </div>
          );
        })}

        {loading && (
          <div className="flex justify-start">
            <div className="bg-white border border-gray-200 rounded-2xl rounded-bl-sm px-4 py-2.5 shadow-sm flex gap-1 items-center">
              <span className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce [animation-delay:0ms]" />
              <span className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce [animation-delay:150ms]" />
              <span className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce [animation-delay:300ms]" />
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="bg-white border-t border-gray-200 px-4 py-3">
        <div className="max-w-2xl mx-auto flex gap-2 items-center">
          <input
            className="flex-1 bg-gray-100 rounded-xl px-4 py-2.5 text-sm outline-none focus:ring-2 focus:ring-gray-900 transition disabled:opacity-50"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder={paymentPending ? "Complete payment above to continue…" : "Type a message…"}
            disabled={loading || paymentPending}
          />
          <button
            onClick={sendMessage}
            disabled={loading || !input.trim() || paymentPending}
            className="bg-gray-900 text-white px-5 py-2.5 rounded-xl text-sm font-medium hover:bg-gray-700 disabled:opacity-40 transition cursor-pointer"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
