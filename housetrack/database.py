"""Database module"""

from pyairtable import Table

from house import House


class Database:
    """Airtable class"""

    __table: Table = None

    def __init__(self, airtable_token: str, airtable_base: str, airtable_table: str):
        self.__table = Table(airtable_token, airtable_base, airtable_table)

    def houses(self) -> list[House]:
        """Retrive all rows as House"""
        return [House(fields=row["fields"]) for row in self.__table.all()]

    def update(self, records: list[list[str]]):
        """Load record to Airtable"""
        return self.__table.batch_upsert(records, key_fields=["Address"], typecast=True)
