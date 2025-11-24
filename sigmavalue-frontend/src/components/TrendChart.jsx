import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default function TrendChart({ data }) {
  if (!data || data.length === 0) {
    return (
      <div className="card h-100">
        <div className="card-body d-flex align-items-center justify-content-center text-muted">
          No chart data available for this query.
        </div>
      </div>
    );
  }

  const hasPrice = data.some((d) => d.price !== undefined && d.price !== null);
  const hasDemand = data.some((d) => d.demand !== undefined && d.demand !== null);

  return (
    <div className="card shadow-sm h-100">
      <div className="card-body">
        <h5 className="card-title mb-3">Trend Overview</h5>
        <div style={{ width: "100%", height: 260 }}>
          <ResponsiveContainer>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip />
              <Legend />
              {hasPrice && <Line type="monotone" dataKey="price" dot={false} />}
              {hasDemand && <Line type="monotone" dataKey="demand" dot={false} />}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
