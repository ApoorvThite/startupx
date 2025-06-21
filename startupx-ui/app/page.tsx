"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [idea, setIdea] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!idea) return;
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/evaluate_idea", {
        idea,
      });
      setResponse(res.data.response || "No response received.");
    } catch (err) {
      setResponse("Error contacting backend.");
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <main style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>StartupX: Idea Evaluator</h1>

      <textarea
        rows={4}
        style={{ width: "100%", padding: "1rem", fontSize: "1rem" }}
        placeholder="Describe your startup idea..."
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
      />

      <button
        style={{
          marginTop: "1rem",
          padding: "0.75rem 1.5rem",
          fontSize: "1rem",
          background: "#0070f3",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Evaluating..." : "Evaluate Idea"}
      </button>

      <div style={{ marginTop: "2rem", whiteSpace: "pre-wrap" }}>
        {response && (
          <>
            <h3>📊 Evaluation Result:</h3>
            <p>{response}</p>
          </>
        )}
      </div>
    </main>
  );
}

