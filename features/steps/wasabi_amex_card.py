import logging

from behave import *

logger = logging.getLogger(__name__)

from test_data.test_data_staging import AMEX_CARD_NAME, AMEX_CARD_NUMBER_SPREEDLY, AMEX_EXPIRY_DATE
from test_data.test_data import TestData as TD


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
    context.browser.find_by_css(
        "input[placeholder='Name on card']").send_keys(
        AMEX_CARD_NAME)


@step("I enter the amex expiry date in the expiry date field")
def enter_amex_card_expiry_date(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.switch_back()
    context.browser.find_by_css(
        "input[placeholder='MM/YY']").send_keys(
        AMEX_EXPIRY_DATE)


@step("I enter my <amex_card_number> in the card number field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I enter my <amex_card_number> in the card number field')


@step("I enter the (?P<card_number>.+) in the card number field")
def step_impl(context, card_number):
    """
    :type context: behave.runner.Context
    :type card_number: str
    """
    context.browser.find_by_id("card_number").send_keys(card_number)


@then("I see my amex card displayed under the unlinked payment cards section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L")
    assert card_name is not None


@step("I already have a valid (?P<card>.+) payment card")
def step_impl(context, card):
    """
    :type context: behave.runner.Context
    """
    try:
        context.browser.find_by_class(
            "PaymentCard_root__delete__5UBn-")
        context.browser.find_by_class(
            "PaymentCard_root__delete__5UBn-").click()
        context.browser.find_by_css("input.PaymentCardDeleteForm_root__input__2E-tl").send_keys('0005')
        context.browser.find_by_css(
            "button.Button_root__3ros1.PaymentCardDeleteForm_root__button__3CtMq.Button_root--tertiary__3wW3X").click()

    except:

        """ add amex card 1 """
    context.browser.find_by_css(".PaymentCardAdd_root__2hmZX").click()
    add_card_iframe = context.browser.find_by_tag_name("iframe")
    context.browser.switch_to_add_card_iframe(add_card_iframe)

    # Payment Card  Number
    context.browser.find_by_id("card_number").send_keys(AMEX_CARD_NUMBER_SPREEDLY)

    # Expiry Date
    context.browser.switch_back()
    context.browser.find_by_css(
        "input[placeholder='MM/YY']").send_keys(
        AMEX_EXPIRY_DATE)

    # Card Name
    context.browser.find_by_css(
        "input[placeholder='Name on card']").send_keys(
        AMEX_EXPIRY_DATE)

    # Submit
    context.browser.find_by_css(
        "button.Button_root__3ros1.PaymentCardAddForm_root__button__2YbO3.Button_root--primary__2A9zd").click()

    # Confirm (for now)
    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L")
    assert card_name is not None


@then("I see my original amex card displayed under the payment cards section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L")
    assert card_name is not None


@step("I don't see an additional duplicate card")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Get card name
    # Get last four digits

    card_name = context.browser.find_by_class("PaymentCard_root__name__qU08L").text
    last_four_digits = context.browser.find_by_class("PaymentCard_root__number__vgIZS").text

    possibly_correct_lol = card_name + "\n" + last_four_digits

    all_card_names_returned = context.browser.find_by_class("PaymentCards_root__2_O-S").text
    assert all_card_names_returned == possibly_correct_lol


@step("I can delete my original payment card ending in (?P<last_four_digits>.+)")
def step_impl(context, last_four_digits):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_class(
        "PaymentCard_root__delete__5UBn-").click()
    context.browser.find_by_css("input.PaymentCardDeleteForm_root__input__2E-tl").send_keys(last_four_digits)
    context.browser.find_by_css(
        "button.Button_root__3ros1.PaymentCardDeleteForm_root__button__3CtMq.Button_root--tertiary__3wW3X").click()
