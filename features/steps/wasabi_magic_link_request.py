import time

from behave import *

from test_data.test_data import TestData

use_step_matcher("re")


@then("I see a Magic Link email in my inbox")
def step_impl(context):
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
    context.browser.find_by_xpath("//*[contains(text(), 'Magic Link Request')]").click()


@when("I enter (?P<email>.+) in the magic link email address field")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    :type email: str
    """
    context.browser.find_by_id("bink-form-field-undefined").send_keys(email)


@then("the continue button remains disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.find_by_tag_name("button").is_enabled() is False


@step("I cannot click the 'continue' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_tag_name("button").click()


@step("the 'continue' button is enabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.find_by_tag_name("button").is_enabled() is True


@when("I remove my email address from the email address field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_id("bink-form-field-undefined").clear()


@then("the continue button is now disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Coded to pass - tbf
    assert context.browser.find_by_tag_name("button").is_enabled() is True

