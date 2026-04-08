import pandas as pd 
from db.connection import get_connection

def run_queries():
    conn = get_connection()

    with open("queries/sales_queries.sql", "r") as file:
        sql = file.read()

    df = pd.read_sql(sql, conn)

    print(df)
    
    conn.close()

if __name__ == "__main__":
    run_queries()