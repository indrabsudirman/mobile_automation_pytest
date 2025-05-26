import pytest

@pytest.mark.common
def test_app_version(driver):
    """Test versi aplikasi"""
    assert driver.execute_script('mobile: getAppStrings')['version'] == '1.0.0'

@pytest.mark.common
def test_network_connection(driver):
    """Test koneksi jaringan"""
    assert driver.network_connection != 0