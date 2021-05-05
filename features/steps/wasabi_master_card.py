from behave import *

from test_data.test_data_staging import MASTERCARD_CARD_NUMBER_SPREEDLY, MASTERCARD_EXPIRY_DATE, MASTERCARD_CARD_NAME

use_step_matcher("re")


@step("I enter my mastercard number in the card number field")
def enter_master_card_number(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_id("card_number").send_keys(MASTERCARD_CARD_NUMBER_SPREEDLY)


@step("I enter the mastercard expiry date in the expiry date field")
def enter_master_card_name(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.switch_back()
    context.browser.find_by_xpath(
        "//div[@id='root']/div/div/div[6]/div[2]/div/form/div/div[3]/input").send_keys(
        MASTERCARD_EXPIRY_DATE)


@step("I enter my mastercard name in the name field")
def enter_master_card_name(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_css(
        "input[placeholder='Name on card']").send_keys(
        MASTERCARD_CARD_NAME)


@then("I see my mastercard displayed under the payment cards section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L")
    assert card_name is not None


@step("I can delete my mastercard")
def delete_master_card(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_class("PaymentCard_root__delete__5UBn-").click()
    context.browser.find_by_css("input.PaymentCardDeleteForm_root__input__2E-tl").send_keys('4444')
    context.browser.find_by_xpath("//div[@id='root']/div/div/div[6]/div[2]/div/button").click()
