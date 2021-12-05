# Created by USER at 02-12-2021
Feature: Test Scenario for Canceling orders

  Scenario: User can click on cancel order and verify cancel and orders is shown.
    Given Open Amazon customer page
    When Input cancel order into search field
    Then Click Enter button
    Then  Check cancel and orders is shown
