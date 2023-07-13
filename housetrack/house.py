"""House module"""

from typing import Optional


class House:
    """Representation of a house"""
    postcode = Optional[str]
    city = Optional[str]
    price = Optional[str]
    house_type = Optional[str]
    living_size = Optional[str]
    rooms = Optional[str]
    bedrooms = Optional[str]
    url = Optional[str]
    registration_date = Optional[str]

    def __init__(
        self,
        address: str,
        url: str = None,
    ):
        self.address = address
        self.url = url

    def fields(self):
        """Return fields of the object"""
        fields = {
            "Address": self.address
        }
        if self.postcode: fields["Postcode"] = self.postcode
        if self.city: fields["City"] = self.city
        if self.price: fields["Price"] = self.price
        if self.house_type: fields["House type"] = self.house_type
        if self.living_size: fields["Living size"] = self.living_size
        if self.rooms: fields["Rooms"] = self.rooms
        if self.bedrooms: fields["Bedrooms"] = self.bedrooms
        if self.url: fields["URL"] = self.url
        if self.registration_date: fields["Registration date"] = self.registation_date

    def record(self):
        """Return records with fields"""
        return {"fields": self.fields()}

    def __str__(self):
        return f"{self.address}"

    def __repr__(self):
        return self.__str__()
