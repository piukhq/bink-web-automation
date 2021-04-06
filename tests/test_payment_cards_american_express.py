from pages.AccountPage import AccountPage
from pages.LoginPage import LoginPage
from test_data.test_data import TestData
from test_data.test_data_staging import VISA_EXPIRY_DATE, VISA_CARD_NAME, VISA_CARD_NUMBER_SPREEDLY
from tests.base_class import BaseClass


class PaymentCardVisaTests(BaseClass):

    def test_add_one_payment_card(self):
        """ Enter Email & Click Login Button """

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        login_page = self.login_page
        account_page = self.account_page

        login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

        """ Add Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

    def test_add_two_payments_cards(self):
        """ Enter Email & Click Login Button """

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        login_page = self.login_page
        account_page = self.account_page

        login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

        """ Add First Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

        """ Add Second Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

    def test_add_three_payment_cards(self):
        """ Enter Email & Click Login Button """

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        login_page = self.login_page
        account_page = self.account_page

        login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

        """ Add First Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

        """ Add Second Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

        """ Add Third Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

    def test_delete_one_payment_card(self):
        """ Enter Email & Click Login Button """

        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        login_page = self.login_page
        account_page = self.account_page

        login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

        """ Add Visa Payment Card """

        account_page.add_payment_card(VISA_CARD_NUMBER_SPREEDLY, VISA_EXPIRY_DATE,
                                      VISA_CARD_NAME)
        customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
        assert customer_card_name == VISA_CARD_NAME

        """ Delete Payment Card """
        # TBC
