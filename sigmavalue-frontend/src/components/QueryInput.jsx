import { useState } from "react";

export default function QueryInput({ onSubmit, loading }) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const trimmed = query.trim();
    if (!trimmed) return;
    onSubmit(trimmed);
  };

  const handleDemo = (text) => {
    setQuery(text);
    onSubmit(text);
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="d-flex gap-2">
        <input
          className="form-control"
          placeholder='Try: "Analyze Wakad price and demand from 2021 to 2024"'
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          disabled={loading}
        />
        <button className="btn btn-primary" disabled={loading}>
          {loading ? "Analyzing…" : "Send"}
        </button>
      </form>

      <div className="d-flex flex-wrap gap-2 mt-2">
        <button
          type="button"
          className="btn btn-sm btn-outline-secondary"
          onClick={() =>
            handleDemo("Analyze Wakad price and demand from 2021 to 2024")
          }
          disabled={loading}
        >
          Example 1
        </button>
        <button
          type="button"
          className="btn btn-sm btn-outline-secondary"
          onClick={() =>
            handleDemo("Compare Wakad and Aundh price trend for last 3 years")
          }
          disabled={loading}
        >
          Example 2
        </button>
      </div>
    </>
  );
}
