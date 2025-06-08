@android @login
Feature: Login Functionality - Android

  @loginPositive
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "indra.indrabayu@gmail.com"
    And I enter password "MyPassword@12345"
    And I click login button
    Then I should see the home page

  @loginNegative
  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "test"
    And I enter password "test"
    And I click login button
    Then I should see error message "Email atau password salah."

  @loginNegative
  Scenario: Failed login with empty credentials
    Given I am on the login page
    When I enter username ""
    And I enter password ""
    And I click login button
    Then I should see error message "Email dan password harus diisi."

  @loginNegative
Scenario: Failed login with empty username
  Given I am on the login page
  When I enter username ""
  And I enter password "test"
  And I click login button
  Then I should see error message "Email dan password harus diisi."

@loginNegative
Scenario: Failed login with empty password
  Given I am on the login page
  When I enter username "test"
  And I enter password ""
  And I click login button
  Then I should see error message "Email dan password harus diisi.fff"
