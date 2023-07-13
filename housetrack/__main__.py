"""Trackhouses and save in Airtable"""

import os
from pathlib import Path

from dotenv import load_dotenv

from house import House
import houselist
import housedetail


load_dotenv()
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE")
AIRTABLE_TABLE = os.environ.get("AIRTABLE_TABLE")
MOVE_USERNAME = os.environ.get("MOVE_USERNAME")
MOVE_PASSWORD = os.environ.get("MOVE_PASSWORD")
HOUSE_URL = os.environ.get("HOUSE_URL")
# HTML_PATH = Path.cwd() / "mijn_gevonden_woningen.html"
HTML_PATH = Path.cwd() / "house.html"


def run_houselist():
    """Execute houselist ETL"""
    extract = houselist.Extract(MOVE_USERNAME, MOVE_PASSWORD, HTML_PATH)
    transform = houselist.Transform(HTML_PATH)
    load = houselist.Load(AIRTABLE_TOKEN, AIRTABLE_BASE, AIRTABLE_TABLE)
    houselist.run_etl(extract, transform, load)


def run_housedetail():
    """Execute housedetail ETL"""
    house = House("Test 23")
    house.url = HOUSE_URL
    extract = housedetail.Extract(MOVE_USERNAME, MOVE_PASSWORD, house, HTML_PATH)
    transform = housedetail.Transform(house, HTML_PATH)
    housedetail.run_etl(extract, transform)


def main():
    """Method to initialize the application"""
    run_housedetail()


if __name__ == "__main__":
    main()
