from pprint import pprint

import requests
import sys
sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central/extraction')

from api_connection import URL


def search_food(food_item):
    print(food_item.upper(),'\n\n')
    url = URL + food_item

    get_response = requests.get(url)

    # extracting data in json format
    data = get_response.json()

    return data
