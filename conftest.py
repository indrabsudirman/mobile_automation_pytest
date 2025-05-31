
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
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
    root_dir = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.join(root_dir, "2.2.0.apk")

    if platform == "android":
        options = UiAutomator2Options()
        options.set_capability("platformName", "Android")
        options.set_capability("automationName", "UiAutomator2")
        options.set_capability("deviceName", "Infinix-X6812")
        options.set_capability("app", apk_path)
        options.set_capability("appWaitActivity", "*.*")
        options.set_capability("autoGrantPermissions", True)
        appium_server_url = "http://localhost:4723"

    elif platform == "ios":
        options = XCUITestOptions()
        options.set_capability("platformName", "iOS")
        options.set_capability("automationName", "XCUITest")
        options.set_capability("deviceName", "iPhone Simulator")
        options.set_capability("platformVersion", "15.5")
        options.set_capability("app", "/path/to/your/app.app")
        options.set_capability("noReset", True)
        appium_server_url = "http://localhost:4723"

    else:
        raise ValueError("Platform harus 'android' atau 'ios'")

    driver = webdriver.Remote(appium_server_url, options=options)
    yield driver
    driver.quit()
