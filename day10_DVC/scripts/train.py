from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

if __name__ == "__main__":
    data = pd.read_csv("data/train.csv")
    features = data.drop("target", axis="columns")
    target = data["target"]
    model = LogisticRegression(max_iter=3000).fit(features, target)
    pickle.dump(model, open("clf.pkl", "wb"))
