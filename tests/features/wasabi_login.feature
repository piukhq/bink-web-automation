@wasabi
Feature: Ensure existing Bink Web Wasabi customers can login into their Account
  As a User
  I want to Login to my Bink Web Wasabi Account
  So that I can view my voucher history, reward history & payment cards

  @login
  Scenario Outline: As an Existing Bink Web customer with a valid loyalty card, I want to login to my account

    Given I am on the Bink Web Wasabi Debug Platform
    And I enter my <email_address> in the email address input field
    And I enter my <password> in the password input field
    When I click the 'login' button
    Then I am logged into my account
    And I can see the Wasabi Hero Image
    And I can see my Loyalty Card Number
    And I can see my Stamp History
    And I can see my Reward History

    Examples:
      | email_address            | password   |
      | dkw_binkweb@testbink.com | Password01 |

#  @happy_path @wasabi
#  Scenario Outline:  As an Existing Bink Web customer with a valid loyalty card & valid payment card, I want to login
#  to my account
#
#    Given I am a Bink Web Wasabi Customer
#    And I am on the Bink Web Wasabi Login Page
#    When I enter my "<email_address>" and "<password>" in the relevant fields
#    And I click the Login button
#    Then I am logged into my account
#    And I can see the Wasabi Hero Image
#    And I can see my Loyalty Card Number "<loyalty_card_number>"
#    And I can see my Voucher History
#    And I can see my Reward History
#    And I can see my Payment Card
#
#    Examples:
#      | email_address             | password   | loyalty_card_number |
#      | bino_binkweb@testbink.com | Password01 | 4783492094          |
#      |                           |            |                     |
#
#
#  @happy_path @wasabi
#  Scenario: As an Existing Bink Web customer with a valid loyalty card & 2 valid payment cards, I want to login
#  to my account
#
#    Given I am a Bink Web Wasabi Customer
#    And I am on the Bink Web Wasabi Login Page
#    When I enter my "<email_address>" and "<password>" in the relevant fields
#    And I click the Login button
#    Then I am logged into my account
#    And I can see the Wasabi Hero Image
#    And I can see my Loyalty Card Number "<loyalty_card_number>"
#    And I can see my Voucher History
#    And I can see my Reward History
#    And I can see my first Payment Card
#    And I can see my second Payment Card
#
#
#  @wasabi
#  Scenario: As an Existing Bink Web customer, I want to login to my account with an incorrect email & correct password
#
#    Given I am a Bink Web Wasabi Customer
#    And I am on the Bink Web Wasabi Login Page
#    When I enter an incorrect "<email_address>" and correct "<password>" in the relevant fields
#    And I click the Login button
#    Then I see a 'incorrect credential, please try again' error message
#    And I am not logged in
#
#  @wasabi
#  Scenario: As an Existing Bink Web customer, I want to login to my account with the correct email & incorrect password
#
#    Given I am a Bink Web Wasabi Customer
#    And I am on the Bink Web Wasabi Login Page
#    When I enter the correct "<email_address>" and incorrect "<password>" in the relevant fields
#    And I click the Login button
#    Then I see a 'incorrect credential, please try again' error message
#    And I am not logged in
#
#
#
#
#
#
