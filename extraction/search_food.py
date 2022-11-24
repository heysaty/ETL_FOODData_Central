from pprint import pprint

import requests
import sys
sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central/extraction')

from api_connection import URL


def search_food(food_item):
    url = URL + food_item
    print(url)

    get_response = requests.get(url)

    # extracting data in json format
    data = get_response.json()

    return data
