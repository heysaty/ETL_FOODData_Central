import psycopg2
import sys

sys.path.insert(1, '/Users/apple/code/ETL_FOODData_Central')

import config

conn = psycopg2.connect(
    database=config.DATABASE_NAME, user=config.USERNAME, password=config.PASSWORD, host=config.HOST,
    port=config.PORT
)
