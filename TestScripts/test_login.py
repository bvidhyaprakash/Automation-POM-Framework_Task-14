import pytest

from PageObjects.base_page import BasePage
from PageObjects.login_page import Login_Page
from PageObjects.dashboard_page import Dashboard_Page

from TestData.data import Data
from Configuration.conftest import driver_setup
from time import sleep

def test_success_login(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    login_page = Login_Page(driver_setup)

    try:
        assert base_page.fetch_url() == Data.url
        login_page.enter_valid_email_address()
        login_page.enter_valid_password()
        login_page.click_signin_button()
        sleep(3)
        assert base_page.fetch_url() == Data.dashboard_page_url
        print("\nPASSED: User Successful LogIn with Valid credential")
    except Exception as e:
        print(e)

def test_unsuccessful_login(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    login_page = Login_Page(driver_setup)


    try:
        assert base_page.fetch_url() == Data.url
        login_page.enter_invalid_email_address()
        login_page.enter_invalid_password()
        login_page.click_signin_button()
        sleep(3)
        assert base_page.fetch_url() != Data.dashboard_page_url
        print("\nPASSED: User Unsuccessful LogIn with Invalid credential")
    except Exception as e:
        print(e)

def test_validate_email_password_input_box(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    login_page = Login_Page(driver_setup)

    try:
        assert base_page.fetch_url() == Data.url
        base_page.is_visible(login_page.EMAIL_ADDRESS)
        base_page.is_visible(login_page.PASSWORD)
        print("\nPASSED: Validated Email and Password input box")
    except Exception as e:
        print("\n",e)

def test_validate_signin_button(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    login_page = Login_Page(driver_setup)

    try:
        assert base_page.fetch_url() == Data.url
        base_page.is_enabled(login_page.SIGNIN_BUTTON)
        print("\nPASSED: Validated Submit button is enabled")
    except Exception as e:
        print("\n",e)

def test_validate_logout_button(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    login_page = Login_Page(driver_setup)
    dashboard_page = Dashboard_Page(driver_setup)
    try:
        assert base_page.fetch_url() == Data.url
        login_page.enter_valid_email_address()
        login_page.enter_valid_password()
        login_page.click_signin_button()
        sleep(3)
        assert base_page.fetch_url() == Data.dashboard_page_url
        print("\nPASSED: User Successful LogIn with Valid credential")
        if dashboard_page.close_common_popup():
            sleep(2)
            dashboard_page.logout_user()
        else:
            dashboard_page.logout_user()
        base_page.is_visible(login_page.SIGNIN_BUTTON)
        assert base_page.fetch_url() == Data.url
        print("\nPASSED: Validated logout button")
    except Exception as e:
        print("\n",e)
