from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.dashboard_page_locator import Dashboard_Page_Locator

class Dashboard_Page(BasePage):
    COMMON_POPUP = (By.XPATH, Dashboard_Page_Locator.common_popup_main_container)
    COMMON_POPUP_CLOSE_BUTTON = (By.XPATH, Dashboard_Page_Locator.popup_close_button)
    USER_PROFILE = (By.XPATH, Dashboard_Page_Locator.user_profile_dropdown)
    LOGOUT_OPTION = (By.XPATH, Dashboard_Page_Locator.logout_option)

    # to close the popup after user logged in to the Dashboard page
    def close_common_popup(self):
        try:
            if self.is_visible(self.COMMON_POPUP):
                self.click(self.COMMON_POPUP_CLOSE_BUTTON)
        except Exception as e:
            print("/n",e)

    # for logout user
    def logout_user(self):
        try:
            self.click(self.USER_PROFILE)
            if self.is_visible(self.LOGOUT_OPTION):
                self.click(self.LOGOUT_OPTION)
        except Exception as e:
            print("\n", e)