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
            for item in nutrients_json:
                if item['nutrientName'] in get_nutrients_name():
                    # pprint(item)
                    print(item['nutrientName'], ' = ', str(item['value']), ' ', item['unitName'])
                    # print('\n\n----------------------------------------------------------------------')


        else:
            print('NO Such Food Items !!!')
    except:
        print('API Connection Error !!!')


