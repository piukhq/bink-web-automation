from behave import *

from test_data.test_data_staging import AMEX_CARD_NAME, AMEX_CARD_NUMBER_SPREEDLY, AMEX_EXPIRY_DATE

use_step_matcher("re")


@step("I enter my amex card number in the card number field")
def enter_amex_card_number(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_id("card_number").send_keys(AMEX_CARD_NUMBER_SPREEDLY)


@then("I see my amex card displayed under the payment cards section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L")
    assert card_name is not None


@step("I enter my amex card name in the name field")
def enter_amex_card_name(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath(
        "//div[@id='root']/div/div/div[6]/div[2]/div/form/div/div[4]/input").send_keys(
        AMEX_CARD_NAME)


@step("I enter the amex expiry date in the expiry date field")
def enter_amex_card_expiry_date(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.switch_back()
    context.browser.find_by_xpath(
        "//div[@id='root']/div/div/div[6]/div[2]/div/form/div/div[3]/input").send_keys(
        AMEX_EXPIRY_DATE)
