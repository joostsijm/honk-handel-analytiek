"""Trackhouses and save in Airtable"""

import os
from pathlib import Path

from dotenv import load_dotenv

from database import Database
import houselist
import housedetail


load_dotenv()
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE")
AIRTABLE_TABLE = os.environ.get("AIRTABLE_TABLE")
MOVE_USERNAME = os.environ.get("MOVE_USERNAME")
MOVE_PASSWORD = os.environ.get("MOVE_PASSWORD")
HOUSE_URL = os.environ.get("HOUSE_URL")
HOUSELIST_HTML_PATH = Path.cwd() / "extract" / "mijn_gevonden_woningen.html"
DATABASE = Database(AIRTABLE_TOKEN, AIRTABLE_BASE, AIRTABLE_TABLE)


def run_houselist():
    """Execute houselist ETL"""
    extract = houselist.Extract(MOVE_USERNAME, MOVE_PASSWORD, HOUSELIST_HTML_PATH)
    transform = houselist.Transform(HOUSELIST_HTML_PATH)
    load = houselist.Load(DATABASE)
    loaded_data = houselist.run_etl(extract, transform, load)
    print(loaded_data)


def run_housedetail():
    """Execute housedetail ETL"""
    houses = DATABASE.houses(needs_update=True)
    extract = housedetail.Extract(MOVE_USERNAME, MOVE_PASSWORD, houses)
    transform = housedetail.Transform(houses)
    load = housedetail.Load(DATABASE)
    loaded_data = housedetail.run_etl(extract, transform, load)
    print(loaded_data)


def main():
    """Method to initialize the application"""
    run_houselist()
    run_housedetail()


if __name__ == "__main__":
    main()
