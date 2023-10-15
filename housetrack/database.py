"""Database module"""

from datetime import datetime
from typing import Optional

import requests
from pyairtable import Table

from house import House


class AirtableError(Exception):
    """Exception for credential error"""

    def __init__(self, message):
        super().__init__(message)


class Database:
    """Airtable class"""

    __table: Table = None

    def __init__(self, airtable_token: str, airtable_base: str, airtable_table: str):
        self.__table = Table(airtable_token, airtable_base, airtable_table)

    def houses(self, needs_update: Optional[bool] = None) -> list[House]:
        """Retrive airtable rows as House"""
        if needs_update:
            today = datetime.today().strftime("%Y-%m-%d")
            rows = self.__table.all(
                formula=f"OR(DATETIME_DIFF({{Update date}}, '{today}', 'd')<=-7,{{Update date}} = BLANK())"
            )
        else:
            rows = self.__table.all()
        return [House(fields=row["fields"]) for row in rows]

    def update(self, records: list[list[str]]):
        """Load record to Airtable"""
        try:
            updated_houses = self.__table.batch_upsert(
                records, key_fields=["Address"], typecast=True
            )
        except requests.exceptions.HTTPError as exception:
            raise AirtableError(
                "Validate you Airtable credentials in the environment configuration."
            ) from exception
        return updated_houses
