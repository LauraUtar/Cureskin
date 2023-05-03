# Created by laurautarbayeva at 4/26/23
Feature: Verify Price filter Functionality

  Scenario:User can change the price filter
    Given Open cureskin homepage
    When Close popup window
    Then Click on Shop All section
    And Adjust the Price Filter such that there is a change in number of products
    Then Verify that number of products changes
    Then Verify that products displayed are within the Price filter
