# Created by sruthi at 12/31/2024
Feature: verify that a logged out user can navigate to Sign In

  Scenario: Verify Sign In form opened
    Given Open Target Page
    When Click on Sign In
    Then verify sign in page