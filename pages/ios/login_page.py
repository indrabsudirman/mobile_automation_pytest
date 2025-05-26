from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IOSLoginPage(BasePage):
    # Locators - used accessibility ID for iOS
    # USERNAME_FIELD = (By.ACCESSIBILITY_ID, 'test-Username')
    # PASSWORD_FIELD = (By.ACCESSIBILITY_ID, 'test-Password')
    # LOGIN_BUTTON = (By.ACCESSIBILITY_ID, 'test-LOGIN')
    # ERROR_MESSAGE = (By.ACCESSIBILITY_ID, 'test-Error message')

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