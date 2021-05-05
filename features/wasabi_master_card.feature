# Created by demetriswilliams at 22/04/2021
@mastercard
Feature: As a User
  I want to add my Master Card
  So that I can start earning points when I purchase Wasabi Products


  @add_mastercard
  Scenario Outline: As an Existing User, I want to add a Master Payment card to my account

    Given I have logged into my account with my email: <email>
    And there aren't any existing cards ending in <last_four_digits>
    And  I click the '+' icon under the payment card section
    And I enter the <master_card_number> in the card number field
    And I enter the expiry date in the expiry date field
    And I enter my mastercard name in the name field
    When I click the 'next' button
    Then I see my mastercard displayed under the payment cards section
    And I can delete my original payment card ending in <last_four_digits>

    Examples:

      | email                               | master_card_number | last_four_digits |
      | 80de19092e-34c8a3@inbox.mailtrap.io | 5555555555554444   | 4444             |
      |                                     |                    | 0005             |
      |                                     |                    | 1111             |


  @duplicate_master_card
  Scenario Outline: As an Existing User, I want to add a duplicate Visa Payment card to my account

    Given I have logged into my account with my email: <email>
    And I already have a valid mastercard payment card
    And  I click the '+' icon under the payment card section
    And I enter the <master_card_number> in the card number field
    And I enter the expiry date in the expiry date field
    And I enter my mastercard name in the name field
    When I click the 'next' button
    Then I see my original amex card displayed under the payment cards section
    And I don't see an additional duplicate card
    And I can delete my original payment card ending in <last_four_digits>

    Examples:
      | master_card_number | last_four_digits |
      | 5555555555554444   | 4444             |