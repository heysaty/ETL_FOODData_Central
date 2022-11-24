from pprint import pprint

import sys
sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central')

from extraction import search_food



api_response = search_food.search_food("pizza")



print(api_response['totalPages'],api_response["totalHits"])