"""House module"""


class House:
    """Representation of a house"""

    def __init__(self, address: str, postcode: str, price: int):
        self.__address = address
        self.__postcode = postcode
        self.__price = price

    def row(self):
        """Return row object for AirTable"""
        return {
            "Address": self.__address,
            "Postcode": self.__postcode,
            "Price": self.__price,
        }

    def __str__(self):
        return f"{self.__address} ({self.__price})"

    def __repr__(self):
        return self.__str__()
