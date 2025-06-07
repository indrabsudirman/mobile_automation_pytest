# Sample Login Android

This project is part of the main repository: **[Mobile Automation Pytest](https://github.com/indrabsudirman/mobile_automation_pytest)**

---

**Sample Login Android** is a simple example project built using **Kotlin** and the latest **Jetpack Compose** technology for modern Android development.

## 🔍 Accessibility Support for Appium Testing

This project uses **Accessibility IDs** as UI element locators to support **Appium automation testing**.

### Why Accessibility IDs?

- **Recommended Locator**: Accessibility IDs are the preferred locator strategy for Appium due to their **robustness**.
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

![Accessibility IDs vs XPath](/SampleLoginAndroid/images/android-accessibility-id.png 'Accessibility IDs')

### Using XPath

![Accessibility IDs vs XPath](/SampleLoginAndroid/images/android-xpath.png 'XPath')

## 🛠️ Tech Stack

- **Kotlin**
- **Jetpack Compose**
- **AndroidX**
- **Accessibility Identifiers** for testing

## 🤖 Automated Testing

Designed with automation in mind. You can easily integrate this app with Appium scripts by targeting components via their `contentDescription` using:

```kotlin
Modifier.semantics { contentDescription = "your_accessibility_id" }
```
