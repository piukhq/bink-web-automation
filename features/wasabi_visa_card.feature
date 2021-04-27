# Created by demetriswilliams at 19/04/2021
@visa
Feature: As a User
  I want to add my Visa Debt Card
  So that I can start earning points when I purchase a chicken Katsu Curry


  @add_visa_card
  Scenario Outline: As an Existing User, I want to add a Visa Payment card to my account

    Given I have logged into my account
    And  I click the '+' icon under the payment card section
    And I enter my visa card number in the card number field
    And I enter the expiry date in the expiry date field
    And I enter my name in the name field
    When I click the 'next' button
    Then I see my card displayed under the payment cards section
    And I can delete my card
#    And I can see my name
#    And I can see the last four digits of my card number
#    And I can see the expiry date


    Examples:

      | payment_provider |
      | visa             |
