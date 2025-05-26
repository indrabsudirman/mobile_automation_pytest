from pytest_bdd import given, when, then
from pages.ios.login_page import IOSLoginPage

@given("I am on the login page", target_fixture="login_page")
def ios_login_page(driver):
    return IOSLoginPage(driver)

@when("I enter username "<username>"")
def ios_enter_username(login_page, username):
    login_page.enter_username(username)

@when("I enter password "<password>"")
def ios_enter_password(login_page, password):
    login_page.enter_password(password)

@when("I click login button")
def ios_click_login(login_page):
    login_page.click_login_button()

@then("I should see the home page")
def ios_verify_home(login_page):
    assert login_page.is_home_page_displayed()