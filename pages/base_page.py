from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
    
    def find_element(self, locator):
        if isinstance(locator, tuple):
            by, value = locator
            if by == "accessibility id":
                return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
            elif by == "id":
                return self.driver.find_element(AppiumBy.ID, value)
            elif by == "xpath":
                return self.driver.find_element(AppiumBy.XPATH, value)
        else:
            raise ValueError("Invalid locator type")
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
  
    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False