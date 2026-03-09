import sqlite3
from src.config import DB_PATH
from src.Scoring_engine import score_leads

def load():

    df = score_leads()

    conn = sqlite3.connect(DB_PATH)

    df.to_sql("leads",conn,if_exists="replace",index=False)

    conn.close()

    print("Leads saved to DB")

if __name__ == "__main__":
    load()