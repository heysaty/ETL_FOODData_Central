from transformation.preprocessing_nutrients import get_nutrients
import pandas as pd
import time
from loading import query_execution
from loading.postgres_connection import conn

start = time.time()
df = pd.read_csv('foods.csv')


for food in df['food']:
    query_execution.insert_data(food)
conn.close()

print(time.time() - start)
