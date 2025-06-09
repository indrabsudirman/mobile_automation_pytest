
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import os
from dotenv import load_dotenv
import allure

load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android", help="Platform to test: android or ios"
    )

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform").lower()

import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logstart(nodeid, location):
    print(f"\n===== START TEST: {nodeid} =====")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item, "_driver", None)
        if driver:
            print("📸 Test failed, take screenshot ...")
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
        else:
            print("⚠️ Driver not found in item._driver.")

    if rep.when == "call":
        duration = rep.duration
        status = rep.outcome
        nodeid = rep.nodeid

        print(f"===== END TEST: {nodeid} =====")
        print(f"Status: {status.upper()} | Duration: {duration:.2f} seconds\n")

@pytest.fixture(scope="function")
def driver(platform, request):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    

    appium_server = os.getenv("APPIUM_SERVER", "http://localhost:4723")


    if platform == "android":
        # Use os.path.abspath to get full path
        apk_path = os.path.abspath(os.path.join(root_dir, "sample_applications", "sample_login_android.apk"))
        print(f"Using APK path: {apk_path}")
        options = UiAutomator2Options()
        options.set_capability("platformName", "Android")
        options.set_capability("automationName", "UiAutomator2")
        options.set_capability("deviceName", "Infinix-X6812")
        options.set_capability("app", apk_path)
        options.set_capability("appWaitActivity", "*.*")
        options.set_capability("autoGrantPermissions", True)
        appium_server_url = appium_server

    elif platform == "ios":
        app_path = os.path.abspath(os.path.join(root_dir, "sample_applications", "sample_login_ios.app"))
        print(f"Using .app path: {app_path}")
        options = XCUITestOptions()
        options.set_capability("platformName", "iOS")
        options.set_capability("automationName", "XCUITest")
        options.set_capability("deviceName", "iPhone 16 Pro")
        options.set_capability("platformVersion", "18.0")
        options.set_capability("app", app_path)
        options.set_capability("autoAcceptAlerts", True)
        appium_server_url = appium_server

    else:
        raise ValueError("Platform must be 'android' or 'ios'")

    driver = webdriver.Remote(appium_server_url, options=options)
    request.node._driver = driver
    yield driver
    driver.quit()
