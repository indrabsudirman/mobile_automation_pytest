@android @login
Feature: Login Functionality - Android

  @loginPositive
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "testuser"
    And I enter password "password123"
    And I click login button
    Then I should see the home page

  @loginNegative
  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "wronguser"
    And I enter password "wrongpass"
    And I click login button
    Then I should see error message "Invalid credentials"