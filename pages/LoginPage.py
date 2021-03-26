from selenium.webdriver.common.by import By

from TestData.test_data import TestData
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """ Constructor """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.STAGING_URL)

        """ Page Actions """

    MAGIC_LINK_EMAIL_ADDRESS = ''
    EMAIL = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/label[1]/input[1]")
    PASSWORD = (By.XPATH, "//label[2]/input")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    PAGE_TITLE = (By.TAG_NAME, 'h1')
    PAYMENT_CARD_ADD_BUTTON = (By.CSS_SELECTOR, 'css=div.PaymentCardAdd_root__inner__1empu')


    """ Obtain the Page title """

    def get_login_page_title(self, title):
        return self.get_page_title(title)

    """ Used to Login to Application """

    def perform_login(self, email, password):
        self.perform_send_keys(self.EMAIL, email)
        self.perform_send_keys(self.PASSWORD, password)
        self.perform_click(self.LOGIN_BUTTON)




    def add_payment_card(self):
        self.perform_click(self.PAYMENT_CARD_ADD_BUTTON)

    def assert_authentication_text_visible(self, authenticated_messaged):
        return self.get_element_text(authenticated_messaged)
