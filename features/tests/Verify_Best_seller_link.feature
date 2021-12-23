# Created by USER at 08-12-2021
Feature: Test scenario for verifying 5 Bestseller links

  Scenario: User should click Bestseller link and verify 5 links are present
    Given Open Amazon page
    Then Click on BestSellers Page
    Then verify 5 links are present

  Scenario: User should click on the Bestseller link and click on sub-links and verify new page opens
    Given Open Amazon page
    Then Click on BestSellers Page
    And Click on sub-links
    Then verify newpage is opened

