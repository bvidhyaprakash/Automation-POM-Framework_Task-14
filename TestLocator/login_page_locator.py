"""
contains all the locator for the Login Page
"""

class Login_Page_Locator:
    email_locator = "//input[@placeholder='Enter your mail']" # xpath
    password_locator = "//input[@placeholder='Enter your password ']" # xpath
    signin_button_locator = ".primary-btn.sign-in-pad" # class name