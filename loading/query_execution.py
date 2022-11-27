import sys

sys.path.insert(1, '//Users/apple/code/ETL_FOODData_Central')
from loading.postgres_connection import conn
from loading.create_table import tables
from transformation import preprocessing_nutrients
from loading.insert_data import insert_query

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


# create_table_execution()
# conn.close()


def insert_data(fooditem):
    # create_table_execution()

    vitamins_dict, fats_dict, macros_dict, minerals_dict, food_description = preprocessing_nutrients.get_nutrients(
        fooditem)
    # food_description= food_description.replace(''', '')
    print(vitamins_dict, '\n', fats_dict, '\n', macros_dict, '\n', minerals_dict, '\n', food_description)

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_minerals(minerals_dict))
    conn.commit()

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_fats(fats_dict))
    conn.commit()

    cursor.execute('select id from fats order by id desc')
    fat_id = cursor.fetchall()
    fat_id = int(fat_id[0][0])
    conn.commit()

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_vitamins(vitamins_dict))
    conn.commit()

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_macronutrients(macros_dict, fat_id))
    conn.commit()

    cursor.execute('select id from minerals order by id desc')
    mineral_id = cursor.fetchall()
    mineral_id = int(mineral_id[0][0])
    conn.commit()

    cursor.execute('select id from vitamins order by id desc')
    vitamins_id = cursor.fetchall()
    vitamins_id = int(vitamins_id[0][0])
    conn.commit()

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_micronutrients(mineral_id, vitamins_id))
    conn.commit()

    cursor.execute('select id from micro_nutrients order by id desc')
    micros_id = cursor.fetchall()
    micros_id = int(micros_id[0][0])
    conn.commit()

    cursor.execute('select id from macro_nutrients order by id desc')
    macros_id = cursor.fetchall()
    macros_id = int(macros_id[0][0])
    conn.commit()

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_nutrientslog(macros_id, micros_id))
    conn.commit()

    cursor.execute('select id from nutrients_log order by id desc')
    log_id = cursor.fetchall()
    log_id = int(log_id[0][0])
    conn.commit()

    cursor = conn.cursor()
    cursor.execute(insert_query.insert_fooditem_query(fooditem, food_description, log_id))
    conn.commit()
    cursor.close()

    # cur = conn.cursor()
    # cur.execute(insert_nutrients_query(nutrients_dict))
    # conn.commit()
    # # cur.close()
    # #
    # #
    # # cur = conn.cursor()
    # cur.execute('select id from nutrients order by id desc')
    # id = cur.fetchall()
    # # print(id[0][0])
    # nutrients_id = int(id[0][0])
    # conn.commit()
    # # cur.close()
    # #
    # #
    # # cur = conn.cursor()
    # cur.execute(insert_fooditem_query(fooditem, food_description, nutrients_id))
    # conn.commit()
    # cur.close()
    # except:
    #     print("API Connection error !!!")
