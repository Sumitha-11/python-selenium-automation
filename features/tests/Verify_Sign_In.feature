# Created by USER at 25-11-2021
Feature:Test scernario for Sign-In Page


  Scenario:Logged out user sees Sign in page when clicking Orders
      Given open Amazon Page
      When click on Orders and Returns
      Then Sign-In page should appear.
