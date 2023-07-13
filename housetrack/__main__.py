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

    extract = houselist.Extract(MOVE_USERNAME, MOVE_PASSWORD)
    extracted_data = extract.execute()
    with open(HTML_PATH, "w", encoding="utf-8") as file:
        file.write(extracted_data)

    transform = houselist.Transform(HTML_PATH)
    transformed_data = transform.execute()

    load = houselist.Load(AIRTABLE_TOKEN, AIRTABLE_BASE, AIRTABLE_TABLE)
    loaded_data = load.execute(transformed_data)
    print(loaded_data)


if __name__ == "__main__":
    main()
