from src.data_generator import generate_data
from src.train_model import train
from src.evaluate_model import evaluate
from src.database_loader import load
from src.sql_analytics import run_queries


def run_pipeline():

    print("Generating Data...")
    generate_data()

    print("Training Model...")
    train()

    print("Evaluating Model...")
    evaluate()

    print("Scoring Leads + Loading DB...")
    load()

    print("Running SQL Analytics...")
    run_queries()


if __name__ == "__main__":
    run_pipeline()