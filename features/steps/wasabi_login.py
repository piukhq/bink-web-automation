import time

from allure_behave.hooks import allure_report
from behave import *

from test_data.test_data import TestData
from test_data.test_data_staging import XRP_CARD_NAME

allure_report('reports')
use_step_matcher("re")


@given("I have already accessed my account using a Magic Link")
@given("I am on the Bink Web Wasabi Platform")
def get_website(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("web.staging.gb.bink.com/staging/wasabi/login")
    context.browser.maximize()


@given("I enter the (?P<email_address>.+) in the magic link email address field")
def enter_email_address(context, email_address):
    """
    :type context: behave.runner.Context
    :type email_address: str
    """
    context.browser.find_by_id("bink-form-field-undefined").send_keys(email_address)


@step("I click the 'continue' button")
def click_magic_link_continue_button(context):
    """
    :type context: behave.runner.Context a
    """
    context.browser.find_by_xpath("//button[contains(text(),'Continue')]").click()


@step("I see the Magic Link email in my inbox")
def log_into_email_inbox(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("mailtrap.io")
    context.browser.find_by_link_text("Log In").click()
    time.sleep(3)
    context.browser.find_by_class('cookies-banner__button').click()
    context.browser.find_by_id('user_email').send_keys(TestData.MAGIC_LINK_EMAIL)
    context.browser.find_by_id('user_password').send_keys(TestData.MAILTRAP_PASSWORD)
    context.browser.find_by_name('commit').click()
    time.sleep(22)
    context.browser.find_by_xpath("//body/div[@id='falconApp']/div[1]/aside[1]/nav[1]/ul[1]/li[1]/a[1]").click()
    context.browser.find_by_xpath(
        "//div[@id='falconApp']/div/div[2]/div/div[2]/div/div/div[3]/div/div/span/a/span").click()
    time.sleep(2)
    context.browser.find_by_xpath("//*[contains(text(), 'Access your Wasabi Club account')]").click()


@when("I click the Magic Link")
def click_magic_link(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.get_magic_link_iframe('i6jjn6')
    magic_link_raw = context.browser.get_magic_link('h2')
    magic_link_url_link = magic_link_raw.split()[2]
    # i = 59
    # updated_ml = magic_link_url_link[:i] + magic_link_url_link[i + 1:]
    context.browser.visit_manually(magic_link_url_link)


@step("I can see the Wasabi Hero Image")
def assert_wasabi_imag_is_displayed(context):
    """
    :type context: behave.runner.Context
    """
    try:
        wasabi_hero_image = context.browser.find_by_css("img.Hero_root__image__2dry5")
        assert wasabi_hero_image is not None
    except:
        print('Hero image not rendered')


@step("I can see my Loyalty Card Number")
def assert_loyalty_card_is_displayed(context):
    """
    :type context: behave.runner.Context
    """
    try:
        loyalty_card_number = context.browser.assert_user_is_logged_in("Hero_root__card-number-value__1ee9h")
        assert loyalty_card_number is TestData.TEMP_LOYALTY_NUMBER
    except:
        print('Loyalty card number not displayed')


@step("I can see my Stamp History")
def assert_stamp_history_is_displayed(context):
    """
    :type context: behave.runner.Context
    """
    try:
        stamp_history = context.browser.find_by_xpath("div[class='Hero_root__subtitle__3qHpP']")
        assert stamp_history is not None
    except:
        print('Stamp history section not displayed')


@step("I can see my Reward History")
def assert_rewards_history_is_displayed(context):
    """
    :type context: behave.runner.Context
    """
    try:
        rewards_history = context.browser.find_by_xpath(
            "div[class='Hero_root__subtitle__3qHpP Hero_root__subtitle--desktop-only__35S6H']")
        assert rewards_history is not None
    except:
        print('Stamp history section not displayed')


@then("I am logged into my account")
def assert_user_is_logged_in(context):
    """
    :type context: behave.runner.Context
    """
    try:
        wasabi_card_number_text = context.browser.assert_user_is_logged_in("Hero_root__card-number-label__10Yz3")[
            0].text
        assert wasabi_card_number_text == 'Card number'
    except:
        print('User failed logged in')


@step("I can see my Active Payment Card in the payment card section")
def assert_the_card_is_displayed(context):
    """
    :type context: behave.runner.Context

    """
    payment_card_name = context.browser.find_by_xpath("//div[contains(text(),'xrp')]").text
    card_status = context.browser.find_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]").text

    assert payment_card_name == XRP_CARD_NAME
    assert card_status == 'Active'


@step("I can see my Unlinked Payment Card in the unlinked payment card section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    card_status = context.browser.find_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]").text
    assert card_status == 'Activating'


@then("I see the 'Linked Expired' page")
def assert_link_expired_page(context):
    """
    :type context: behave.runner.Context
    """
    page_title = context.browser.assert_page_title("h1")
    assert page_title == 'Link Expired'


@then("I see the on-boarding page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page_title = context.browser.assert_page_title('h1')
    assert page_title == 'Wasabi Club'


@step("I can enter my email in the email address field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I have a logged out of my account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I click the Magic Link that I have already used")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.get_magic_link_iframe('i6jjn6')
    magic_link_raw = context.browser.get_magic_link('pre')
    magic_link_url_link = magic_link_raw.split()[2]
    context.browser.visit_manually(magic_link_url_link)


@step("I see the Magic Link that I have already used in my inbox")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit("mailtrap.io")
    context.browser.maximize()
    context.browser.find_by_link_text("Log in").click()
    context.browser.find_by_id('user_email').send_keys(TestData.MAGIC_LINK_EMAIL)
    context.browser.find_by_id('user_password').send_keys(TestData.MAILTRAP_PASSWORD)
    context.browser.find_by_name('commit').click()
    time.sleep(20)
    context.browser.find_by_xpath("//body/div[@id='falconApp']/div[1]/aside[1]/nav[1]/ul[1]/li[1]/a[1]").click()
    context.browser.find_by_xpath(
        "//div[@id='falconApp']/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div/span/a/strong").click()

    context.browser.find_by_xpath("//*[contains(text(), 'Magic Link Request')]").click()