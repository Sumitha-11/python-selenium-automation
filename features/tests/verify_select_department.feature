# Created by USER at 04-01-2022
Feature: Test for verifying select feature for dropdown

  Scenario: User need to select book department from the dropdown
    Given Open Amazon page
    When Select department by alias stripbooks
    And Search for Faust
    And Click on search button
    Then Verify books department is selected

  Scenario: User need to select Amazon Pharmacy department from the dropdown
    Given Open Amazon page
    When Select department by alias amazon-pharmacy
    And Search for vitamin d3
    And Click on search button
    Then Verify "vitamin d3" text is present

  Scenario: User need to select appliances department from the dropdown
    Given Open Amazon page
    When Select department by alias appliances
    And Search for Fridge
    And Click on search button
    Then Verify appliances department is selected





