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
  - **Accessibility IDs for robust automation**
- **Kotlin (Android)**
  - **Jetpack Compose**
  - **Accessibility IDs for robust automation**

These apps are used as test targets to demonstrate and validate the automation framework.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js & Appium Server
- Xcode & Android Studio (for building/running iOS and Android apps)
- Java (for Android tools)

### Installation

1. Clone the repository (SSH):
   ```bash
   git clone git@github.com:indrabsudirman/mobile_automation_pytest.git
   cd mobile_automation_pytest
   ```
