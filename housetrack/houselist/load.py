"""Load module"""

from pyairtable import Table

from database import Database


class Load:
    """Load class"""

    __database: Database = None

    def __init__(self, database: Database):
        self.__database = database

    def execute(self, houses):
        """Load houses to database"""
        self.__database.update([house.record() for house in houses])
