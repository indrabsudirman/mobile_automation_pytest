# Mobile Automation Testing Framework

This repository contains a mobile test automation framework for Android and iOS applications using Python. It is designed to support BDD-style test scenarios with robust reporting and retry mechanisms.

## 🧰 Tech Stack

### Testing Framework

- **pytest** – Test runner
- **pytest-bdd** – BDD-style test writing (Given/When/Then)

### Reporting

- **allure-pytest** – Generates beautiful and detailed test reports

### Automation Tools

- **Appium-Python-Client** – Automate mobile apps with Appium
- **selenium** – For any web-based interactions if required

### Configuration Management

- **python-dotenv** – Load environment variables from `.env` files

## 📱 Application Under Test

This repository may also contain simple example apps built with:

- **Swift (iOS)**
  - **SwiftUI**
  - **Accessibility IDs for robust automation see [SampleLoginiOS](https://github.com/indrabsudirman/mobile_automation_pytest/tree/main/Sample%20Login%20iOS)**
- **Kotlin (Android)**
  - **Jetpack Compose**
  - **Accessibility IDs for robust automation see [SampleLoginAndroid](https://github.com/indrabsudirman/mobile_automation_pytest/tree/main/SampleLoginAndroid)**

These apps are used as test targets to demonstrate and validate the automation framework.

## 🚀 Getting Started

### Prerequisites

- Python 3.13.3
- Node.js & Appium Server
- Xcode & Android Studio (for building/running iOS and Android apps)
- Java (for Android tools)

### Installation

1. Clone the repository (SSH):

   ```bash
   git clone git@github.com:indrabsudirman/mobile_automation_pytest.git
   cd mobile_automation_pytest
   ```

2. Install `allure` please see [allure](https://allurereport.org/docs/install/) documentation

3. Install the dependencies via the `Pipfile` file using

   required `Python 3.13.3`

   ```bash
   pipenv install
   ```

   ```bash
   pipenv shell
   ```

If you don't have `pipenv` installed, please install it via `pipx` below (step no 4), skip this step if you already have `pipenv` installed.

4. Install [pipx](https://github.com/pypa/pipx), since I'm using macOS and have brew installed, I can use brew to install pipx:

   ```bash
   brew install pipx
   ```

   ```bash
   pipx ensurepath
   ```

   ```bash
   pipx install pipenv
   ```

   If you're using Windows or Linux, please see [pipx](https://github.com/pypa/pipx) documentation

5. Make sure you have run `appium` server, please see [appium](https://appium.io/docs/en/latest/quickstart/install/#starting-appium) documentation

6. Make sure you have run `Android Emulator` or real device. Try to run `adb devices` to check if you have any device connected and update the `ANDROID_DEVICE_NAME` in the `.env` file.

7. Try to run the test

   ```bash
   pytest -m "loginNegative" -q --disable-warnings --alluredir=reports/allure-results
   ```

   The command above will run the test with tag `loginNegative` in Android and will generate the report in `reports/allure-results` directory

8. Finally, To generate the report, please run the command below:
   ```bash
   allure serve reports/allure-results
   ```
