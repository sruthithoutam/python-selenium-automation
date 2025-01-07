
Feature: Add Product to Cart

  Scenario: Verify Product Added to Cart
  Given open the target page
    When search for cup
    Then Verify search results shown for cup
    Then click on add to cart button
    And confirm add to cart button from navigation side
    And open cart page
   Then verify cart has 1 item(s)
