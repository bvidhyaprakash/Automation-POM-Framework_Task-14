from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.login_page_locator import Login_Page_Locator
from TestData.data import Data

class Login_Page(BasePage):
    EMAIL_ADDRESS = (By.XPATH, Login_Page_Locator.email_locator)
    PASSWORD = (By.XPATH, Login_Page_Locator.password_locator)
    SIGNIN_BUTTON = (By.CSS_SELECTOR, Login_Page_Locator.signin_button_locator)

    def enter_valid_email_address(self):
        self.enter_text(self.EMAIL_ADDRESS, Data.email)

    def enter_valid_password(self):
        self.enter_text(self.PASSWORD, Data.password)

    def enter_invalid_email_address(self):
        self.enter_text(self.EMAIL_ADDRESS, Data.invalid_email)

    def enter_invalid_password(self):
        self.enter_text(self.PASSWORD, Data.invalid_password)

    def click_signin_button(self):
        self.click(self.SIGNIN_BUTTON)