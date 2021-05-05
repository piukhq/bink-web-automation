# Created by demetriswilliams at 28/04/2021
@voucherz
Feature: As a User
  I want to login to my Wasabi Web Account
  So that I can view my vouchers

  @redeemable_vouchers
  Scenario Outline: As an Existing Wasabi Web customer, I want to view my redeemable vouchers
    Given I have obtained a magic link with my email address: <email>
    And I have <number> redeemable vouchers linked to my loyalty card
    When I click the Magic Link
    Then I am logged into my account
    And I can see <number_returned> redeemable vouchers
    And I can see '<number> stamps to go' status


    Examples:
      | email                               | number | number_returned | number |
      | cfab97b370-e08df7@inbox.mailtrap.io | 5      | 5               | 2      |


  @expired_vouchers
  Scenario Outline: As an Existing Wasabi Web customer, I want to view my redeemable vouchers
    Given I have obtained a magic link with my email address: <email>
    And I have <number> redeemable vouchers linked to my loyalty card
    When I click the Magic Link
    Then I am logged into my account
    And I can see <number_returned> redeemable vouchers
    And I can see '<number> stamps to go' status


    Examples:
      | email | number | number_returned | number |
      |       | 5      | 5               | 2      |
