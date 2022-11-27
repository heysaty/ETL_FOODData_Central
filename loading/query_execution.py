import sys
sys.path.insert(1, '//Users/apple/code/ETL_FOODData_Central')
from loading.postgres_connection import conn
from loading import create_table
from transformation import preprocessing_nutrients
from loading.insert_data import insert_fooditem_query, insert_nutrients_query

queries = [create_table.create_minerals(),create_table.create_vitamins(),create_table.create_fats(),
           create_table.create_macronutrients(),create_table.create_micronutrients(),
           create_table.create_nutrientslog(),create_table.create_fooditems(), 'select * from fooditems;']


# nutrients_dict, food_description = preprocessing_nutrients.get_nutrients()

def create_table_execution():
    for query in queries:
        print(query)
        # #     try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
            # conn.close()
        # except:
        #     continue


create_table_execution()
conn.close()


def insert_data(fooditem):
    # create_table_execution()

    try:
        nutrients_dict, food_description = preprocessing_nutrients.get_nutrients(fooditem)
        # food_description= food_description.replace(''', '')
        cur = conn.cursor()
        # print(nutrients_dict)
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



