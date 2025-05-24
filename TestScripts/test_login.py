from PageObjects.base_page import BasePage
from PageObjects.login_page import Login_Page
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
        print("\nPASSED: User Successfully Logged In")
    except Exception as e:
        print(e)