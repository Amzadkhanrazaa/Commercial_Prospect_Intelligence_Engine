import pandas as pd
import joblib

from src.config import DATA_PATH, MODEL_PATH
from src.feature_engineering import create_features

def score_leads():

    df = pd.read_csv(DATA_PATH)

    features = create_features(df)

    model = joblib.load(MODEL_PATH)

    df["lead_score"] = model.predict_proba(features)[:,1]

    df = df.sort_values("lead_score",ascending=False)

    print(df[["name","company","lead_score"]].head(10))

    return df