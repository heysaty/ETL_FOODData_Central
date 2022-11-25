import time
import pandas as pd
from loading import query_execution
from loading.postgres_connection import conn

start = time.time()
df = pd.read_csv('foods.csv')


def run_pipeline():
    for food in df['food']:
        query_execution.insert_data(food)
    conn.close()

    print(time.time() - start)
