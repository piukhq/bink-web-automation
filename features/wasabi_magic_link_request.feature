# Created by demetriswilliams at 28/04/2021

@magic_link
Feature: As a User
  I want to enter my email on the Magic Link Request Page
  So I can obtain a magic link

  @valid_email
  Scenario Outline: As an existing Wasabi Web User, I want to obtain a Magic Link with a valid email address

    Given I am on the Bink Web Wasabi Platform
    And I enter the <email_address> in the magic link email address field
    When I click the 'continue' button
    Then I see the Magic Link email in my inbox

    Examples:
      | email_address                       |
      | 33cc7471de-f34439@inbox.mailtrap.io |

  @invalid_email_address_format @negative
  Scenario Outline: As an existing Wasabi Web User, I want to obtain a Magic Link with an invalid email address format

    Given I am on the Bink Web Wasabi Platform
    When I enter <email> in the magic link email address field
    Then the continue button remains disabled

    Examples:
      | email                                                 |
      | 33cc7471de-hjesbudvvcsdinsfcoa  fi @inbox.mailtrap.io |
      | 0-0934482043                                          |
      | gmail.com@esidnsE                                     |


  @empty_email_field @negative
  Scenario Outline: As an existing Product Owner, I want to request a Magic Link without an email address

    Given I am on the Bink Web Wasabi Platform
    And I enter my <email_address> in the magic link email address field
    And the 'continue' button is enabled
    When I remove my email address from the email address field
    Then the continue button is now disabled

    Examples:
      | email_address                 |
      | iamvalidlol@inbox.mailtrap.io |




