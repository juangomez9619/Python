from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as select


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_by_visibility(self):
        try:
            web_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            return web_element
        except TimeoutException:
            print('Element is not visible. Timeout')


    def find_by_presence(self):
        try:
            web_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator=self.locator)
            )
            return web_element
        except TimeoutException:
            print('Element is not present. Timeout')

    def wait_to_be_clickable(self):
        try:
            web_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator=self.locator)
            )
            return web_element
        except TimeoutException:
            print('Element is not clickable. Timeout')


    def set_text(self, txt):
        web_element = self.find_by_visibility()
        web_element.send_keys(txt)
        return None

    def click_visible(self):
        web_element = self.find_by_visibility()
        web_element.click()
        return None

    def click_present(self):
        web_element = self.find_by_presence()
        web_element.click()
        return None

    def attribute_visible(self, attr_name):
        web_element = self.wait_to_be_clickable()
        attribute = web_element.get_attribute(attr_name)
        return attribute

    def select_dropdown_by_value(self, value):
        element = select(self.find_by_presence())
        element.select_by_value(value)
        return None

    def select_dropdown_by_visible_text(self, value):
        element = select(self.find_by_presence())
        element.select_by_visible_text(value)
        return None

    def clear_element(self):
        element = self.find_by_visibility()
        element.clear()

    def get_text(self):
        web_element = self.find_by_visibility()
        text = web_element.text
        return text
