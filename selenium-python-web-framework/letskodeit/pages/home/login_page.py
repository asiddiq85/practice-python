import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.click_on_element(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.send_data(email, self._email_field)

    def enterPassword(self, password):
        self.send_data(password, self._password_field)

    def clickLoginButton(self):
        self.click_on_element(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.wait_for_element("//div[@id='navbar']//li[@class='dropdown']",
                              locatorType="xpath")
        result = self.is_element_present(locator="//div[@id='navbar']//li[@class='dropdown']",
                                         locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.is_element_present(locator="//div[contains(text(),'Invalid email or password')]",
                                         locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verify_page_title("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.wait_for_element(locator="//div[@id='navbar']//a[@href='/sign_out']",
                                                  locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=logoutLinkElement)
        self.click_on_element(locator="//div[@id='navbar']//a[@href='/sign_out']",
                              locatorType="xpath")

    def clearFields(self):
        emailField = self.get_element(locator=self._email_field)
        emailField.clear()
        passwordField = self.get_element(locator=self._password_field)
        passwordField.clear()
