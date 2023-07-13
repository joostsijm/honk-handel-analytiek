"""Trackhouses and save in Airtable"""

import os
from pathlib import Path

from dotenv import load_dotenv

import houselist


load_dotenv()
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN")
AIRTABLE_BASE = os.environ.get("AIRTABLE_BASE")
AIRTABLE_TABLE = os.environ.get("AIRTABLE_TABLE")
MOVE_USERNAME = os.environ.get("MOVE_USERNAME")
MOVE_PASSWORD = os.environ.get("MOVE_PASSWORD")
HTML_PATH = Path.cwd() / "mijn_gevonden_woningen.html"


def main():
    """Method to initialize the application"""
    extract = houselist.Extract(MOVE_USERNAME, MOVE_PASSWORD, HTML_PATH)
    transform = houselist.Transform(HTML_PATH)
    load = houselist.Load(AIRTABLE_TOKEN, AIRTABLE_BASE, AIRTABLE_TABLE)

    houselist.run_etl(extract, transform, load)


if __name__ == "__main__":
    main()
