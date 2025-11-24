export default function SummaryCard({ text, query }) {
  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h5 className="card-title mb-1">Analysis Summary</h5>
        {query && (
          <p className="text-muted small mb-2">
            Based on your query: <code>{query}</code>
          </p>
        )}
        <p className="card-text mb-0">{text}</p>
      </div>
    </div>
  );
}
