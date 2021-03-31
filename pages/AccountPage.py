from selenium.webdriver.common.by import By

from test_data.test_data import TestData
from pages.BasePage import BasePage


class AccountPage(BasePage):
    """ Constructor """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.STAGING_URL_DEBUG)

    """ Page Actions """

    ADD_PAYMENT_CARD_BUTTON = (By.XPATH, "//div[@id='root']/div/div[2]/div[3]/div/div/div")
    SPREEDLY_IFRAME = (By.NAME, "spreedly-number-frame-2754")
    CARD_NUMBER_FIELD = (By.ID, "card_number")
    CARD_EXPIRY_DATE = (By.XPATH, "//div[@id='root']/div/div[2]/div[5]/div[2]/div/form/div/div[3]/input")
    CARD_NAME = (By.XPATH, "//div[@id='root']/div/div[2]/div[5]/div[2]/div/form/div/div[4]/input")
    ADD_PAYMENT_NEXT_BUTTON = (By.XPATH, "//div[@id='root']/div/div[2]/div[5]/div[2]/div/form/button")
    ACCEPT_TERMS_BUTTON = (By.XPATH, "//div[@id='root']/div/div[2]/div[5]/div/div[2]/button")
    CUSTOMER_NAME_ON_CARD = (By.CLASS_NAME, "PaymentCard_root__name__qU08L")
    # driver.find_element_by_id("card_number").click()
    # driver.find_element_by_id("card_number").clear()
    # driver.find_element_by_id("card_number").send_keys("10101010101010101011111")
    #
    # driver.find_element_by_xpath("//input[@value='']").click()
    # driver.find_element_by_xpath("//input[@value='02/13']").clear()
    # driver.find_element_by_xpath("//input[@value='02/13']").send_keys("02/13")
    # driver.find_element_by_xpath("//input[@value='']").click()
    # driver.find_element_by_xpath("//input[@value='Lolol']").clear()
    # driver.find_element_by_xpath("//input[@value='Lolol']").send_keys("Lolol")
    # driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div[5]/div[2]/div/form/button").click()

    """ Add a Payment Card """

    def add_payment_card(self, card_number, expiry_date, name):
        self.perform_click(self.ADD_PAYMENT_CARD_BUTTON)
        # self.switch_to_iframe(self.SPREEDLY_IFRAME)
        self.switch_to_first_frame(0)
        self.perform_send_keys(self.CARD_NUMBER_FIELD, card_number)
        self.switch_to_relevant_parent_frame()
        self.perform_send_keys(self.CARD_EXPIRY_DATE, expiry_date)
        self.perform_send_keys(self.CARD_NAME, name)
        self.switch_to_relevant_parent_frame()
        self.perform_click(self.ADD_PAYMENT_NEXT_BUTTON)
        self.perform_click(self.ACCEPT_TERMS_BUTTON)

    def get_name_on_added_card(self):
        self.get_element_text(self.CUSTOMER_NAME_ON_CARD)
