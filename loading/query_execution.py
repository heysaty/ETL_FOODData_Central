import sys

sys.path.insert(1, '//Users/apple/code/ETL_FOODData_Central')
from loading.postgres_connection import conn
from loading.create_table import tables
from transformation import preprocessing_nutrients
from loading.insert_data import insert_fooditem_query, insert_nutrients_query

queries = [tables.create_minerals(), tables.create_vitamins(), tables.create_fats(),
           tables.create_macronutrients(), tables.create_micronutrients(),
           tables.create_nutrientslog(), tables.create_fooditems(), tables.recipes()]


# nutrients_dict, food_description = preprocessing_nutrients.get_nutrients()

def create_table_execution():
    for query in queries:


        cur = conn.cursor()
        cur.execute(query)
        print(query)
        conn.commit()
        cur.close()
        # conn.close()


create_table_execution()
# conn.close()


def insert_data(fooditem):
    # create_table_execution()

    try:
        vitamins_dict, fats_dict, macros_dict, minerals_dict, food_description = preprocessing_nutrients.get_nutrients()
        # food_description= food_description.replace(''', '')
        cur = conn.cursor()
        cur.execute(insert_nutrients_query(nutrients_dict))
        conn.commit()
        # cur.close()
        #
        #
        # cur = conn.cursor()
        cur.execute('select id from nutrients order by id desc')
        id = cur.fetchall()
        # print(id[0][0])
        nutrients_id = int(id[0][0])
        conn.commit()
        # cur.close()
        #
        #
        # cur = conn.cursor()
        cur.execute(insert_fooditem_query(fooditem, food_description, nutrients_id))
        conn.commit()
        cur.close()
    except:
        print("API Connection error !!!")
