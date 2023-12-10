from sklearn.datasets import load_wine
from flytekit import task
import pandas as pd


@task
def preprocess_df() -> pd.DataFrame:
    data = load_wine(as_frame=True).frame
    data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))
    return data


if __name__ == "__main__":
    data = preprocess_df()
    data.to_csv("data/processed_data.csv")
