"""Transform module"""

from typing import Optional
from bs4 import BeautifulSoup

from house import House


class Transform:
    """Transform class"""
    __html_path: Optional[str] = None

    def __init__(self, html_path: str = None):
        self.__html_path = html_path

    def execute(self, extracted_data=None):
        """Tranform houses from file"""
        if not extracted_data:
            with open(self.__html_path, "r", encoding="utf-8") as extracted_file:
                extracted_data = extracted_file.read()
        soup = BeautifulSoup(extracted_data, "html.parser")
        houses = []
        for house_element in soup.select(".ant-list-item"):
            house = House(house_element.select_one("span[class='address']").text)
            price = house_element.select_one("span[class='price']").text
            for replace in ["€ ", ".", ",- kosten koper"]:
                price = price.replace(replace, "")
            house.price = int(price)
            postcode_city = house_element.select_one(
                "span[class='post-code-city']"
            ).text.split(" ")
            house.postcode = " ".join([postcode_city[0], postcode_city[1]])
            house.city = postcode_city[2]
            detail_elements = house_element.select(".ant-descriptions-item-content")
            house.house_type = detail_elements[0].text
            house.living_size = int(detail_elements[1].text)
            house.rooms = int(detail_elements[2].text)
            house.bedrooms = int(detail_elements[3].text)
            house.url = "https://move.nl" + house_element.select_one("a")["href"]
            houses.append(house)
        return houses
