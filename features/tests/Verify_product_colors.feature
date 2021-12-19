# Created by USER at 15-12-2021
Feature: Test to verify different colors of the product

  Scenario Outline: User need to click through colors of the product
    Given Open Amazon Product <product_id> Page
    Then Verify user can click through <Expected_colors> of the product
    Examples:
      | product_id   | Expected_colors |
      | B07BJKRR25   | ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash', 'Indigo Wash'] |
      | B081YS2F7N   | ['Army Green', 'Black', 'Blue', 'Burgundy', 'Caramel'] |