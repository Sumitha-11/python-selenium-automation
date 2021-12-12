# Created by USER at 08-12-2021
Feature: Test Scenario for adding a product in the cart
  # Enter feature description here

  Scenario Outline: User can add a product to the cart
    Given Open Amazon page
    When Search for <product>
    And Click on search button
    Then Click on First product
    And Click on Add to cart Button
    Then Click on No thanks Button
    Then Click on cart icon
    Then Verify Cart has <Expected> item
    Examples:
    | product | Expected |
    | ipad    |   1      |

