import pandas as pd


def load_messages(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)
