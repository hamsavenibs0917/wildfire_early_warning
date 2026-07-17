from pathlib import Path
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "wildfire_model.pkl"
DATASET_PATH = BASE_DIR / "dataset" / "wildfire_data.csv"


def load_model():
    try:
        with open(MODEL_PATH, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


def train_model():
    data_frame = pd.read_csv(DATASET_PATH)
    features = data_frame.drop("risk", axis=1)
    target = data_frame["risk"]

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    with open(MODEL_PATH, "wb") as file:
        pickle.dump(model, file)

    return model, accuracy
