from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage


class HeaderComponent(BasePage):
    # Properties
    # first header
    @property
    def sign_in_btn(self):
        locator = Locator(by=By.CLASS_NAME, value='login')
        return BaseElement(self.driver, locator)

    @property
    def sign_contact_us_btn(self):
        locator = Locator(by=By.XPATH, value='//a[text() = \'Contact us\']')
        return BaseElement(self.driver, locator)

    # search header
    @property
    def search_input(self):
        locator = Locator(by=By.ID, value='search_query_top')
        return BaseElement(self.driver, locator)

    @property
    def search_btn(self):
        locator = Locator(by=By.XPATH, value='//button[@name=\'submit_search\']')
        return BaseElement(self.driver, locator)

    @property
    def cart_btn(self):
        locator = Locator(by=By.XPATH, value='//a[@title=\'View my shopping cart\']')
        return BaseElement(self.driver, locator)

    # cateogories header
    @property
    def women_btn(self):
        locator = Locator(by=By.XPATH, value='//a[@title=\'Women\']')
        return BaseElement(self.driver, locator)

    @property
    def dresses_btn(self):
        locator = Locator(by=By.XPATH, value='//a[@title=\'Dresses\']')
        return BaseElement(self.driver, locator)

    @property
    def tshirts_btn(self):
        locator = Locator(by=By.XPATH, value='//a[@title=\'T - shirts\']')
        return BaseElement(self.driver, locator)

    # Behavior
    def search_something(self, value):
        BaseElement.set_text(self.search_input, value)
        BaseElement.click_visible(self.search_btn)
