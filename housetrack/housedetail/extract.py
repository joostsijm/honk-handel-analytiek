"""Extract module"""

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from house import House


class Extract:
    """Extract class"""

    def __init__(
        self, username: str, password: str, house: House, html_path: str = None
    ):
        self.__username = username
        self.__password = password
        self.__house = house
        self.__html_path = html_path

    def execute(self):
        """Extract houses to file"""
        driver = webdriver.Firefox()
        try:
            driver.get("https://move.nl/login")
            assert "Move" in driver.title
            username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.clear()
            username_input.send_keys(self.__username)

            password_input = driver.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(self.__password)

            button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            ActionChains(driver).click(button).perform()

            username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ant-spin-container"))
            )
            time.sleep(1)
            driver.get(self.__house.url)
            time.sleep(2)
            if self.__html_path:
                with open(self.__html_path, "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
            return driver.page_source
        finally:
            driver.quit()
