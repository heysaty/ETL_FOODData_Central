import sys

sys.path.insert(1, '//Users/apple/code/ETL_FOODData_Central')
from loading.postgres_connection import conn
from loading.create_table import tables
from transformation.preprocessing_nutrients import pre_processing
from loading.insert_data import insert_query
from scraper.recipe_scraper import scraper

queries = [tables.recipes()]


class run_query:

    @staticmethod
    def create_table_execution():
        for query in queries:
            cursor = conn.cursor()
            cursor.execute(query)

            conn.commit()
            cursor.close()

    @staticmethod
    def find_id(table):
        query = """
                select id from {} order by id desc
                """.format(table)

        cursor = conn.cursor()
        cursor.execute(query)
        table_id = cursor.fetchall()
        table_id = int(table_id[0][0])

        return table_id

    @staticmethod
    def execute_query(query):
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    @staticmethod
    def food_repetition_checker(food):
        cursor = conn.cursor()
        cursor.execute(f"select * from fooditems where food_item = '{food}'")
        flag = cursor.fetchone()
        if flag is None:
            return True
        else:
            return False



    @staticmethod
    def insert_data(fooditem):

        try:
            if run_query.food_repetition_checker(fooditem) is True:
                vitamins_dict, fats_dict, macros_dict, minerals_dict, food_description = pre_processing.get_nutrients(
                    fooditem)

                run_query.execute_query(insert_query.insert_minerals(minerals_dict))
                run_query.execute_query(insert_query.insert_fats(fats_dict))

                fat_id = run_query.find_id('fats')

                run_query.execute_query(insert_query.insert_vitamins(vitamins_dict))
                run_query.execute_query(insert_query.insert_macronutrients(macros_dict, fat_id))

                mineral_id = run_query.find_id('minerals')
                vitamins_id = run_query.find_id('vitamins')

                run_query.execute_query(insert_query.insert_micronutrients(mineral_id, vitamins_id))

                micros_id = run_query.find_id('micro_nutrients')
                macros_id = run_query.find_id('macro_nutrients')

                run_query.execute_query(insert_query.insert_nutrientslog(macros_id, micros_id))

                log_id = run_query.find_id('nutrients_log')

                run_query.execute_query(insert_query.insert_fooditem_query(fooditem, food_description, log_id))

                food_id = run_query.find_id('fooditems')

                run_query.execute_query(insert_query.insert_recipes(scraper(fooditem), food_id))
            else:
                print('Food Already Exists in Database !!!')

        except:
            print('Database Connection Error !!!')
