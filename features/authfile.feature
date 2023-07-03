# Created by Atpl-15 at 20-06-2023
Feature:  Authentication API Validation
  # Enter feature description here
  Scenario: session management check
    Given We have API get profile
    When We hit get profile API with Auth
    Then Status code of response should be 200

