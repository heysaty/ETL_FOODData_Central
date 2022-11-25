import sys

sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central')

from extraction import search_food
from transformation.nutrients import get_nutrients_name


def get_nutrients(food_item):
    api_response = search_food.search_food(food_item)

    try:
        if api_response['totalPages'] != 0 and len(api_response['foods'][1]['foodNutrients']) != 0:
            # pprint(api_response['foods'][1]['foodNutrients'])

            nutrients_json = api_response['foods'][1]['foodNutrients']
            food_description = api_response['foods'][1]["description"]
            nutrients_dict = {}

            for item in nutrients_json:
                if item['nutrientName'] in get_nutrients_name():
                    nutrients_dict[item['nutrientName']] = str(item['value']) + ' ' + item['unitName'].lower()

            for item in get_nutrients_name():
                if item not in nutrients_dict.keys():
                    # print(item)
                    nutrients_dict[item] = None
            # print(nutrients_dict, food_description)
            return nutrients_dict, food_description

        else:
            print('NO Such Food Items !!!')
            return None
    except:
        print('API Connection Error !!!')
        return None
