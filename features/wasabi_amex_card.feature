# Created by demetriswilliams at 22/04/2021
@amex
Feature: As a User
  I want to add my Amex Credit Card
  So that I can start earning points when I purchase a chicken Katsu Curry


  @add_amex_card
  Scenario: As an Existing User, I want to add a Amex Payment card to my account

    Given I have logged into my account
    And  I click the '+' icon under the payment card section
    And I enter my amex card number in the card number field
    And I enter the amex expiry date in the expiry date field
    And I enter my amex card name in the name field
    When I click the 'next' button
    Then I see my amex card displayed under the payment cards section
    And I can delete my card
#    And I can see my name
#    And I can see the last four digits of my card number
#    And I can see the expiry date


