from selenium.webdriver.common.by import By

from test_data.test_data import TestData
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """ Constructor """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.STAGING_URL_DEBUG)

        """ Page Actions """

    MAGIC_LINK_EMAIL_ADDRESS_FIELD = (By.XPATH, "//div[@id='root']/div/div[2]/form/div[2]/input")
    MAGIC_LINK_CONTINUE_BUTTON = (By.XPATH, "//div[@id='root']/div/div[2]/form/button")
    EMAIL = (By.XPATH, "(//input[@value=''])[2]")
    PASSWORD = (By.XPATH, "(//input[@value=''])[2]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    PAGE_TITLE = (By.TAG_NAME, 'h1')
    ML_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Check your inbox!')]")
    PAYMENT_CARD_ADD_BUTTON = (By.CSS_SELECTOR, 'css=div.PaymentCardAdd_root__inner__1empu')

    """ Obtain the Page title """

    def get_login_page_title(self, title):
        return self.get_page_title(title)

    def get_the_page_header(self, page_header):
        return self.get_home_page_title(self.ML_PAGE_TITLE, page_header)

    """ Used to Login to Application """

    def perform_login(self, email, password):
        self.perform_send_keys(self.EMAIL, email)
        self.perform_send_keys(self.PASSWORD, password)
        self.perform_click(self.LOGIN_BUTTON)

    def request_magic_link(self, email):
        self.perform_send_keys(self.MAGIC_LINK_EMAIL_ADDRESS_FIELD, email)
        self.perform_click(self.MAGIC_LINK_CONTINUE_BUTTON)

    def add_payment_card(self):
        self.perform_click(self.PAYMENT_CARD_ADD_BUTTON)

    def assert_authentication_text_visible(self, authenticated_messaged):
        return self.get_element_text(authenticated_messaged)

