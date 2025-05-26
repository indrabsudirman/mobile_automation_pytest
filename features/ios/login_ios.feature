@ios
Feature: Login Functionality - iOS
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "testuser"
    And I enter password "password123"
    And I click login button
    Then I should see the home page