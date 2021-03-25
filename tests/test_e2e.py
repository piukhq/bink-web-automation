
import time
from logging import Logger

from TestData.test_data import TestData
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.base_class import BaseClass


class AddPaymentCardTests(BaseClass):

    def test_add_payment_card_journey(self):

        """ Enter Email & Click Login Button """
        self.login_page = LoginPage(self.driver)
        self.login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

        """ Click + Add Payment Card button """
        self.home_page.add_payment_card()

