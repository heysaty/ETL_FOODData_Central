from transformation.preprocessing_nutrients import get_nutrients
import pandas as pd
import time


start = time.time()
df = pd.read_csv('foods.csv')
print(df)
for food in df['food']:
# food= input("food: ")
    x=time.time()
    print(get_nutrients(food))
    print('---------------------------------------------------\n')
    t=time.time()
    print('------------',t-x,'-------------')
print(time.time() - start)
