from db.load_data import load_csv_to_postgres
from scripts.run_queries import run_queries

if __name__ == "__main__":
    print("Step 1: Loading data...")
    load_csv_to_postgres()

    print("Step 2: Running queries...")
    run_queries()