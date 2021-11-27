# Created by USER at 26-11-2021
Feature: Test Scenario for orders and returns


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon Page
    When Click on Orders and Returns
    Then Sign-In page should appear.