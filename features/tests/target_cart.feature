# Created by sruthi at 12/31/2024
Feature: cart should be empty


  Scenario: open the target main page
    Given open the target main page
    When click on cart
    Then Verify that cart is empty