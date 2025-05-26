from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AndroidLoginPage(BasePage):
    # Locators - used resources ID for Android
    USERNAME_FIELD = (By.ID, "com.example.android:id/username")
    PASSWORD_FIELD = (By.ID, "com.example.android:id/password")
    LOGIN_BUTTON = (By.ID, "com.example.android:id/loginButton")
    ERROR_MESSAGE = (By.ID, "com.example.android:id/errorMessage")
    HOME_PAGE_INDICATOR = (By.ID, "com.example.android:id/homePageIndicator")  # Tambahkan ini

    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_username(self, username):
        self.input_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
    def is_home_page_displayed(self):  # Tambahkan method ini
        return self.is_element_displayed(self.HOME_PAGE_INDICATOR)