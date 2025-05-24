from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def fetch_url(self):
        try:
            return self.driver.current_url
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

    def fetch_title(self):
        try:
            return self.driver.title
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
            return web_element
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

    def find_elements(self, locator):
        try:
            web_elements = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))
            return web_elements
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear() # this will clear if any text in the input area
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
            return web_element.is_displayed()
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

    def is_enabled(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
            return web_element.is_enabled()
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)