# Created by demetriswilliams at 19/04/2021
@visa
Feature: As a User
  I want to add my Visa Debt Card
  So that I can start earning points when I purchase Wasabi Products


  @add_visa_card
  Scenario Outline: As an Existing User, I want to add a Visa Payment card to my account

    Given I have logged into my account with my email: <email>
    And there aren't any existing cards ending in <last_four_digits>
    And  I click the '+' icon under the payment card section
    And I enter the <visa_card_number> in the card number field
    And I enter the expiry date in the expiry date field
    And I enter my name in the name field
    When I click the 'next' button
    Then I see my card displayed under the payment cards section
    And I can delete my original payment card ending in <last_four_digits>


    Examples:

      | email                               | visa_card_number | last_four_digits |
      | 2705a98811-fc9a6e@inbox.mailtrap.io | 4111111111111111 | 1111             |
      |                                     |                  | 0005             |
      |                                     |                  | 4444             |


  @duplicate_visa_card
  Scenario Outline: As an Existing User, I want to add a duplicate Visa Payment card to my account

    Given I have logged into my account with my email: <email>
    And I already have a valid visa payment card
    And  I click the '+' icon under the payment card section
    And I enter the <visa_card_number> in the card number field
    And I enter the amex expiry date in the expiry date field
    And I enter my amex card name in the name field
    When I click the 'next' button
    Then I see my original amex card displayed under the payment cards section
    And I don't see an additional duplicate card
    And I can delete my original payment card ending in <last_four_digits>

    Examples:
      | visa_card_number | last_four_digits |
      | 4111111111111111 | 1111             |