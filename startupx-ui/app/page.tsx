'use client';

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [idea, setIdea] = useState("");
  const [competitors, setCompetitors] = useState([]);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [tags, setTags] = useState<string[]>([]);
  const [readinessScore, setReadinessScore] = useState<number | null>(null);
  const [personas, setPersonas] = useState([]);

  const handleSubmit = async () => {
    if (!idea.trim()) {
      alert("Please enter a startup idea first!");
      return;
    }
  
    setLoading(true);
    setError(null);
    setCompetitors([]); // reset previous results
  
    try {
      const res = await axios.post("http://127.0.0.1:8000/evaluate_idea", { idea });
      setTags(res.data.tags || []);
      setReadinessScore(res.data.readiness || null);
      
      if (res.data.personas && res.data.personas.length > 0) {
        setPersonas(res.data.personas);
      }
  
      if (res.data.competitors && res.data.competitors.length > 0) {
        setCompetitors(res.data.competitors);
      } else {
        setError("No competitors found for this idea."); // No competitors returned
      }
    } catch (err) {
      console.error("Error:", err);
      setError("Something went wrong. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  const Spinner = () => (
    <div className="mt-4 text-white text-center animate-pulse">
      Evaluating your idea...
    </div>
  );

  const getReadinessColor = (score: number) => {
    if (score <= 3) return "bg-green-500";
    if (score <= 7) return "bg-yellow-500";
    return "bg-red-500";
  };

  const getReadinessTooltip = (score: number) => {
    if (score <= 3) return "Low saturation — Unique market opportunity ✅";
    if (score <= 7) return "Moderate saturation — Some competition ⚠️";
    return "High saturation — Competitive space 🔥";
  };
  

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4 bg-black text-white">
      <h1 className="text-3xl font-bold mb-6">StartupX 🚀</h1>

      <div className="w-full max-w-md mb-6">
        <input
          type="text"
          placeholder="Enter your startup idea"
          value={idea}
          onChange={(e) => setIdea(e.target.value)}
          className="w-full p-3 bg-gray-900 text-white border border-gray-700 rounded mb-2 placeholder-gray-400"
        />
        <button
          onClick={handleSubmit}
          disabled={loading}
          className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? "Evaluating..." : "Evaluate Idea"}
        </button>
      </div>
      {error && (
        <p className="text-red-500 mt-4 text-center">{error}</p>
      )}

      {readinessScore !== null && (
        <div className="w-full max-w-md mt-6">
          <p className="text-white mb-2 text-center font-medium">
            🧭 Market Readiness Score: <span className="font-bold">{readinessScore}/10</span>
          </p>

          <div className="relative group">
            {/* Progress Bar Container */}
            <div className="w-full bg-gray-700 rounded-full h-5 overflow-hidden">
              <div
                className={`${getReadinessColor(readinessScore)} h-5 transition-all duration-500`}
                style={{ width: `${readinessScore * 10}%` }}
              ></div>
            </div>

            {/* Tooltip */}
            <div className="absolute top-full left-1/2 transform -translate-x-1/2 mt-2 w-max bg-gray-800 text-white text-sm px-3 py-1 rounded shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-10">
              {getReadinessTooltip(readinessScore)}
            </div>
          </div>
        </div>
      )}


      {tags.length > 0 && (
    <div className="flex flex-wrap gap-2 mt-6 justify-center">
      {tags.map((tag, idx) => (
        <span
          key={idx}
          className="bg-blue-700 text-white px-3 py-1 rounded-full text-sm shadow transition-transform duration-300 hover:scale-105"
        >
          {tag}
        </span>
      ))}
    </div>
  )}

      <div className="w-full max-w-2xl grid grid-cols-1 md:grid-cols-2 gap-4">
        {competitors.map((comp: any, idx: number) => (
          <div
          key={idx}
          className="bg-gray-800 p-4 shadow rounded border border-gray-700 animate-fade-in-up"
        >
          <h2 className="text-xl font-semibold mb-2">{comp.name}</h2>
          <p className="text-gray-300 mb-2">{comp.description}</p>
          <a
            href={comp.url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:underline"
          >
            View on ProductHunt
          </a>
        </div>        
        ))}
      </div>

      {personas.length > 0 && (
        <div className="mt-10 w-full max-w-3xl">
          <h2 className="text-2xl font-bold mb-4 text-center">🎯 Target Personas</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {personas.map((p: any, idx: number) => (
              <div key={idx} className="bg-gray-800 p-4 rounded shadow border border-gray-700">
                <h3 className="text-lg font-semibold mb-2">
                  {p.name}, {p.age} – {p.occupation}
                </h3>
                <p><strong>Goals:</strong> {p.goals}</p>
                <p><strong>Pain Points:</strong> {p.pain_points}</p>
                <p><strong>How Product Helps:</strong> {p.how_product_helps}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ✅ Show error if any */}
      {error && (
        <p className="text-red-400 text-center mt-6">
          ⚠️ Something went wrong. Please try again later.
        </p>
      )}
    </main>
  );
}

