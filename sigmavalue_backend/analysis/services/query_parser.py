import re
from typing import Tuple, List
from .excel_loader import load_dataset  # 👈 add this import at the top


def extract_areas(query: str) -> List[str]:
    """
    Detect area/locality names by matching against the dataset's 'area' column.
    This is much more robust than trying to guess from generic text rules.
    """
    q = query.lower()

    df = load_dataset()
    if "area" not in df.columns:
        return []


    # Get all unique area names from the data
    known_areas = (
        df["area"]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
        .unique()
        .tolist()
    )

    matched = []
    for area in known_areas:
        if area and area in q:
            # Title-case for consistency (Wakad, Aundh, etc.)
            matched.append(area.title())

    # Remove duplicates while preserving order
    seen = set()
    result = []
    for a in matched:
        if a not in seen:
            seen.add(a)
            result.append(a)

    return result
def detect_metric(query: str) -> str:
    q = query.lower()
    has_price = "price" in q
    has_demand = "demand" in q
    if has_price and has_demand:
        return "both"
    if has_price:
        return "price"
    if has_demand:
        return "demand"
    return "both"

def detect_year_range(query: str) -> Tuple[int | None, int | None]:
    years = re.findall(r"(20[0-3][0-9])", query)
    if not years:
        return None, None
    years_int = sorted({int(y) for y in years})
    return years_int[0], years_int[-1]
