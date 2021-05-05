# Created by demetriswilliams at 22/04/2021
@amex
Feature: As a User
  I want to add my Amex Credit Card
  So that I can start earning points when I purchase Wasabi Products


  @add_valid_amex_card
  Scenario Outline: As an Existing User, I want to add a Amex Payment card to my account

    Given I have logged into my account with my email: <email>
    And there aren't any existing cards ending in <last_four_digits>
    And  I click the '+' icon under the payment card section
    And I enter the <amex_card_number> in the card number field
    And I enter the expiry date in the expiry date field
    And I enter my amex card name in the name field
    When I click the 'next' button
    Then I see my amex card displayed under the payment cards section
    And I can delete my card

    Examples:
      | email                               | amex_card_number | last_four_digits |
      | 33cc7471de-f34439@inbox.mailtrap.io | 378282246310005  | 1111             |
      |                                     |                  | 0005             |
      |                                     |                  | 4444             |

  @duplicate_amex_card
  Scenario Outline: As an Existing User, I want to add a duplicate Amex Payment card to my account

    Given I have logged into my account with my email: <email>
    And I already have a valid amex payment card
    And  I click the '+' icon under the payment card section
    And I enter the <amex_card_number> in the card number field
    And I enter the amex expiry date in the expiry date field
    And I enter my amex card name in the name field
    When I click the 'next' button
    Then I see my original amex card displayed under the payment cards section
    And I don't see an additional duplicate card
    And I can delete my original payment card ending in <last_four_digits>

    Examples:
      | email                               | amex_card_number | last_four_digits |
      | 33cc7471de-f34439@inbox.mailtrap.io | 378282246310005  | 0005             |



#  @add_invalid_card_number_amex
#  Scenario Outline: As an Existing User, I want to add an Invalid Amex Payment card to my account
#
#    Given I have logged into my account
#    And  I click the '+' icon under the payment card section
#    And I enter the <invalid_amex_card_number> in the card number field
#    And I enter the amex expiry date in the expiry date field
#    And I enter my amex card name in the name field
#    When I click the 'next' button
#    Then I see my amex card displayed under the unlinked payment cards section
#    And I can delete my card
#
#    Examples:
#      | invalid_amex_card_number |
#      | 371449635398431          |





