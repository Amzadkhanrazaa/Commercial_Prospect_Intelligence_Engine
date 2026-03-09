import streamlit as st
import pandas as pd
import sqlite3

st.title("AI Lead Scoring Dashboard")

conn = sqlite3.connect("database/leads.db")

df = pd.read_sql("SELECT * FROM leads", conn)

st.subheader("Lead Score Distribution")

st.bar_chart(df["lead_score"])

st.subheader("Top Leads")

top_leads = df.sort_values("lead_score", ascending=False).head(20)


st.dataframe(top_leads)

st.subheader("Average Lead Score by Company")

company_scores = df.groupby("company")["lead_score"].mean()

st.bar_chart(company_scores)