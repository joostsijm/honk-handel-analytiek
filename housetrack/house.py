"""House module"""


class House:
    """Representation of a house"""

    def __init__(
        self,
        address: str = None,
        postcode: str = None,
        city: str = None,
        price: int = None,
        house_type: str = None,
        living_size: int = None,
        rooms: int = None,
        bedrooms: int = None,
        url: str = None,
    ):
        self.__address = address
        self.__postcode = postcode
        self.__city = city
        self.__price = price
        self.__house_type = house_type
        self.__living_size = living_size
        self.__rooms = rooms
        self.__bedrooms = bedrooms
        self.url = url

    def fields(self):
        """Return fields of the object"""
        return {
            "Address": self.__address,
            "Postcode": self.__postcode,
            "City": self.__city,
            "Price": self.__price,
            "House type": self.__house_type,
            "Living size": self.__living_size,
            "Rooms": self.__rooms,
            "Bedrooms": self.__bedrooms,
            "URL": self.url,
        }

    def record(self):
        """Return records with fields"""
        return {"fields": self.fields()}

    def __str__(self):
        return f"{self.__address} ({self.__price})"

    def __repr__(self):
        return self.__str__()
