import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from src.config import DATA_PATH, MODEL_PATH
from src.feature_engineering import create_features

def train():

    df = pd.read_csv(DATA_PATH)

    X = create_features(df)
    y = df["converted"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )

    model.fit(X_train,y_train)

    joblib.dump(model, MODEL_PATH)

    print("Model trained and saved")

if __name__ == "__main__":
    train()