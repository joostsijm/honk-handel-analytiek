"""Load module"""

from pyairtable import Table

from house import House


class Load:
    """Load class"""

    __table: Table = None

    def __init__(self, airtable_token: str, airtable_base: str, airtable_table: str):
        self.__table = Table(airtable_token, airtable_base, airtable_table)

    def execute(self, houses: list[House]):
        """Load houses to AirTable"""
        house_records = [house.record() for house in houses]
        print(house_records)

        return self.__table.batch_upsert(
            house_records, key_fields=["Address"], typecast=True
        )
