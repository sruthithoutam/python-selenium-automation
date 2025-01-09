# Created by sruthi at 1/3/2025
Feature:  Product Search on Target
  # Enter feature description here

  Scenario: Search for a product and verify results
  Given open the target page
  When search for mug
  Then i should see the results for mug