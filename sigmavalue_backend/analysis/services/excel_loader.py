import pandas as pd
from functools import lru_cache
from pathlib import Path

# BASE_DIR points to sigmavalue_backend/
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "Sample_data.xlsx"


class DatasetNotFoundError(Exception):
    pass


@lru_cache(maxsize=1)
def load_dataset() -> pd.DataFrame:
    """
    Load the Excel dataset once and cache it in memory.
    Also normalize and rename columns so the rest of the code
    can always rely on generic names: area, price, demand.
    """
    if not DATA_FILE.exists():
        raise DatasetNotFoundError(f"Dataset file not found at: {DATA_FILE}")

    df = pd.read_excel(DATA_FILE)

    # Normalize column names: lowercase and strip spaces
    df.columns = [c.strip().lower() for c in df.columns]

    # Map the real columns from Sample_data.xlsx to generic names
    # Actual columns in your sheet:
    # 'final location', 'year', 'flat - weighted average rate', 'total sold - igr', ...
    rename_map = {
        "final location": "area",                   # locality name
        "flat - weighted average rate": "price",    # treat as price
        "total sold - igr": "demand",               # treat as demand
    }

    df = df.rename(columns=rename_map)

    return df


def filter_by_area(df: pd.DataFrame, areas: list[str]) -> pd.DataFrame:
    """
    Filter the dataframe by the 'area' column (which we mapped from 'final location').
    """
    if "area" not in df.columns:
        # If mapping failed for some reason, just return df unchanged
        return df

    areas_lower = [a.lower() for a in areas]
    return df[df["area"].str.lower().isin(areas_lower)]
