
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("FDC_API_KEY")
DATABASE_NAME = os.environ.get('databaseName')
USERNAME = os.environ.get('username')
PASSWORD = os.environ.get('password')
HOST = os.environ.get('host')
PORT = os.environ.get('port')

