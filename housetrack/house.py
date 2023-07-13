"""House module"""

from pathlib import Path
from typing import Optional
from datetime import datetime


class House:
    """Representation of a house"""

    address: str = None
    url: str = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    price: Optional[int] = None
    house_type: Optional[str] = None
    living_size: Optional[int] = None
    rooms: Optional[int] = None
    bedrooms: Optional[int] = None
    url: Optional[str] = None
    plot_area: Optional[int] = None
    registration_date: Optional[datetime] = None
    year: Optional[int] = None
    location: Optional[str] = None

    def __init__(
        self,
        address: str,
        url: Optional[str] = None,
    ):
        self.address = address
        self.url = url

    def fields(self):
        """Return fields of the object"""
        fields = {
            "Address": self.address,
            "Update date": datetime.today().strftime("%Y-%m-%d"),
        }
        if self.postcode:
            fields["Postcode"] = self.postcode
        if self.city:
            fields["City"] = self.city
        if self.price:
            fields["Price"] = self.price
        if self.house_type:
            fields["House type"] = self.house_type
        if self.living_size:
            fields["Living size"] = self.living_size
        if self.rooms:
            fields["Rooms"] = self.rooms
        if self.bedrooms:
            fields["Bedrooms"] = self.bedrooms
        if self.url:
            fields["URL"] = self.url
        if self.plot_area:
            fields["Plot area"] = self.plot_area
        if self.registration_date:
            fields["Registration date"] = self.registration_date.strftime("%Y-%m-%d")
        if self.year:
            fields["Year"] = self.year
        if self.location:
            fields["Location"] = self.location
        return fields

    def record(self):
        """Return records with fields"""
        return {"fields": self.fields()}

    def html_path(self):
        """Return path for HTML storage"""
        return Path.cwd() / f"{self.address}.html"

    def __str__(self):
        return f"{self.address}"

    def __repr__(self):
        return self.__str__()
