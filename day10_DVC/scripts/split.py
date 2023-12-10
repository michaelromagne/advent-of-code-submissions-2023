import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple


def split(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    return train, test


if __name__ == "__main__":
    data = pd.read_csv("data/processed_data.csv")
    train, test = split(data)

    train.to_csv("data/train.csv")
    test.to_csv("data/test.csv")
