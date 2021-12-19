# Created by USER at 17-12-2021
Feature: Test for wholefood product name

  Scenario: User need to verify "Regular" in all product and print the name of the product
    Given Open Amazon Wholefood page
    Then Verify Regular word in all product
    Then Print the name of the product