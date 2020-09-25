from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .header_component import HeaderComponent
from .locator import Locator


# properties

class AuthenticationPage(BasePage):
    def __init__(self, driver, data_structure):
        super().__init__(driver, data_structure)
        self.url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

    # properties


    # signup component


    @property
    def mail_signup_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def submit_signup_btn(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def signup_error_message(self):
        locator = Locator(by=By.ID, value='create_account_error')
        return BaseElement(self.driver, locator)

    # login component
    @property
    def mail_login_input(self):
        locator = Locator(by=By.ID, value='email')
        return BaseElement(self.driver, locator)

    @property
    def password_login_input(self):
        locator = Locator(by=By.ID, value='passwd')
        return BaseElement(self.driver, locator)

    @property
    def submit_login_btn(self):
        locator = Locator(by=By.ID, value='SubmitLogin')
        return BaseElement(self.driver, locator)

    # behavior
    def set_signup_mail(self, value: str):
        BaseElement.set_text(self.mail_signup_input, value)

    def set_login_mail(self, value: str):
        BaseElement.set_text(self.mail_login_input, value)

    def set_login_password(self, value: str):
        BaseElement.set_text(self.password_login_input, value)

    def submit_signup(self):
        BaseElement.click_visible(self.submit_signup_btn)

    def submit_login(self):
        BaseElement.click_visible(self.submit_login_btn)

    def signup(self, info_list: list):
        self.set_signup_mail(info_list[self.data_structure['e_mail']])
        self.submit_signup()

    def login(self, info_list: list):
        self.set_login_mail(info_list[self.data_structure['e_mail']])
        self.set_login_password(info_list[self.data_structure['password']])
        self.submit_login()
