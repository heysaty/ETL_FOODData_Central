import sys

sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central')

from extraction import search_food
from transformation.nutrients import nutrients


class pre_processing:
    @staticmethod
    def get_nutrients_dict(nutrients_json, nutrients_lst):
        nutrients_dict = {}
        for item in nutrients_json:
            if item['nutrientName'] in nutrients_lst:
                nutrients_dict[item['nutrientName']] = str(item['value']) + ' ' + item['unitName'].lower()

        for item in nutrients_lst:
            if item not in nutrients_dict.keys():
                nutrients_dict[item] = None

        return nutrients_dict

    @staticmethod
    def get_nutrients(food_item):
        api_response = search_food.search_food(food_item)

        try:
            if api_response['totalPages'] != 0 and len(api_response['foods'][1]['foodNutrients']) != 0:

                nutrients_json = api_response['foods'][1]['foodNutrients']
                food_description = api_response['foods'][1]["description"]

                minerals_dict = pre_processing.get_nutrients_dict(nutrients_json, nutrients.get_minerals())
                fats_dict = pre_processing.get_nutrients_dict(nutrients_json, nutrients.get_fats())
                vitamins_dict = pre_processing.get_nutrients_dict(nutrients_json, nutrients.get_vitamins())
                macros_dict = pre_processing.get_nutrients_dict(nutrients_json, nutrients.get_macronutrients())

                return vitamins_dict, fats_dict, macros_dict, minerals_dict, food_description

            else:
                print('NO Such Food Items !!!')
                return None
        except:
            print('API Connection Error !!!')
            return None
