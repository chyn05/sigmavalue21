import { useState } from "react";
import QueryInput from "./QueryInput";
import SummaryCard from "./SummaryCard";
import TrendChart from "./TrendChart";
import DataTable from "./DataTable";
import { analyzeQuery } from "../api/client";

export default function ChatPage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [response, setResponse] = useState(null);
  const [lastQuery, setLastQuery] = useState("");

  const handleSubmit = async (query) => {
    setLoading(true);
    setError("");
    setLastQuery(query);
    try {
      const data = await analyzeQuery(query);
      setResponse(data);
    } catch (err) {
      console.error(err);
      setError(
        err?.response?.data?.error ||
          "Something went wrong while contacting the server."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container py-4">
      <header className="mb-4">
        <h2 className="fw-bold mb-1">Sigmavalue Real Estate Assistant</h2>
        <p className="text-muted mb-0">
          Ask questions like{" "}
          <code>“Analyze Wakad price and demand from 2021 to 2024”</code> and
          get insights.
        </p>
      </header>

      <QueryInput onSubmit={handleSubmit} loading={loading} />

      {error && (
        <div className="alert alert-danger mt-3" role="alert">
          {error}
        </div>
      )}

      {loading && (
        <div className="mt-3">
          <span className="spinner-border spinner-border-sm me-2" />
          <span className="text-muted">Analyzing your query…</span>
        </div>
      )}

      {response && !loading && (
        <section className="mt-4">
          <SummaryCard text={response.summary} query={lastQuery} />
          <div className="row mt-3 g-3">
            <div className="col-md-6">
              <TrendChart data={response.chartData} />
            </div>
            <div className="col-md-6">
              <DataTable rows={response.tableData} />
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
