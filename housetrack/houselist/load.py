"""Load module"""

from pyairtable import Table


class Load:
    """Load class"""

    __table: Table = None

    def __init__(self, airtable_token: str, airtable_base: str, airtable_table: str):
        self.__table = Table(airtable_token, airtable_base, airtable_table)

    def execute(self, houses):
        """Load houses to AirTable"""
        house_records = [house.record() for house in houses]

        return self.__table.batch_upsert(
            house_records, key_fields=["Address"], typecast=True
        )
