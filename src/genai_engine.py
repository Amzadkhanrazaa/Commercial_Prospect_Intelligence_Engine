import pandas as pd

def generate_insights(df):

    high_value = df[df["lead_score"] > 0.8]

    insight = f"""
    Sales Insight Report

    Total high value leads: {len(high_value)}

    Recommendation:
    Focus outreach on leads with engagement_score > 50
    and demo_requested = 1
    """

    print(insight)