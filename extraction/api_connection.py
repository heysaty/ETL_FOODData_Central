import sys
sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central')
import config



URL = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=" + config.SECRET_KEY + "&query="


