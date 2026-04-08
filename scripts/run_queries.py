from db.connection import get_connection

def run_queries():
    conn = get_connection()
    cur = conn.cursor()

    with open("queries/sales_queries.sql", "r") as file:
        sql = file.read()

    cur.execute(sql)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    run_queries()