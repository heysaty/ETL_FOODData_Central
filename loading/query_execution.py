import sys
sys.path.insert(1, '//Users/apple/code/ETL_FOODData_Central')
from loading.postgres_connection import conn
from loading import create_table
from transformation import preprocessing_nutrients
from loading.insert_data import insert_fooditem_query, insert_nutrients_query

queries = [create_table.create_nutrients(), create_table.create_fooditems(), 'select * from fooditems;']


# nutrients_dict, food_description = preprocessing_nutrients.get_nutrients()

def create_table_execution():
    for query in queries:
        try:
            cur = conn.cursor()
            print(query)
            print(cur.execute(query))
            conn.commit()
            cur.close()
            # conn.close()
        except:
            continue


# create_table_execution()


def insert_data(fooditem):


    nutrients_dict, food_description = preprocessing_nutrients.get_nutrients(fooditem)

    cur = conn.cursor()
    cur.execute(insert_nutrients_query(nutrients_dict))
    conn.commit()
    cur.close()


    cur = conn.cursor()
    cur.execute('select id from nutrients order by id desc')
    id = cur.fetchall()
    print(id[0][0])
    nutrients_id = int(id[0][0])
    conn.commit()
    cur.close()


    cur = conn.cursor()
    cur.execute(insert_fooditem_query(fooditem, food_description, nutrients_id))
    conn.commit()
    cur.close()



