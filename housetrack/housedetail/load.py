"""Load module"""

from pyairtable import Table

from house import House
from database import Database


class Load:
    """Load class"""

    __database: Database = None

    def __init__(self, database: Database):
        self.__database = database

    def execute(self, houses: list[House]):
        """Load houses to database"""
        self.__database.update([house.record() for house in houses])
