# Created by Atpl-15 at 16-06-2023
Feature: Verify if user exist or not using checkUser API
  # Enter feature description here
  @smoke
  Scenario: Verify user Functionality
    Given The User Details which needs to be check
    When We execute user exist PostAPI method
    Then User Checked successfully
    @regression
    Scenario Outline: Verify user Functionality
      Given The User Details which <user_name> check
      When We execute user exist PostAPI method
      Then User Checked successfully
      Examples:
        | user_name  |
        | 9265589161 |
        | 1452588458 |
        | 9909020991 |
        | 1452588458 |