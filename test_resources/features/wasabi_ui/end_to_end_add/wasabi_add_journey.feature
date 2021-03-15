@wasabi
Feature: Ensure a customer can use Bink Web to add an existing loyalty card to their wasabi account
  As a User
  I want to register / login to the Bink Web Platform
  So I can add my existing Wasabi Loyalty card to my account

  @happy_path
  Scenario: Register as new Bink Web Wasabi customer & add my existing Wasabi Loyalty card to my Bink Web Account

  Given I am on the Bink Web Wasabi Platform
    And I have registered to open an Account
    # Enter steps here