from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from TestData.test_data import TestData


class HomePage(BasePage):
    """ Constructor """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ Page Actions """

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



#
#
# home_page_title = (By.CLASS_NAME, "RequestMagicLink_root__headline__2zhXs")
# login_email_field = (By.ID, "bink-form-field-undefined")
# magic_link_continue_button = (By.XPATH,
#                               "//button[contains(text(),'Continue')]")
#
# def getHomePageTitle(self):
#     self.driver.find_element(HomePage.home_page_title)
#
# def getLoginEmailField(self):
#     self.driver.find_element(HomePage.login_email_field)
#
# def getContinueButton(self):
#     self.driver.find_element(HomePage.magic_link_continue_button)
