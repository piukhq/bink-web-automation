import time

from behave import *

from test_data.test_data import TestData

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
    time.sleep(11)
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
    title = context.browser.assert_page_title(TestData.PAGE_TITLE)
    # assert title == TestData.PAGE_TITLE


@step("I can see the Wasabi Hero Image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I can see the Wasabi Hero Image')


@step("I can see my Loyalty Card Number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I can see my Loyalty Card Number')


@step("I can see my Stamp History")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I can see my Stamp History')


@step("I can see my Reward History")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I can see my Reward History')


@then("I am logged into my account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I am logged into my account')
