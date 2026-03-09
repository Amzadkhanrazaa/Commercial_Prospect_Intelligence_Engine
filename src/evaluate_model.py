import pandas as pd
import joblib

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from src.config import DATA_PATH, MODEL_PATH
from src.feature_engineering import create_features

def evaluate():

    df = pd.read_csv(DATA_PATH)

    X = create_features(df)
    y = df["converted"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = joblib.load(MODEL_PATH)

    preds = model.predict(X_test)

    print(classification_report(y_test,preds))

if __name__ == "__main__":
    evaluate()