from transformation.preprocessing_nutrients import get_nutrients
import pandas as pd
import time
from loading import query_execution
from loading.postgres_connection import conn

start = time.time()
df = pd.read_csv('foods.csv')
print(df)

# for food in df['food']:

query_execution.insert_data('brownie')
conn.close()

print(time.time() - start)


#     x=time.time()
#     print(get_nutrients(food))
#     print('---------------------------------------------------\n')
#     t=time.time()
#     print('------------',t-x,'-------------')
# print(time.time() - start)