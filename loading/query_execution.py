import sys

sys.path.insert(1, '//Users/apple/code/ETL_FOODData_Central')
from loading.postgres_connection import conn
from loading.create_table import tables
from transformation import preprocessing_nutrients
from loading.insert_data import insert_query
from scraper.recipe_scraper import scraper

queries = [tables.recipes()]


class run_query:

    @staticmethod
    def create_table_execution():
        for query in queries:
            cur = conn.cursor()
            cur.execute(query)

            conn.commit()
            cur.close()

    @staticmethod
    def insert_data(fooditem):

        try:

            vitamins_dict, fats_dict, macros_dict, minerals_dict, food_description = preprocessing_nutrients.get_nutrients(
                fooditem)

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

            cursor.execute('select id from fooditems order by id desc')
            food_id = cursor.fetchall()
            food_id = int(food_id[0][0])
            conn.commit()

            cursor = conn.cursor()
            cursor.execute(insert_query.insert_recipes(scraper(fooditem), food_id))
            conn.commit()

            cursor.close()
        except:
            print('Database Connection Error !!!')
