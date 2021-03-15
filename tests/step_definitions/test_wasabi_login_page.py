from pytest_bdd import scenario, given, when, then, scenarios
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios("wasabi_ui/login/")


@given("I am a Bink Web Wasabi Customer")
def step_impl():
    pass


@given("I am on the Bink Web Wasabi Login Page")
def step_impl(browser):
    global login_page
    browser.get('https://web.dev.gb.bink.com/develop/wasabi/login')
    try:
        login_page = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    finally:
        assert login_page.text == "Login"
