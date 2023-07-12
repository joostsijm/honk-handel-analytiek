"""Trackhouses and save in Airtable"""

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from pyairtable import Table
from bs4 import BeautifulSoup

import extract
import transform
import load


load_dotenv()
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE")
AIRTABLE_TABLE = os.environ.get("AIRTABLE_TABLE")
MOVE_USERNAME = os.environ.get("MOVE_USERNAME")
MOVE_PASSWORD = os.environ.get("MOVE_PASSWORD")
HTML_PATH = Path.cwd() / "mijn_gevonden_woningen.html"


def main():
    """Method to initialize the application"""
    table = Table(AIRTABLE_TOKEN, AIRTABLE_BASE, AIRTABLE_TABLE)
    extract.execute(MOVE_USERNAME, MOVE_PASSWORD, HTML_PATH)
    houses = transform.execute(HTML_PATH)
    load.execute(table, houses)

    print(table.all())


if __name__ == "__main__":
    main()
