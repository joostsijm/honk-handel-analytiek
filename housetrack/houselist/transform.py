"""Transform module"""

from bs4 import BeautifulSoup

from house import House


class Transform:
    """Transform class"""

    def __init__(self, html_path: str=None):
        self.__html_path = html_path

    def execute(self, extracted_data=None):
        """Tranform houses from file"""
        if not extracted_data:
            with open(self.__html_path, "r", encoding="utf-8") as extracted_file:
                extracted_data = extracted_file.read()
        soup = BeautifulSoup(extracted_data, "html.parser")
        houses = []
        for house_element in soup.select(".ant-list-item"):
            price = house_element.select_one("span[class='price']").text
            for replace in ["€ ", ".", ",- kosten koper"]:
                price = price.replace(replace, "")
            price = int(price)
            postcode_city = house_element.select_one(
                "span[class='post-code-city']"
            ).text.split(" ")
            postcode = " ".join([postcode_city[0], postcode_city[1]])
            city = postcode_city[2]
            detail_elements = house_element.select(".ant-descriptions-item-content")
            house_type = detail_elements[0].text
            living_size = int(detail_elements[1].text)
            rooms = int(detail_elements[2].text)
            bedrooms = int(detail_elements[3].text)
            url = "https://move.nl" + house_element.select_one("a")["href"]

            house = House(
                house_element.select_one("span[class='address']").text,
                postcode,
                city,
                price,
                house_type,
                living_size,
                rooms,
                bedrooms,
                url
            )
            houses.append(house)
        return houses
