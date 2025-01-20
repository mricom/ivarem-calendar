import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ZIP_CODE_ID = os.environ.get("ZIP_CODE_ID")
STREET_ID = os.environ.get("STREET_ID")
HOUSE_NUMBER = os.environ.get("HOUSE_NUMBER")
STRAAT = os.environ.get("STRAAT")
GEEMENTE = os.environ.get("GEEMENTE")