# Created by demetriswilliams at 22/04/2021
@mastercard
Feature: As a User
  I want to add my Master Card
  So that I can start earning points when I purchase a chicken Katsu Curry


  @add_mastercard
  Scenario: As an Existing User, I want to add a Master Payment card to my account

    Given I have logged into my account
    And  I click the '+' icon under the payment card section
    And I enter my mastercard number in the card number field
    And I enter the mastercard expiry date in the expiry date field
    And I enter my mastercard name in the name field
    When I click the 'next' button
    Then I see my mastercard displayed under the payment cards section
    And I can delete my mastercard