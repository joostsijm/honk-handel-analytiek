"""Extract module"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def execute(username, password, html_path):
    """Extract houses to file"""
    driver = webdriver.Firefox()
    try:
        driver.get("https://move.nl/login")
        assert "Move" in driver.title
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username.clear()
        username.send_keys(username)
        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys(password)
        button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        ActionChains(driver).click(button).perform()
        with open(html_path, "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    finally:
        driver.quit()
