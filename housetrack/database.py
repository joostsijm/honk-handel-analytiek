"""Database module"""

from datetime import datetime
from typing import Optional

from pyairtable import Table
from pyairtable.formulas import match

from house import House


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
        return self.__table.batch_upsert(records, key_fields=["Address"], typecast=True)
