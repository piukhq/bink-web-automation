import logging
import time

logger = logging.getLogger(__name__)

from behave import *

from test_data.test_data import TestData
from test_data.test_data_staging import VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE, VISA_CARD_NAME
from test_data.test_data import TestData as TD

use_step_matcher("re")


@given("I click the '\+' icon under the payment card section")
def click_add_payment_card_icon(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_css("div.PaymentCardAdd_root__inner__1empu").click()
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
    context.browser.find_by_css(
        "input[placeholder='MM/YY']").send_keys(
        VISA_EXPIRY_DATE)


@step("I enter my name in the name field")
def enter_payment_card_name(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_css(
        "input[placeholder='Name on card']").send_keys(
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


@given("I have logged into my account with my email: (?P<enter_email>.+)")
def user_logged_into_account(context, enter_email):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("web.staging.gb.bink.com/staging/wasabi/login")
    context.browser.find_by_id("bink-form-field-undefined").send_keys(enter_email)
    context.browser.find_by_xpath("//button[contains(text(),'Continue')]").click()

    context.browser.visit("mailtrap.io")
    context.browser.find_by_link_text("Log In").click()
    time.sleep(3)
    context.browser.find_by_class('cookies-banner__button').click()
    context.browser.find_by_id('user_email').send_keys(TestData.MAGIC_LINK_EMAIL)
    context.browser.find_by_id('user_password').send_keys(TestData.MAILTRAP_PASSWORD)
    context.browser.find_by_name('commit').click()
    context.browser.find_by_xpath("//body/div[@id='falconApp']/div[1]/aside[1]/nav[1]/ul[1]/li[1]/a[1]").click()

    """ Check which Inbox to select """

    user_emails = [TD.visa_email_mail_trap, TD.master_card_email_mail_trap, TD.amex_email_mail_trap]

    if enter_email == user_emails[0]:
        context.browser.find_by_xpath('//span[contains(text(),"VISA")]').click()
    elif enter_email == user_emails[1]:
        context.browser.find_by_xpath(
            '//span[contains(text(),"MASTERCARD")]').click()
    else:
        context.browser.find_by_xpath(
            '//span[contains(text(),"AMEX")]').click()

    """ Select Email """
    context.browser.find_by_xpath("//*[contains(text(), 'a few seconds ago')]").click()

    # context.browser.get_iframe_by_index('3')
    context.browser.get_magic_link_iframe('i6jjn6')
    magic_link_raw = context.browser.get_magic_link('h2')
    magic_link_url_link = magic_link_raw.split()[2]
    # i = 59
    # updated_ml = magic_link_url_link[:i] + magic_link_url_link[i + 1:]

    context.browser.visit_manually(magic_link_url_link)

    try:
        wasabi_hero_image = context.browser.find_by_css("img.Hero_root__image__2dry5")
        assert wasabi_hero_image is not None
    except:
        logger.info('Hero image not rendered')

    """ check is there is an existing card """


@step("I can delete my card")
def delete_payment_card(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_class(
        "PaymentCard_root__delete__5UBn-").click()
    context.browser.find_by_css("input.PaymentCardDeleteForm_root__input__2E-tl").send_keys('0005')
    context.browser.find_by_xpath("//div[@id='root']/div/div/div[6]/div[2]/div/button").click()


@step("there aren't any existing cards ending in (?P<last_four_digits>.+)")
def step_impl(context, last_four_digits):
    """
    :type context: behave.runner.Context
    :type last_four_digits: str
    """

    try:
        context.browser.find_by_class(
            "PaymentCard_root__delete__5UBn-")
        context.browser.find_by_class(
            "PaymentCard_root__delete__5UBn-").click()
        context.browser.find_by_css("input.PaymentCardDeleteForm_root__input__2E-tl").send_keys(last_four_digits)
        context.browser.find_by_css(
            "button.Button_root__3ros1.PaymentCardDeleteForm_root__button__3CtMq.Button_root--tertiary__3wW3X").click()

    except Exception as e:
        logger.info(e)
