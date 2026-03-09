import sqlite3
from src.config import DB_PATH

def run_queries():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    q1 = """
    SELECT company, AVG(lead_score)
    FROM leads
    GROUP BY company
    ORDER BY 2 DESC
    LIMIT 5
    """

    results = cursor.execute(q1)

    print("\nTop Companies:\n")

    for row in results:
        print(row)

    conn.close()