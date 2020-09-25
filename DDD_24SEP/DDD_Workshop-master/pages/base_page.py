from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator


class BasePage(object):
    url = None

    def __init__(self, driver, data_structure):
        self.driver = driver
        self.data_structure = data_structure

    def go_to(self):
        self.driver.get(self.url)

