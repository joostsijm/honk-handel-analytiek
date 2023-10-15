"""Trackhouses and save in Airtable"""

import os
from pathlib import Path

from dotenv import load_dotenv

from database import Database
import houselist
import housedetail


load_dotenv()
MOVE_USERNAME = os.environ.get("MOVE_USERNAME")
MOVE_PASSWORD = os.environ.get("MOVE_PASSWORD")
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE")
AIRTABLE_TABLE = os.environ.get("AIRTABLE_TABLE")
HOUSE_URL = os.environ.get("HOUSE_URL")

HOUSELIST_HTML_PATH = Path.cwd() / "extract" / "mijn_gevonden_woningen.html"
DATABASE = Database(AIRTABLE_TOKEN, AIRTABLE_BASE, AIRTABLE_TABLE)


def run_houselist():
    """Execute houselist ETL"""
    extract = houselist.Extract(MOVE_USERNAME, MOVE_PASSWORD, HOUSELIST_HTML_PATH)
    transform = houselist.Transform(HOUSELIST_HTML_PATH)
    load = houselist.Load(DATABASE)
    loaded_data = houselist.run_etl(extract, transform, load)
    print(f"Found {len(loaded_data)} new houses in list.")


def run_housedetail(from_cache: bool = False):
    """Execute housedetail ETL"""
    needs_update = not from_cache
    houses = DATABASE.houses(needs_update=needs_update)
    if not houses:
        return
    extract = (
        None
        if from_cache
        else housedetail.Extract(MOVE_USERNAME, MOVE_PASSWORD, houses)
    )
    transform = housedetail.Transform(houses)
    load = housedetail.Load(DATABASE)
    loaded_data = housedetail.run_etl(extract, transform, load)
    print(f"Update details of {len(loaded_data)} houses.")


def main():
    """Method to initialize the application"""
    run_houselist()
    run_housedetail(from_cache=False)


if __name__ == "__main__":
    main()
