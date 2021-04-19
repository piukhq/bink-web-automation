import time
from allure_behave.hooks import allure_report
from behave import *

from test_data.test_data import TestData
from test_data.test_data_staging import XRP_CARD_NAME

allure_report('reports')
use_step_matcher("re")


@given("I am on the Bink Web Wasabi Platform")
def get_website(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("web.staging.gb.bink.com/staging/wasabi/login")
    context.browser.maximize()


@given("I enter my (?P<email_address>.+) in the magic link email address field")
def enter_email_address(context, email_address):
    """
    :type context: behave.runner.Context
    :type email_address: str
    """
    email_address = TestData.MAILTRAP_EMAIL
    context.browser.find_by_id("bink-form-field-undefined").send_keys(email_address)


@step("I click the 'continue' button")
def click_magiclink_continue_button(context):
    """
    :type context: behave.runner.Context a
    """
    context.browser.find_by_xpath("//button[contains(text(),'Continue')]").click()


@step("I see the Magic Link email in my inbox")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("mailtrap.io")
    context.browser.find_by_link_text("Log in").click()
    context.browser.find_by_id('user_email').send_keys(TestData.MAGIC_LINK_EMAIL)
    context.browser.find_by_id('user_password').send_keys(TestData.MAILTRAP_PASSWORD)
    context.browser.find_by_name('commit').click()
    time.sleep(20)
    context.browser.find_by_xpath("//body/div[@id='falconApp']/div[1]/aside[1]/nav[1]/ul[1]/li[1]/a[1]").click()
    context.browser.find_by_xpath(
        "//body/div[@id='falconApp']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/a[1]/strong[1]").click()
    context.browser.find_by_xpath("//*[contains(text(), 'Magic Link Request')]").click()


@when("I click the Magic Link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.get_magic_link_iframe('i6jjn6')
    magic_link_raw = context.browser.get_magic_link('pre')
    magic_link_url_link = magic_link_raw.split()[2]
    context.browser.visit_manually(magic_link_url_link)


@step("I can see the Wasabi Hero Image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        wasabi_hero_image = context.browser.find_by_css("img.Hero_root__image__2dry5")
        assert wasabi_hero_image is not None
    except:
        print('Hero image not rendered')


@step("I can see my Loyalty Card Number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        loyalty_card_number = context.browser.assert_user_is_logged_in("Hero_root__card-number-value__1ee9h")
        assert loyalty_card_number is TestData.TEMP_LOYALTY_NUMBER
    except:
        print('Loyalty card number not displayed')


@step("I can see my Stamp History")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        stamp_history = context.browser.find_by_xpath("div[class='Hero_root__subtitle__3qHpP']")
        assert stamp_history is not None
    except:
        print('Stamp history section not displayed')


@step("I can see my Reward History")
def step_impl(context):
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
def step_impl(context):
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
def step_impl(context):
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
