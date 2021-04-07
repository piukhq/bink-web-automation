@wasabi
Feature: Ensure a customer can use Bink Web to add an existing loyalty card to their wasabi account
  As a User
  I want to register / login to the Bink Web Platform
  So I can add my existing Wasabi Loyalty card to my account

  @happy_path
  Scenario Outline: Register as new Bink Web Wasabi customer & add my existing Wasabi Loyalty card to my Bink Web Account

    Given I am on the Bink Web Wasabi Platform
    And I enter my <email_address> in the email address text box
    When I click the 'continue' button


    Examples:

      | email_address          |
      | dwilliams@testbink.com |
      |                        |