export default function DataTable({ rows }) {
  if (!rows || rows.length === 0) {
    return (
      <div className="card h-100">
        <div className="card-body d-flex align-items-center justify-content-center text-muted">
          No detailed rows for this query.
        </div>
      </div>
    );
  }

  const columns = Object.keys(rows[0]);

  return (
    <div className="card shadow-sm h-100">
      <div className="card-body d-flex flex-column">
        <div className="d-flex justify-content-between align-items-center mb-2">
          <h5 className="card-title mb-0">Filtered Dataset</h5>
          <span className="badge bg-secondary">
            {rows.length} row{rows.length !== 1 ? "s" : ""}
          </span>
        </div>

        <div className="table-responsive" style={{ maxHeight: 260 }}>
          <table className="table table-sm table-striped mb-0 align-middle">
            <thead className="table-light sticky-top">
              <tr>
                {columns.map((col) => (
                  <th key={col} className="text-capitalize">
                    {col.replace(/_/g, " ")}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row, idx) => (
                <tr key={idx}>
                  {columns.map((col) => (
                    <td key={col}>
                      {row[col] !== null && row[col] !== undefined
                        ? row[col].toString()
                        : "-"}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <p className="text-muted small mt-2 mb-0">
          Scroll to inspect individual records. Use this to validate calculations
          and explore outliers.
        </p>
      </div>
    </div>
  );
}
