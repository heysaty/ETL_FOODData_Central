import time
import pandas as pd
from loading.query_execution import run_query
from loading.postgres_connection import conn

start = time.time()
df = pd.read_csv('foods.csv')


def run_pipeline(flag):
    if flag == 'scraper':
        food = input("Enter food item :")
        run_query.insert_recipe(food)
    else:
        for food in df['food']:
            run_query.insert_data(food)

        conn.close()

    print(time.time() - start)
