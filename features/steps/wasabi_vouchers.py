import time

from behave import *

from test_data.test_data import TestData

use_step_matcher("re")


@given("I have obtained a magic link with my email address: (?P<email>.+)")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """

    context.browser.visit("web.staging.gb.bink.com/staging/wasabi/login")
    context.browser.find_by_id("bink-form-field-undefined").send_keys(email)
    context.browser.find_by_xpath("//button[contains(text(),'Continue')]").click()

    context.browser.visit("mailtrap.io")
    context.browser.find_by_link_text("Log In").click()
    time.sleep(3)
    context.browser.find_by_class('cookies-banner__button').click()
    context.browser.find_by_id('user_email').send_keys(TestData.MAGIC_LINK_EMAIL)
    context.browser.find_by_id('user_password').send_keys(TestData.MAILTRAP_PASSWORD)
    context.browser.find_by_name('commit').click()
    context.browser.find_by_xpath("//body/div[@id='falconApp']/div[1]/aside[1]/nav[1]/ul[1]/li[1]/a[1]").click()
    context.browser.find_by_xpath(
        "//div[@id='falconApp']/div/div[2]/div/div[2]/div/div/div[3]/div[6]/div/span/a/span").click()

    context.browser.find_by_xpath("//*[contains(text(), 'a few seconds ago')]").click()


@step("I have (?P<number>.+) redeemable vouchers linked to my loyalty card")
def step_impl(context, number):
    """
    :type context: behave.runner.Context
    """
    assert number == '5'


@step("I can see (?P<int>.+) redeemable vouchers")
def step_impl(context, int):
    """
    :type context: behave.runner.Context
    """
    collect_stamps = context.browser.find_by_class("Voucher_root__progress-value__A6MBD").text[0]
    assert collect_stamps == str(int)



@step("I can see the (?P<status>.+) status above my vouchers")
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_by_xpath("//div[@id='bink-app-root']/div/div/div[3]/div/div/div[4]/span[4]")


@step("I can see '(?P<number>.+) stamps to go' status")
def step_impl(context, number):
    """
    :type context: behave.runner.Context
    :type number: str
    """
    stamps_to_go = context.browser.find_by_class("Voucher_root__headline__3e7PO").text[0]
    str(number) == stamps_to_go
