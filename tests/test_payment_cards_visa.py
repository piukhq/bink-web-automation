from pages.AccountPage import AccountPage
from pages.LoginPage import LoginPage
from test_data.test_data import TestData
from test_data.test_data_staging import VISA_EXPIRY_DATE, VISA_CARD_NAME, VISA_CARD_NUMBER
from tests.base_class import BaseClass


class PaymentCardTests(BaseClass):

    def test_add_one_payment_card(self):
        """ Enter Email & Click Login Button """

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        login_page = self.login_page
        account_page = self.account_page

        login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

        """ Add Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME
