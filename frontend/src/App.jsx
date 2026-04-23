import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkBreaks from "remark-breaks";

const AgentAvatar = () => (
  <div className="w-8 h-8 rounded-full bg-gradient-to-br from-orange-400 to-red-500 flex items-center justify-center flex-shrink-0 shadow-sm text-base">
    🍽️
  </div>
);

const UserAvatar = () => (
  <div className="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0 shadow-sm">
    <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24">
      <path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/>
    </svg>
  </div>
);

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
    <div className="min-h-screen bg-gradient-to-br from-orange-50 via-amber-50 to-red-50 flex items-center justify-center p-4">
    <div className="flex flex-col w-full max-w-2xl h-[90vh] bg-white rounded-2xl shadow-2xl overflow-hidden">

      {/* Header */}
      <header className="bg-gradient-to-r from-orange-500 to-red-500 px-6 py-4 shadow-md">
        <div className="flex flex-col items-center gap-1">
          <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-xl shadow-inner">
            🍽️
          </div>
          <h1 className="text-lg font-bold text-white tracking-tight">Food Order Agent</h1>
          <div className="flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-green-300 animate-pulse" />
            <span className="text-xs text-orange-100">Online</span>
          </div>
        </div>
      </header>

      {/* Chat */}
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-orange-300 gap-3 select-none">
            <span className="text-5xl">🍕</span>
            <p className="text-sm font-medium text-orange-400">Ask about the menu, prices, or place an order.</p>
          </div>
        )}

        {messages.map((m, i) => {
          if (m.role === "payment") {
            return (
              <div key={i} className="flex items-start gap-2">
                <AgentAvatar />
                <div className="bg-white border-2 border-orange-400 rounded-2xl rounded-tl-sm p-5 max-w-sm shadow-md space-y-3">
                  <p className="font-bold text-orange-500 text-sm">💳 Complete Payment</p>
                  <input
                    className="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm outline-none focus:border-orange-400 focus:ring-2 focus:ring-orange-100 transition"
                    placeholder="Card Number  1234 5678 9012 3456"
                    value={card}
                    onChange={(e) => setCard(e.target.value)}
                  />
                  <div className="flex gap-2 overflow-hidden">
                    <input
                      className="flex-1 min-w-0 border border-gray-200 rounded-lg px-3 py-2 text-sm outline-none focus:border-orange-400 focus:ring-2 focus:ring-orange-100 transition"
                      placeholder="MM/YY"
                      value={expiry}
                      onChange={(e) => setExpiry(e.target.value)}
                    />
                    <input
                      className="flex-1 min-w-0 border border-gray-200 rounded-lg px-3 py-2 text-sm outline-none focus:border-orange-400 focus:ring-2 focus:ring-orange-100 transition"
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
                    className="w-full bg-gradient-to-r from-orange-500 to-red-500 text-white text-sm font-semibold py-2.5 rounded-lg hover:from-orange-600 hover:to-red-600 disabled:opacity-40 transition cursor-pointer shadow-sm"
                  >
                    {paying ? "Processing…" : "Pay Now"}
                  </button>
                </div>
              </div>
            );
          }

          const isUser = m.role === "user";
          return (
            <div key={i} className={`flex items-end gap-2 ${isUser ? "flex-row-reverse" : "flex-row"}`}>
              {isUser ? <UserAvatar /> : <AgentAvatar />}
              <div className={`max-w-[72%] px-4 py-3 rounded-2xl text-sm leading-relaxed shadow-sm ${
                isUser
                  ? "bg-gradient-to-br from-indigo-500 to-purple-600 text-white rounded-br-sm whitespace-pre-wrap"
                  : "bg-white border border-orange-100 text-gray-800 rounded-bl-sm prose prose-sm max-w-none"
              }`}>
                {isUser ? m.content : <ReactMarkdown remarkPlugins={[remarkBreaks]}>{m.content}</ReactMarkdown>}
              </div>
            </div>
          );
        })}

        {loading && (
          <div className="flex items-end gap-2">
            <AgentAvatar />
            <div className="bg-white border border-orange-100 rounded-2xl rounded-bl-sm px-4 py-3 shadow-sm flex gap-1 items-center">
              <span className="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:0ms]" />
              <span className="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:150ms]" />
              <span className="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:300ms]" />
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="bg-white border-t border-orange-100 px-4 py-3 shadow-inner">
        <div className="flex gap-2 items-center">
          <input
            className="flex-1 bg-orange-50 border border-orange-200 rounded-xl px-4 py-2.5 text-sm outline-none focus:ring-2 focus:ring-orange-300 focus:border-orange-400 transition disabled:opacity-50 placeholder-gray-500 text-gray-800"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder={paymentPending ? "Complete payment above to continue…" : "Type a message…"}
            disabled={loading || paymentPending}
          />
          <button
            onClick={sendMessage}
            disabled={loading || !input.trim() || paymentPending}
            className="bg-gradient-to-r from-orange-500 to-red-500 text-white px-5 py-2.5 rounded-xl text-sm font-bold hover:from-orange-600 hover:to-red-600 disabled:opacity-50 transition cursor-pointer shadow-sm tracking-wide"
          >
            Send
          </button>
        </div>
      </div>
    </div>
    </div>
  );
}
