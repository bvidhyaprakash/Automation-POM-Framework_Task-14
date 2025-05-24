import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# This setup is common for all the test
@pytest.fixture()
def driver_setup():
    # Initialize the driver setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver # this splits the function into setup and teardown parts.

    # teardown method
    driver.quit()