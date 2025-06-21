"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [idea, setIdea] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    if (!idea.trim()) return;
    const res = await axios.post("http://localhost:8000/analyze", { idea });
    setResult(res.data.message);
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-start p-10">
      <h1 className="text-4xl font-bold mb-4 text-blue-600">StartupX</h1>
      <textarea
        className="w-full max-w-xl border border-gray-300 rounded-md p-3 mb-4 bg-white text-black"
        rows={5}
        placeholder="Describe your startup idea..."
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md"
      >
        Analyze
      </button>

      {result && (
        <div className="mt-6 max-w-xl bg-gray-100 p-4 rounded-md shadow-sm w-full text-left">
          <h2 className="font-semibold mb-2 text-lg">AI Analysis:</h2>
          <p className="text-gray-700">{result}</p>
        </div>
      )}
    </main>
  );
}