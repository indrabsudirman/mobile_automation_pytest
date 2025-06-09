from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IOSLoginPage(BasePage):
    # Locators - used accessibility ID for iOS
    USERNAME_FIELD = ("accessibility id", "login.email")
    PASSWORD_FIELD = ("accessibility id", "login.password")
    LOGIN_BUTTON = ("accessibility id", "login.button")
    ERROR_MESSAGE = ("accessibility id", "login.message")
    HOME_PAGE_INDICATOR = ("accessibility id", "home.message")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.input_text(self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        self.input_text(self.PASSWORD_FIELD, password)


    def click_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def is_home_page_displayed(self):
        return self.find_element(self.HOME_PAGE_INDICATOR).is_displayed()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()