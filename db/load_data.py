import pandas as pd
from db.connection import get_connection

def load_csv_to_postgres():
    conn = get_connection()
    cur = conn.cursor()

    df = pd.read_csv("data/coffee_shop_sales.csv")

    # Create table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        hour_of_day INT,
        cash_type TEXT,
        money FLOAT,
        coffee_name TEXT,
        time_of_day TEXT,
        weekday TEXT,
        month_name TEXT,
        weekdaysort INT,
        monthsort INT,
        date DATE,
        time TIME
    );
    """)

    conn.commit()

    # Insert data
    for _, row in df.iterrows():
        cur.execute("""
        INSERT INTO sales VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded successfully!")