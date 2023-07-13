"""Transform module"""

from typing import Optional
from datetime import datetime

from bs4 import BeautifulSoup

from house import House


class Transform:
    """Transform class"""

    __houses: list[House] = None

    def __init__(self, houses: list[House]):
        self.__houses = houses

    def execute(self, extracted_data=None):
        """Tranform houses from file"""
        for house in self.__houses:
            if not extracted_data:
                with open(house.html_path(), "r", encoding="utf-8") as extracted_file:
                    extracted_data = extracted_file.read()
            soup = BeautifulSoup(extracted_data, "html.parser")
            features = {}
            for feature_element in soup.select(".kenmerk-item"):
                label = feature_element.select_one(".kenmerk-label").text
                value = feature_element.select_one(".kenmerk-value").text
                features[label] = value
                print(f"{label:25}: {value}")
            if "Perceeloppervlakte" in features:
                house.plot_area = int(features["Perceeloppervlakte"].replace(" m²", ""))
            if "Aanmelddatum" in features:
                house.registration_date = datetime.strptime(
                    features["Aanmelddatum"], "%d-%m-%Y"
                )
            if "Bouwjaar" in features:
                house.year = int(features["Bouwjaar"])
            if "Ligging" in features:
                house.location = features["Ligging"]

        return self.__houses
