from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage
from .header_component import HeaderComponent


class LandingPage(BasePage):
    def __init__(self, driver, data_structure):
        super().__init__(driver, data_structure)
        self.url = 'http://automationpractice.com/index.php'

    # mapear landing page
