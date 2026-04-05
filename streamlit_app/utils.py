from pathlib import Path
from functools import lru_cache
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = PROJECT_ROOT #/ "data" / "processed"


def data_path(filename: str) -> Path:
    return PROCESSED_DATA_DIR / filename


@lru_cache(maxsize=16)
def read_processed_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(data_path(filename))


def safe_sample(df: pd.DataFrame, n: int, random_state: int = 42) -> pd.DataFrame:
    if df.empty:
        return df
    return df.sample(min(n, len(df)), random_state=random_state)
