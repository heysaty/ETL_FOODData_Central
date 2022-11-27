import sys

sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central')

from extraction import search_food
from transformation.nutrients import nutrients


def get_nutrients(food_item):
    api_response = search_food.search_food(food_item)

    try:
        if api_response['totalPages'] != 0 and len(api_response['foods'][1]['foodNutrients']) != 0:

            nutrients_json = api_response['foods'][1]['foodNutrients']
            food_description = api_response['foods'][1]["description"]

            minerals_dict = {}
            fats_dict = {}
            vitamins_dict = {}
            macros_dict = {}

            for item in nutrients_json:
                if item['nutrientName'] in nutrients.get_vitamins():
                    vitamins_dict[item['nutrientName']] = str(item['value']) + ' ' + item['unitName'].lower()

                if item['nutrientName'] in nutrients.get_fats():
                    fats_dict[item['nutrientName']] = str(item['value']) + ' ' + item['unitName'].lower()

                if item['nutrientName'] in nutrients.get_macronutrients():
                    macros_dict[item['nutrientName']] = str(item['value']) + ' ' + item['unitName'].lower()

                if item['nutrientName'] in nutrients.get_minerals():
                    minerals_dict[item['nutrientName']] = str(item['value']) + ' ' + item['unitName'].lower()

            for item in nutrients.get_vitamins():
                if item not in vitamins_dict.keys():
                    vitamins_dict[item] = None

            for item in nutrients.get_fats():
                if item not in fats_dict.keys():
                    fats_dict[item] = None

            for item in nutrients.get_macronutrients():
                if item not in macros_dict.keys():
                    macros_dict[item] = None

            for item in nutrients.get_minerals():
                if item not in minerals_dict.keys():
                    minerals_dict[item] = None

            return vitamins_dict, fats_dict, macros_dict, minerals_dict, food_description

        else:
            print('NO Such Food Items !!!')
            return None
    except:
        print('API Connection Error !!!')
        return None


