from allure_behave.hooks import allure_report
from behave import *

from test_data.test_data_staging import VISA_CARD_NUMBER, VISA_EXPIRY_DATE
from utils import page_selectors as el

allure_report('reports')
use_step_matcher("re")
use_step_matcher("re")


@given("I click the '\+' icon under the payment card section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath("//div[@id='root']/div/div/div[4]/div[2]/div/div").click()
    add_card_iframe = context.browser.find_by_tag_name("iframe")
    context.browser.switch_to_add_card_iframe(add_card_iframe)


@step("I enter my visa card number in the card number field")
def enter_card_number(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_tag_name("//div[@id='bink-spreedly-number']").send_keys(VISA_CARD_NUMBER)


@step("I enter the expiry date in the expiry date field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath(
        "//body/div[@id='root']/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/input[1]").send_keys(
        VISA_EXPIRY_DATE)


@step("I enter my name in the name field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath(
        "//body/div[@id='root']/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/input[1]").send_keys(
        VISA_CARD_NAME="Pret")


@step("I click the 'next' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.browser.find_by_xpath("div[class='PaymentCardAdd_root__inner__1empu']").click


@when("I click the 'I accept' button on the terms & conditions modal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.perform_click(el.ADD_CARD_NEXT_BUTTON)


@then("I see my visa card displayed under the payment cards section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I can see my name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


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
