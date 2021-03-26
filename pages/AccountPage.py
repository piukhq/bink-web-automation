from selenium.webdriver.common.by import By

from TestData.test_data import TestData
from pages.BasePage import BasePage


class AccountPage(BasePage):
    """ Constructor """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ Page Actions """

    ADD_PAYMENT_CARD_BUTTON = (By.XPATH, "//div[@id='root']/div/div[2]/div[3]/div/div/div")


    """ Add a Payment Card """
