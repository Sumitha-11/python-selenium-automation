# Created by USER at 04-01-2022
Feature: Test for verifying hover function

  Scenario: User hover over language and verify spanish option is present
    Given Open Amazon page
    When  Hover over language options
    Then verify Spanish option present

  Scenario: User need to hover over new arrivals of the product
    Given Open Amazon Product B074TBCSC8 Page
    When Hover over new arrivals
    Then Verify 5 category are present

  Scenario: User need to hover over new arrivals and verify women category is  present
    Given Open Amazon Product B074TBCSC8 Page
    When Hover over new arrivals
    Then Verify women category is present