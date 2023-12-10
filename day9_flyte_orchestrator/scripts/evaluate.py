from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

if __name__ == "__main__":
    data = pd.read_csv("data/test.csv")
    features = data.drop("target", axis="columns")

    model = pickle.load(open("clf.pkl", "rb"))
    final_df = data[["target"]].copy()
    final_df["prediction"] = model.predict(features)
    final_df.to_csv("data/evaluation_report.txt")
