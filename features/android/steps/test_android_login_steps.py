from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.login_page import AndroidLoginPage

# Assign all scenarios from feature file to this file
scenarios('android/login_android.feature')

@given("I am on the login page", target_fixture="login_page")
def android_login_page(driver):
    return AndroidLoginPage(driver)


@when(parsers.re(r'I enter username "(?P<username>.*)"'))
def android_enter_username(login_page, username):
    login_page.enter_username(username)


@when(parsers.re(r'I enter password "(?P<password>.*)"'))
def android_enter_password(login_page, password):
    login_page.enter_password(password)


@when("I click login button")
def android_click_login(login_page):
    login_page.click_login_button()


@then("I should see the home page")
def android_verify_home_page(login_page):
    assert login_page.is_home_page_displayed()


@then(parsers.parse('I should see error message "{message}"'))
def android_verify_error_message(login_page, message):
    assert login_page.get_error_message() == message
