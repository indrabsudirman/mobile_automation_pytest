import pytest
from appium import webdriver
import os

def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android", help="Platform to test: android or ios"
    )

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform").lower()

@pytest.fixture(scope="session")
def driver(platform):
    desired_caps = {}

    root_dir = os.path.dirname(os.path.abspath(__file__))  # path ke direktori conftest.py
    apk_path = os.path.join(root_dir, "2.2.0.apk")  # sesuaikan nama apk-n

    if platform == "android":
        desired_caps.update({
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Infinix-X6812",
            "app": apk_path,  # Ganti dengan path ke APK
            "appWaitActivity": "*.*",
            "autoGrantPermissions": True
        })
        appium_server_url = "http://localhost:4723"

    elif platform == "ios":
        desired_caps.update({
            "platformName": "iOS",
            "automationName": "XCUITest",
            "deviceName": "iPhone Simulator",
            "platformVersion": "15.5",  # Ganti dengan versi iOS sesuai simulator kamu
            "app": "/path/to/your/app.app",  # Ganti dengan path ke .app atau .ipa
            "noReset": True
        })
        appium_server_url = "http://localhost:4723"

    else:
        raise ValueError("Platform harus 'android' atau 'ios'")

    driver = webdriver.Remote(appium_server_url, desired_caps)
    yield driver
    driver.quit()
