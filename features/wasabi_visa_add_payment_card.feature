# Created by demetriswilliams at 19/04/2021
Feature: As a User
  I want to add my Visa Debt Card
  So that I can start earning points when I purchase a chicken Katsu Curry

  Background: User is logged into their Bink Web Wasabi Account

    Given I am on the Bink Web Wasabi Platform
    And I enter my <email_address> in the magic link email address field
    And I click the 'continue' button
    And I see the Magic Link email in my inbox
    When I click the Magic Link
    Then I am logged into my account

    @paypay
  Scenario: As an Existing User, I want to add a Visa Payment card to my account

    Given I click the '+' icon under the payment card section
    And I enter my visa card number in the card number field
    And I enter the expiry date in the expiry date field
    And I enter my name in the name field
    And I click the 'next' button
    When I click the 'I accept' button on the terms & conditions modal
    Then I see my visa card displayed under the payment cards section
    And I can see my name
    And I can see the last four digits of my card number
    And I can see the expiry date


