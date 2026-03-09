import pandas as pd

def create_features(df):

    df["engagement_score"] = (
        df["website_visits"] * 0.3 +
        df["pages_viewed"] * 0.3 +
        df["time_spent"] * 0.2 +
        df["email_opens"] * 0.2
    )

    features = df[[
        "website_visits",
        "pages_viewed",
        "time_spent",
        "email_opens",
        "demo_requested",
        "engagement_score"
    ]]

    return features