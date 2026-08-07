import sqlite3


def create_connection():

    conn = sqlite3.connect("customer_behavior.db")

    return conn


def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(

        CustomerID INTEGER,
        Age INTEGER,
        Gender TEXT,
        City TEXT,
        Category TEXT,
        ProductName TEXT,
        PurchaseAmount REAL,
        PurchaseDate TEXT,
        PaymentMethod TEXT,
        CustomerRating REAL

    )
    """)

    conn.commit()
    conn.close()


def insert_dataframe(df):

    conn = create_connection()

    df.to_sql(
        "customers",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def read_data():

    conn = create_connection()

    data = conn.execute(
        "SELECT * FROM customers"
    ).fetchall()

    conn.close()

    return data