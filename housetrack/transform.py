"""Transform module"""

from bs4 import BeautifulSoup

from house import House


def execute(html_path):
    """Tranform houses from file"""
    with open(html_path, "r", encoding="utf-8") as extracted_file:
        soup = BeautifulSoup(extracted_file.read(), "html.parser")
    house_elements = soup.select(".ant-spin-container > div > div")
    houses = []
    for house_element in house_elements:
        price = house_element.select_one("span[class='price']").text
        for replace in ["€ ", ".", ",- kosten koper"]:
            price = price.replace(replace, "")
        price = int(price)
        house = House(
            house_element.select_one("span[class='address']").text,
            house_element.select_one("span[class='post-code-city']").text,
            price,
        )
        houses.append(house)
    return houses
