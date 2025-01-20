import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ZIP_CODE_ID = os.environ("ZIP_CODE_ID")
STREET_ID = os.environ("STREET_ID")
HOUSE_NUMBER = os.environ("HOUSE_NUMBER")
STRAAT = os.environ("STRAAT")
GEEMENTE = os.environ("GEEMENTE")