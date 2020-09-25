from .locator import Locator
from .base_element import BaseElement
from .base_page import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime


class SignupPage(BasePage):
    def __init__(self, driver, data_structure):
        super().__init__(driver, data_structure)

    # properties
    @property
    def register_btn(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    # event object
    @property
    def register_danger_alert(self):
        locator = Locator(by=By.XPATH, value='//*[@class=\'alert alert-danger\']')
        return BaseElement(self.driver, locator)


    @property
    def mr_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def mrs_input(self):
        locator = Locator(by=By.ID, value='id_gender2')
        return BaseElement(self.driver, locator)

    @property
    def customer_first_name_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def customer_last_name_input(self):
        locator = Locator(by=By.ID, value='customer_lastname')
        return BaseElement(self.driver, locator)

    @property
    def mail_input(self):
        locator = Locator(by=By.ID, value='email')
        return BaseElement(self.driver, locator)

    @property
    def password_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def days_select(self):
        locator = Locator(by=By.ID, value='days')
        return BaseElement(self.driver, locator)

    @property
    def months_select(self):
        locator = Locator(by=By.ID, value='months')
        return BaseElement(self.driver, locator)

    @property
    def years_select(self):
        locator = Locator(by=By.ID, value='years')
        return BaseElement(self.driver, locator)

    @property
    def first_name_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def last_name_input(self):
        locator = Locator(by=By.ID, value='lastname')
        return BaseElement(self.driver, locator)

    @property
    def company_input(self):
        locator = Locator(by=By.ID, value='company')
        return BaseElement(self.driver, locator)

    @property
    def address_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    @property
    def city_input(self):
        locator = Locator(by=By.ID, value='city')
        return BaseElement(self.driver, locator)

    @property
    def state_select(self):
        locator = Locator(by=By.ID, value='id_state')
        return BaseElement(self.driver, locator)

    @property
    def zip_input(self):
        locator = Locator(by=By.ID, value='postcode')
        return BaseElement(self.driver, locator)

    @property
    def country_select(self):
        locator = Locator(by=By.ID, value='id_country')
        return BaseElement(self.driver, locator)

    @property
    def home_phone_input(self):
        locator = Locator(by=By.ID, value='phone')
        return BaseElement(self.driver, locator)

    @property
    def mobile_phone_input(self):
        locator = Locator(by=By.ID, value='phone_mobile')
        return BaseElement(self.driver, locator)

    @property
    def alias_input(self):
        # **********************************************************
        # 2. Completar locator
        # **********************************************************
        locator = "Completar"
        return BaseElement(self.driver, locator)

    def set_title(self, value):
        if value.lower() == 'mr':
            self.mr_input.click_present()
        elif value.lower() == 'mrs':
            self.mrs_input.click_present()

    def set_first_name(self, value):
        self.customer_first_name_input.set_text(value)

    def set_last_name(self, value):
        self.customer_last_name_input.set_text(value)

    def set_password(self, value):
        self.password_input.set_text(value)

    def set_date_birth(self, value):
        if value != "":
            if str(type(value)) != '<class \'datetime.date\'>':
                obj_date = datetime.strptime(value, '%Y-%m-%d')
            else:
                obj_date = value
            self.days_select.select_dropdown_by_value(str(obj_date.day))
            self.months_select.select_dropdown_by_value(str(obj_date.month))
            self.years_select.select_dropdown_by_value(str(obj_date.year))

    def set_first_name_address(self, value):
        self.first_name_input.set_text(value)

    def set_last_name_address(self, value):
        self.last_name_input.set_text(value)

    def set_company(self, value):
        self.company_input.set_text(value)

    def set_address(self, value):
        self.address_input.set_text(value)

    def set_city(self, value):
        self.city_input.set_text(value)

    def select_state(self, value):
        if value != "":
            self.state_select.select_dropdown_by_visible_text(value)

    def set_zip_code(self, value):
        if value != "":
            self.zip_input.set_text(str(int(value)))

    def select_country(self, value):
        if value != "":
            self.country_select.select_dropdown_by_visible_text(value)

    def set_home_phone(self, value):
        if value != "":
            self.home_phone_input.set_text(str(int(value)))

    def set_mobile_phone(self, value):
        if value != "":
            self.mobile_phone_input.set_text(str(int(value)))

    def set_alias(self, value):
        self.alias_input.set_text(value)

    def register_account(self, info_list):
        #************************************************
        #.3 Bonus
        #encontrar el fallo de la logica de esta funcion
        #Pista: hay se esta haciendo un paso antes de lo
        #debido.
        #************************************************
        self.register_btn.click_visible()
        self.set_title(info_list[self.data_structure['title']])
        self.set_first_name(info_list[self.data_structure['name']])
        self.set_last_name(info_list[self.data_structure['last_name']])
        self.set_password(info_list[self.data_structure['password']])
        self.set_date_birth(info_list[self.data_structure["date_of_birth"]])
        self.set_company(info_list[self.data_structure["company"]])
        self.set_address(info_list[self.data_structure["address"]])
        self.set_city(info_list[self.data_structure["city"]])
        self.select_state(info_list[self.data_structure["state"]])
        self.set_zip_code(info_list[self.data_structure["zip_code"]])
        self.select_country(info_list[self.data_structure["country"]])
        self.set_home_phone(info_list[self.data_structure["home_phone"]])
        self.set_mobile_phone(info_list[self.data_structure["mobile_phone"]])
        self.alias_input.clear_element()
        self.set_alias(info_list[self.data_structure["alias"]])