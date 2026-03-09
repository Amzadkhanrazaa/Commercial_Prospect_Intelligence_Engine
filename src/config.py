import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "prospect.csv")

DB_PATH = os.path.join(BASE_DIR, "database", "leads.db")

MODEL_PATH = os.path.join(BASE_DIR, "models", "lead_model.pkl")

LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")

RANDOM_STATE = 42