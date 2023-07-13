"""House module"""

import os
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
    update_date: Optional[str] = None

    def __init__(
        self,
        address: Optional[str] = None,
        url: Optional[str] = None,
        fields: Optional[list[str]] = None,
    ):
        self.address = address
        self.url = url
        if fields:
            self.fill_from_fields(fields)

    field_mapping = {
        "Address": "address",
        "Postcode": "postcode",
        "City": "city",
        "Price": "price",
        "House type": "house_type",
        "Living size": "living_size",
        "Rooms": "rooms",
        "Bedrooms": "bedrooms",
        "URL": "url",
        "Year": "year",
        "Plot area": "plot_area",
        "Registration date": "registration_date",
        "Location": "location",
        "Update date": "update_date",
    }

    def fill_from_fields(self, fields: list[str]):
        """Fill object with fields"""
        for (
            field,
            mapping,
        ) in self.field_mapping.items():
            if field in fields:
                setattr(self, mapping, fields[field])

    def fields(self, update: Optional[bool] = None):
        """Return fields of the object"""
        fields = {}
        for (
            field,
            mapping,
        ) in self.field_mapping.items():
            if hasattr(self, mapping):
                value = getattr(self, mapping)
                if isinstance(value, datetime):
                    value = value.strftime("%Y-%m-%d")
                fields[field] = value
        if update:
            fields["Update date"] = datetime.today().strftime("%Y-%m-%d")
        return fields

    def record(self, update: Optional[bool] = None):
        """Return records with fields"""
        return {"fields": self.fields(update)}

    def html_path(self):
        """Return path for HTML storage"""
        address = self.address.replace("/", ",")
        return os.path.abspath(os.path.join("extract", f"{address}.html"))

    def __str__(self):
        return f"{self.address}"

    def __repr__(self):
        return self.__str__()
