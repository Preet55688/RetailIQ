import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}"
    return create_engine(connection_string)

def fetch_table(table_name):
    engine = get_engine()
    df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
    return df

def fetch_query(sql_query):
    engine = get_engine()
    df = pd.read_sql(sql_query, engine)
    return df

if __name__ == "__main__":
    df = fetch_table("Product")
    print(df)