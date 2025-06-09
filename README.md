# Mobile Automation Testing Framework

This repository contains a mobile test automation framework for Android and iOS applications using Python. It is designed to support BDD-style test scenarios with robust reporting and retry mechanisms.

## 🧰 Tech Stack

### Testing Framework

- **pytest** – Test runner  
- **pytest-bdd** – BDD-style test writing (Given/When/Then)  
- **Page Object Model (POM)** – Design pattern for organizing test code by separating page structure and test logic

### Reporting

- **allure-pytest** – Generates beautiful and detailed test reports  
- **Failure screenshots** – Automatically captured and attached on test failures

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

> These apps are used as test targets to demonstrate and validate the automation framework. You can see the apps in the `sample_applications` directory. For the iOS app (.app) you need to extract it first

## 🚀 Getting Started

### Prerequisites

- Python 3.13.3
- Node.js & Appium Server
- Xcode & Android Studio (for building/running iOS and Android apps) [optional] since the .apk and .app already available in this repo
- Java (for Android tools)

### Installation

1. Clone the repository (SSH):

   ```bash
   git clone git@github.com:indrabsudirman/mobile_automation_pytest.git
   cd mobile_automation_pytest
   ```

2. Install `allure` please see [allure](https://allurereport.org/docs/install/) documentation
   
   <img width="143" alt="image" src="https://github.com/user-attachments/assets/3274b05a-1c8e-40bc-aae1-b6406c602e40" />

3. Install the dependencies via the `Pipfile` file using

   required `Python 3.13.3`

   ```bash
   pipenv install
   ```

    <img width="500" alt="image" src="https://github.com/user-attachments/assets/dcae23da-e0a1-466d-9c23-efe5c1e9a812" />



     ```bash
   pipenv shell
   ```

    <img width="962" alt="image" src="https://github.com/user-attachments/assets/a35db7fa-5728-499f-ba45-2aa26669f927" />
 

    type `exit` to exit from the virtual environment


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

   <img width="300" alt="image" src="https://github.com/user-attachments/assets/861a2765-b4a2-4569-8392-643408c656aa" />

7. Try to run the test

   ```bash
   pytest -m "android and loginNegative" --alluredir=reports/allure-results
   ```

   <img width="1337" alt="image" src="https://github.com/user-attachments/assets/d152df43-e473-4f07-be8e-10ab62a95f86" />
 

   The command above will run the test with tag `android and loginNegative` it's mean Android testcases will be execute lastly will generate the report in `reports/allure-results` directory

   <img width="1680" alt="image" src="https://github.com/user-attachments/assets/c9ca6717-15ef-4a44-832c-026b46cfec07" />

   for the ios you need to pass the `platform`
   ```bash
   pytest --platform=ios -m "ios and loginNegative" --alluredir=reports/allure-results
   ```

   <img width="1680" alt="image" src="https://github.com/user-attachments/assets/7744cf76-5a33-4bd0-9428-52d5effede43" />



9. Finally, To generate the report, please run the command below:
    
   ```bash
   allure serve reports/allure-results
   ```

    <img width="1680" alt="image" src="https://github.com/user-attachments/assets/41c13fa9-e593-40ec-8d08-d6380e504ee6" />

