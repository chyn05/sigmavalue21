from typing import Tuple, List, Dict, Any
from .excel_loader import load_dataset, filter_by_area

def compute_trends(areas: List[str], metric: str, year_range: Tuple[int | None, int | None] = (None, None)) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    df = load_dataset()
    if areas:
        df = filter_by_area(df, areas)
    start, end = year_range
    if "year" in df.columns and start is not None and end is not None:
        df = df[(df["year"] >= start) & (df["year"] <= end)]
    table_data = df.to_dict(orient="records")
    if df.empty:
        return [], []
    agg_map = {}
    if metric in ("price", "both") and "price" in df.columns:
        agg_map["price"] = "mean"
    if metric in ("demand", "both") and "demand" in df.columns:
        agg_map["demand"] = "mean"
    if not agg_map:
        return [], table_data
    if "year" in df.columns:
        group_cols = ["year"]
    else:
        group_cols = []
    if len(areas) > 1 and "area" in df.columns and "area" not in group_cols:
        group_cols.append("area")
    if group_cols:
        grouped = df.groupby(group_cols).agg(agg_map).reset_index()
    else:
        grouped = df.agg(agg_map).to_frame().T
    chart_data = grouped.to_dict(orient="records")
    return chart_data, table_data

def build_mock_summary(query: str, areas: List[str], metric: str, chart_data: List[Dict[str, Any]]) -> str:
    if not chart_data:
        return ("I couldn’t find matching data for your query. "
                "Try a different locality name or a broader time range.")
    area_part = ", ".join(areas) if areas else "the selected localities"
    metric_phrase = {
        "price": "average price levels",
        "demand": "buyer demand index",
        "both": "both price and demand levels",
    }.get(metric, "key metrics")
    years = sorted({row.get("year") for row in chart_data if row.get("year") is not None})
    if years:
        period = f"{years[0]}–{years[-1]}"
    else:
        period = "the available period"
    sentence_1 = f"For {area_part}, the {metric_phrase} show noticeable variation over {period}."
    try:
        first = chart_data[0]
        last = chart_data[-1]
        details = []
        if "price" in first and "price" in last:
            if last["price"] > first["price"]:
                details.append("prices have generally increased over time")
            elif last["price"] < first["price"]:
                details.append("prices have generally softened over time")
            else:
                details.append("prices have remained relatively stable")
        if "demand" in first and "demand" in last:
            if last["demand"] > first["demand"]:
                details.append("demand has trended upwards")
            elif last["demand"] < first["demand"]:
                details.append("demand has trended downwards")
            else:
                details.append("demand has stayed broadly flat")
        if details:
            sentence_2 = " At a high level, " + " and ".join(details) + "."
        else:
            sentence_2 = ""
    except Exception:
        sentence_2 = ""
    sentence_3 = (" Use the chart for a quick comparison across years "
                  "and the table for detailed, row-level inspection.")
    return sentence_1 + sentence_2 + " " + sentence_3
