# Created by Atpl-15 at 16-06-2023
Feature: Verify if login successfully or not using login API
  # Enter feature description here

  Scenario: Verify Login Functionality
    Given The login Details which needs to be logged in to App
    When We execute login PostAPI method
    Then Login successfully

    Scenario: session management check
      Given We have API get profile
      When We hit get profile API with Auth
      Then Status code of response should be 200
