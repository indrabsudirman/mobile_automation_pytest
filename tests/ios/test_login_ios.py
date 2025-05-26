import pytest
from pages.ios.login_page import IOSLoginPage

@pytest.mark.ios
def test_successful_login_ios(driver):
    """Test login berhasil di iOS"""
    login_page = IOSLoginPage(driver)
    login_page.enter_credentials('username', 'password')
    assert login_page.is_home_page_displayed()

@pytest.mark.ios
def test_failed_login_ios(driver):
    """Test login gagal di iOS"""
    login_page = IOSLoginPage(driver)
    login_page.enter_credentials('wrong', 'wrong')
    assert login_page.is_error_message_displayed()