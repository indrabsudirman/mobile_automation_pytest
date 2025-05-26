import pytest
from pages.android.login_page import AndroidLoginPage

@pytest.mark.android
def test_successful_login_android(driver):
    """Test login berhasil di Android"""
    login_page = AndroidLoginPage(driver)
    login_page.login('username', 'password')
    assert login_page.is_home_page_displayed()

@pytest.mark.android
def test_failed_login_android(driver):
    """Test login gagal di Android"""
    login_page = AndroidLoginPage(driver)
    login_page.login('wrong', 'wrong')
    assert login_page.is_error_message_displayed()