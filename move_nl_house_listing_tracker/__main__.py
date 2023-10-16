"""Trackhouses and save in Airtable"""

import os
import sys
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


def main():
    """Method to initialize the application"""
    if len(sys.argv) != 2:
        run_houselist()
        run_housedetail()
    else:
        if (argument := sys.argv[1]) == "list":
            run_houselist()
        elif argument == "detail":
            run_housedetail(from_cache=False)
        elif argument == "cache":
            run_housedetail(from_cache=True)
        else:
            print(f"Argument not available, got {argument}")

def run_houselist():
    """Execute houselist ETL"""
    print("Start adding new houses from list.")
    loaded_data = houselist.run_etl(
        houselist.Extract(MOVE_USERNAME, MOVE_PASSWORD, HOUSELIST_HTML_PATH),
        houselist.Transform(HOUSELIST_HTML_PATH),
        houselist.Load(DATABASE),
    )
    print(f"Finished adding {len(loaded_data)} new houses to database.")


def run_housedetail(from_cache: bool = False):
    """Execute housedetail ETL"""
    print("Start updating house details.")
    if houses := DATABASE.houses(needs_update=not from_cache):
        print(f"Found {len(houses)} that require updating details.")
        loaded_data = housedetail.run_etl(
            (
                None
                if from_cache
                else housedetail.Extract(MOVE_USERNAME, MOVE_PASSWORD, houses)
            ),
            housedetail.Transform(houses),
            housedetail.Load(DATABASE),
        )
        print(
            f"Finished updating existing {len(loaded_data)} house details to database."
        )


if __name__ == "__main__":
    main()
