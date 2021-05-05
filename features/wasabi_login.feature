# Created by demetriswilliams at 10/04/2021
@login_web
Feature: Magic Link Existing Users
  As an Existing Bink Web Wasabi User
  I want to request a magic link
  So that I can login to my account

  @login
  Scenario Outline: As an Existing Bink Web customer with no active payment cards, I want to login to my account using the Magic Link
    Given I am on the Bink Web Wasabi Platform
    And I enter the <email_address> in the magic link email address field
    And I click the 'continue' button
    And I see the Magic Link email in my inbox
    When I click the Magic Link
    Then I am logged into my account
    And I can see the Wasabi Hero Image
    And I can see my Loyalty Card Number
    And I can see my Stamp History
    And I can see my Reward History

    Examples:
      | email_address                       |
      | 33cc7471de-f34439@inbox.mailtrap.io |

#
#  @login @existinguser @happypath
#  Scenario Outline: As an Existing Bink Web customer with an Active Payment Card, I want to login to my account using the Magic Link
#
#    Given I am on the Bink Web Wasabi Platform
#    And I enter the <email_address> in the magic link email address field
#    And I click the 'continue' button
#    And I see the Magic Link email in my inbox
#    When I click the Magic Link
#    Then I am logged into my account
#    And I can see the Wasabi Hero Image
#    And I can see my Loyalty Card Number
#    And I can see my Stamp History
#    And I can see my Reward History
#    And I can see my Active Payment Card in the payment card section
#
#    Examples:
#      | email_address                       |
#      | 33cc7471de-f34439@inbox.mailtrap.io |
#
#
#  @login @linkexpired
#  Scenario Outline: As an Existing Bink Web customer with an Active Payment Card, I want to login to my account using an
#  expired Magic Link
#
#    Given I am on the Bink Web Wasabi Platform
#    And I enter the <email_address> in the magic link email address field
#    And I click the 'continue' button
#    And I see the Magic Link email in my inbox
#    When I click the Magic Link
#    Then I see the 'Linked Expired' page
#
#    Examples:
#      | email_address                       |
#      | be260314e3-dbdf20@inbox.mailtrap.io |

#
#  @login @recyclerview
#  Scenario Outline: As an Existing Bink Web customer with one Unlinked Payment Card, I want to login to my account with an already used Magic Link
#
#    Given I have already accessed my account using a Magic Link
#    And I have a logged out of my account
#    And I see the Magic Link that I have already used in my inbox
#    When I click the Magic Link that I have already used
#    Then I see the on-boarding page
#    And I can enter my email in the email address field
#    Examples:
#      | email_address                       |
#      | be260314e3-dbdf20@inbox.mailtrap.io |


#  Scenario Outline: As an Existing Bink Web customer with one Active Payment Card & one Unlinked Payment Card,
#  I want to login to my account using the Magic Link
#
#    Given I am on the Bink Web Wasabi Platform
#    And I enter the <email_address> in the magic link email address field
#    And I click the 'continue' button
#    And I see the Magic Link email in my inbox
#    When I click the Magic Link
#    Then I am logged into my account
#    And I can see the Wasabi Hero Image
#    And I can see my Loyalty Card Number
#    And I can see my Stamp History
#    And I can see my Reward History
#    And I can see my Active Payment Card in the payment card section
#    And I can see my Unlinked Payment Card in the unlinked payment card section
#
#    Examples:
#      | email_address                       |
#      | 33cc7471de-f34439@inbox.mailtrap.io |