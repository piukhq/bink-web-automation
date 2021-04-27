from behave import *

use_step_matcher("re")


@step("I enter my (?P<email_address>.+) in the magic link email address field")
def enter_email_address_new_user_enrol(context, email_address):
    """
    :type context: behave.runner.Context
    :type email_address: str
    """
    context.browser.find_by_id("bink-form-field-undefined").send_keys(email_address)
