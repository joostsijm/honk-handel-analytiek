"""Transform module"""

from datetime import datetime

from bs4 import BeautifulSoup

from house import House


class Transform:
    """Transform class"""

    __houses: list[House] = None

    def __init__(self, houses: list[House]):
        self.__houses = houses

    def execute(self):
        """Tranform houses from file"""
        for house in self.__houses:
            with open(house.html_path(), "r", encoding="utf-8") as extracted_file:
                extracted_data = extracted_file.read()
            soup = BeautifulSoup(extracted_data, "html.parser")
            for feature_element in soup.select(".kenmerk-item"):
                feature_label = feature_element.select_one(".kenmerk-label").text
                if feature_label in FEATURE_TYPES:
                    (attribute_name, value_parser) = FEATURE_TYPES[feature_label]
                    setattr(
                        house,
                        attribute_name,
                        value_parser(feature_element.select_one(".kenmerk-value").text),
                    )
        return self.__houses


FEATURE_VALUES = {
    "str": lambda x: x,
    "m2": lambda x: int(x.replace(" m²", "")),
    "m3": lambda x: int(x.replace(" m³", "")),
    "date": lambda x: datetime.strptime(x, "%d-%m-%Y"),
    "int": lambda x: int(x),
}

FEATURE_TYPES = {
    "Perceeloppervlakte": ("plot_area", FEATURE_VALUES["m2"]),
    "Aanmelddatum": ("registration_date", FEATURE_VALUES["date"]),
    "Ligging": ("location", FEATURE_VALUES["str"]),
    "Energieklasse": ("energy_class", FEATURE_VALUES["str"]),
    "Kwaliteit woning": ("home_quality", FEATURE_VALUES["str"]),
    "Bouwjaar": ("year", FEATURE_VALUES["int"]),
    "Status": ("status", FEATURE_VALUES["str"]),
    "Gebouwgebonden buitenruimte": ("built_outdoor_space", FEATURE_VALUES["m2"]),
    "Externe bergruimte": ("external_storage_space", FEATURE_VALUES["m2"]),
    "Inhoud": ("volume", FEATURE_VALUES["m3"]),
    "Aantal woonlagen": ("number_of_floors", FEATURE_VALUES["str"]),
}
