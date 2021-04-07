""" Step Definitions in relation to Login in via Legacy route (NOT Magic Link) """

# WIP - stopped at confirm_user_logged_in


from pytest_bdd import when, scenarios, then, given

from test_data.test_data import TestData

scenarios('../features/wasabi_login.feature')


@given("I am on the Bink Web Wasabi Debug Platform")
def bink_wasabi_debug_web_page(web_browser):
    web_browser.get(TestData.STAGING_URL_DEBUG)


@given("I enter my <email_address> in the email address input field")
def enter_email_address_login_field(web_browser, email_address):
    email_address = TestData.USERNAME
    web_browser.find_element_by_xpath("(//input[@value=''])[2]").send_keys(email_address)



@given("I enter my <password> in the password input field")
def step_impl(web_browser, password):
    password = TestData.PASSWORD
    web_browser.find_element_by_xpath("(//input[@value=''])[2]").send_keys(password)



@when("I click the 'login' button")
def click_login_button_debug_page(web_browser):
    web_browser.find_element_by_xpath("//button[contains(text(),'Login')]").click()


@then("I am logged into my account")
def confirm_user_logged_in(web_browser):
    element = web_browser.find_element_by_xpath("//div[@id='root']/div/div/button").text()
    assert element == 'Logout'


@given("I can see the Wasabi Hero Image")
def step_impl(web_browser):
    web_browser.find_element_by_class_name("Hero_root__image-section__1kcBL").is_displayed()


@given("I can see my Loyalty Card Number")
def confirm_loyalty_card_number_present(web_browser):
    loyalty_card_number = web_browser.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div[2]").text()
    assert loyalty_card_number is not None


@given("I can see my Stamp History")
def stamp_history_present(web_browser):
    web_browser.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div[2]").is_displayed()


@given("I can see my Reward History")
def reward_history(web_browser):
    web_browser.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div[3]").is_displayed()
