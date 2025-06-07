# Sample Login iOS

This project is part of the main repository: **[Mobile Automation Pytest](https://github.com/indrabsudirman/mobile_automation_pytest)**

---

**Sample Login iOS** is a simple example app built using **SwiftUI**, showcasing the use of modern declarative UI patterns for iOS development.

## 🔍 Accessibility Support for Appium Testing

This project uses **Accessibility Identifiers (Accessibility IDs)** to support **Appium automation testing**.

### Why Accessibility IDs?

- **Recommended Locator**: Accessibility IDs are the preferred locator strategy for Appium due to their **stability and reliability**.
- **Faster than XPath**: Accessibility IDs perform significantly better than XPath-based locators.

See the comparison screenshot below:

| Aspect         | Accessibility ID                     | XPath                                              |
| -------------- | ------------------------------------ | -------------------------------------------------- |
| Speed          | Faster                               | Slower                                             |
| Readability    | Easy to read and understand          | More complex and harder to read                    |
| Maintenance    | Easy to maintain and update          | Harder to maintain due to DOM structure dependency |
| Reliability    | More reliable and stable             | Vulnerable to UI structure changes                 |
| Implementation | Requires adding specific identifiers | Can be used directly without UI modification       |

### Using Accessibility IDs

![Accessibility IDs vs XPath](/Sample%20Login%20iOS/images/accessibility-id.png 'Accessibility IDs')

### Using XPath

![Accessibility IDs vs XPath](/Sample%20Login%20iOS/images/xpath_locator.png 'XPath')

## 🛠️ Tech Stack

- **Swift**
- **SwiftUI**
- **Accessibility Identifiers** for testing

## 🤖 Automated Testing

This app is designed with automation in mind. UI elements include accessibility identifiers like:

```swift
Text("Login Page").accessibilityIdentifier("login.title")
```
