import time

from allure_behave.hooks import allure_report
from behave import *

from test_data.test_data import TestData
from test_data.test_data_staging import VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE, VISA_CARD_NAME

allure_report('reports')
use_step_matcher("re")


@given("I click the '\+' icon under the payment card section")
def click_add_payment_card_icon(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath("//div[@id='root']/div/div/div[4]/div/div/div").click()
    add_card_iframe = context.browser.find_by_tag_name("iframe")
    context.browser.switch_to_add_card_iframe(add_card_iframe)


@step("I enter my visa card number in the card number field")
def enter_card_number(context):
    """
    :param payment_provider:
    :type context: behave.runner.Context
    """

    context.browser.find_by_id("card_number").send_keys(VISA_CARD_NUMBER_SPREEDLY)


@step("I enter the expiry date in the expiry date field")
def enter_expiry_date(context):
    """
    :type context: behave.runner.Context
    # """
    context.browser.switch_back()
    context.browser.find_by_xpath(
        "//div[@id='root']/div/div/div[6]/div[2]/div/form/div/div[3]/input").send_keys(
        VISA_EXPIRY_DATE)


@step("I enter my name in the name field")
def enter_payment_card_name(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath(
        "//div[@id='root']/div/div/div[6]/div[2]/div/form/div/div[4]/input").send_keys(
        VISA_CARD_NAME)


@when("I click the 'next' button")
def click_submit_payment_card_button(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_css(
        "button.Button_root__3ros1.PaymentCardAddForm_root__button__2YbO3.Button_root--primary__2A9zd").click()


@step("I click the 'I accept' button on the terms & conditions modal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_xpath("//div[@id='root']/div/div/div[6]/div/div/div[2]/button").click()


@then("I see my card displayed under the payment cards section")
def assert_new_card_is_added(context):
    """
    :param payment_provider:
    :type context: behave.runner.Context
    """

    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L")
    assert card_name is not None


@step("I can see my name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@step("I can see the last four digits of my card number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I can see the expiry date")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("I have logged into my account")
def user_logged_into_account(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("web.staging.gb.bink.com/staging/wasabi/login")
    context.browser.maximize()
    email_address = TestData.MAILTRAP_EMAIL
    context.browser.find_by_id("bink-form-field-undefined").send_keys(email_address)
    context.browser.find_by_xpath("//button[contains(text(),'Continue')]").click()

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
    context.browser.find_by_xpath("//*[contains(text(), 'Magic Link Request')]").click()

    # context.browser.get_iframe_by_index('3')
    context.browser.get_magic_link_iframe('i6jjn6')
    magic_link_raw = context.browser.get_magic_link('h2')
    magic_link_url_link = magic_link_raw.split()[2]
    i = 59
    updated_ml = magic_link_url_link[:i] + magic_link_url_link[i + 1:]

    context.browser.visit_manually(updated_ml)

    try:
        wasabi_hero_image = context.browser.find_by_css("img.Hero_root__image__2dry5")
        assert wasabi_hero_image is not None
    except:
        print('Hero image not rendered')


@step("I can delete my card")
def delete_payment_card(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_class(
        "PaymentCard_root__delete__5UBn-").click()
    context.browser.find_by_css("input.PaymentCardDeleteForm_root__input__2E-tl").send_keys('1111')
    context.browser.find_by_xpath("//div[@id='root']/div/div/div[6]/div[2]/div/button").click()
