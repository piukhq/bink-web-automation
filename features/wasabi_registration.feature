# Created by demetriswilliams at 12/04/2021
Feature: Magic Link Registration
  As a new user
  I want to obtain a magic link
  So that I can register for a Bink Web Wasabi account

  Background: New User is on the Magic Link request page
    Given I am on the Bink Web Wasabi Platform


  Scenario Outline: As a new User, I want to enrol for a Bink Web Wasabi Account

    Given I enter my "email_address" in the magic link email address field
    And I click the 'continue' button
    And I see the Magic Link email in my inbox
    When I click the Magic Link
    Then I see the on-boarding page


    Examples:
      | email_address                       |
      | 0b2ad83295-e07b63@inbox.mailtrap.io |


#
#        Given I am on the on-boarding page
#    And I see the 'get a new card' button
#    And I see the 'I already got a card' button
#    When I click the 'get new card' button



