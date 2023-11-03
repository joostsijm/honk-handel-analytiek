"""Extract module"""

import time
from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver import ActionChains


class Extract:
    """Extract class"""

    __username: str = None
    __password: str = None
    __html_path: Optional[str] = None

    def __init__(
        self,
        username: str,
        password: str,
        html_path: Optional[str] = None,
        wait_time: Optional[str] = 2,
    ):
        self.__username = username
        self.__password = password
        self.__html_path = html_path
        self.__wait_time = wait_time
        self.__driver = webdriver.Firefox()

    def execute(self):
        """Extract houses to file"""
        try:
            self.login()
            self.scroll_to_bottom()

            if self.__html_path:
                with open(self.__html_path, "w", encoding="utf-8") as file:
                    file.write(self.__driver.page_source)
            return self.__driver.page_source
        finally:
            self.__driver.quit()

    def login(self):
        self.__driver.get("https://move.nl/login")
        assert "Move" in self.__driver.title
        username_input = WebDriverWait(self.__driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "username"))
        )
        username_input.clear()
        username_input.send_keys(self.__username)

        password_input = self.__driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(self.__password)

        submit = self.__driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        ActionChains(self.__driver).click(submit).perform()

        WebDriverWait(self.__driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "ant-spin-container"))
        )
        time.sleep(self.__wait_time)

    def scroll_to_bottom(self):
        last_height = self.__driver.execute_script("return document.body.scrollHeight")
        while True:
            self.__driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(self.__wait_time)
            new_height = self.__driver.execute_script(
                "return document.body.scrollHeight"
            )
            if new_height == last_height:
                break
            last_height = new_height
