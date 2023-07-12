"""Load module"""


def execute(table, houses):
    """Load houses to AirTable"""
    for house in houses:
        table.create(house.row())
