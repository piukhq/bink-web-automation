from pytest_bdd import when, scenarios, then, given
from test_data.test_data import TestData

scenarios('../features/wasabi_add_journey.feature')


@given('I am on the Bink Web Wasabi Platform')
def bink_wasabi_web_page(web_browser):
    web_browser.get(TestData.STAGING_URL)


@when('I enter my <email> in the email address text box')
def step_impl():
    pass


def step_impl():
    raise NotImplementedError(u'STEP: Given I am on the Bink Web Wasabi Platform')



@given("I am on the Bink Web Wasabi Login Page")
def step_impl():
    raise NotImplementedError(u'STEP: And I am on the Bink Web Wasabi Login Page')


@when('I enter my "<email_address>" and "<password>" in the relevant fields')
def step_impl():
    raise NotImplementedError(u'STEP: When I enter my "<email_address>" and "<password>" in the relevant fields')


@given("I click the Login button")
def step_impl():
    raise NotImplementedError(u'STEP: And I click the Login button')


@given('I can see my Loyalty Card Number "<loyalty_card_number>"')
def step_impl():
    raise NotImplementedError(u'STEP: And I can see my Loyalty Card Number "<loyalty_card_number>"')


@given("I can see my Payment Card")
def step_impl():
    raise NotImplementedError(u'STEP: And I can see my Payment Card')


@given("I can see my first Payment Card")
def step_impl():
    raise NotImplementedError(u'STEP: And I can see my first Payment Card')


@given("I can see my second Payment Card")
def step_impl():
    raise NotImplementedError(u'STEP: And I can see my second Payment Card')


@when('I enter an incorrect "<email_address>" and correct "<password>" in the relevant fields')
def step_impl():
    raise NotImplementedError(
        u'STEP: When I enter an incorrect "<email_address>" and correct "<password>" in the relevant fields')


@then("I see a 'incorrect credential, please try again' error message")
def step_impl():
    raise NotImplementedError(u'STEP: Then I see a \'incorrect credential, please try again\' error message')


@given("I am not logged in")
def step_impl():
    raise NotImplementedError(u'STEP: And I am not logged in')
