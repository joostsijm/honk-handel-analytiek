"""Transform module"""

from datetime import datetime 

from bs4 import BeautifulSoup

from house import House


class Transform:
    """Transform class"""

    def __init__(self, house: House, html_path: str = None):
        self.__house = house
        self.__html_path = html_path

    def execute(self, extracted_data=None):
        """Tranform houses from file"""
        if not extracted_data:
            with open(self.__html_path, "r", encoding="utf-8") as extracted_file:
                extracted_data = extracted_file.read()
        soup = BeautifulSoup(extracted_data, "html.parser")
        features = {}
        for feature_element in soup.select(".kenmerk-item"):
            label = feature_element.select_one(".kenmerk-label").text
            value = feature_element.select_one(".kenmerk-value").text
            features[label] = value
            print(f"{label:25}: {value}")
        if "Perceeloppervlakte" in features:
            self.__house.plot_area = int(features["Perceeloppervlakte"].replace(" m²", ""))
        if "Aanmelddatum" in features:
            self.__house.registration_date = datetime.strptime(features["Aanmelddatum"], "%d-%m-%Y")
        if "Bouwjaar" in features:
            self.__house.year = int(features["Bouwjaar"])
        if "Ligging" in features:
            self.__house.location = features["Ligging"]

        return self.__house
