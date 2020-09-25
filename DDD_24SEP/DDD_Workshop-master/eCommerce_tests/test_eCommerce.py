import logging
from pytest import mark
from pages.landing_page import LandingPage
from pages.authentication_page import AuthenticationPage
from pages.signup_page import SignupPage


approaches_dict = {
    "EXCEL":"1",
    "SQL": "2"
}

#test definition
def test_invalid_signup(data_signup, header, browser):
    data = data_signup
    logging.warning("Test: " + data[header['test_id']])
    landing = LandingPage(driver=browser, data_structure=header)
    authentication = AuthenticationPage(driver=browser, data_structure=header)
    signup = SignupPage(driver=browser, data_structure=header)
    landing.go_to()
    authentication.go_to()
    authentication.signup(data)
    signup.register_account(data)
    result = signup.register_danger_alert.get_text().replace("\n", "")
    #*************************************
    #3. Completar test
    #Hace falto lo mas importante de un test
    #Tenga en cuenta que estamos probando que
    #el mensaje de error durante un registro
    #sea el esperado
    #*************************************

#***********************************************
#6.
class signup_form_Tests:
    #generic approach

# el approach de SQL hace parte del homework
    # @mark.parametrize('approach', approaches_dict.get("SQL"))
    # @mark.invalid_signup_sql
    # def test_invalid_signup_sql(self, browser, header, data_signup_sql):
    #     test_invalid_signup(data_signup_sql, header, browser)

    @mark.parametrize('approach', approaches_dict.get("EXCEL"))
    #*****************************************************************
    #5. Nombrar un test usando @mark
    #*****************************************************************
    def test_invalid_signup_excel(self, browser, header, data_signup_excel):
        test_invalid_signup(data_signup_excel, header, browser)