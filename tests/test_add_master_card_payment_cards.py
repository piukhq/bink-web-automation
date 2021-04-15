# """ As a Bink Wasabi Customer
#     I want to add One/Multiple MASTERCARD Payment Cards
#     So that I can collect points """
#
# from pages.AccountPage import AccountPage
# from pages.LoginPage import LoginPage
# from test_data.test_data import TestData
# from test_data.test_data_staging import MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME
# from tests.base_class import BaseClass
#
#
# class AddMasterCardPaymentCardTests(BaseClass):
#
#     def test_add_one_payment_card(self):
#         """ Enter Email & Click Login Button """
#
#         self.login_page = LoginPage(self.driver)
#         self.account_page = AccountPage(self.driver)
#         login_page = self.login_page
#         account_page = self.account_page
#
#         login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)
#
#         """ Add MASTERCARD Payment Card """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
#
#     def test_add_two_payments_cards(self):
#         """ Enter Email & Click Login Button """
#
#         self.login_page = LoginPage(self.driver)
#         self.account_page = AccountPage(self.driver)
#         login_page = self.login_page
#         account_page = self.account_page
#
#         login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)
#
#         """ Add First MASTERCARD Payment Card """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
#
#         """ Add Second MASTERCARD Payment Card """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
#
#     def test_add_three_payment_cards(self):
#         """ Enter Email & Click Login Button """
#
#         self.login_page = LoginPage(self.driver)
#         self.account_page = AccountPage(self.driver)
#         login_page = self.login_page
#         account_page = self.account_page
#
#         login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)
#
#         """ Add First MASTERCARD Payment Card """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
#
#         """ Add Second MASTERCARD Payment Card """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
#
#         """ Add Third MASTERCARD Payment Card """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
#
#     def test_add_card_with_invalid_expiry_date_format(self):
#         """ Enter Email & Click Login Button """
#
#         self.login_page = LoginPage(self.driver)
#         self.account_page = AccountPage(self.driver)
#         login_page = self.login_page
#         account_page = self.account_page
#
#         login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)
#
#         """ Add MASTERCARD Payment Card with INVALID EXPIRY DATE """
#
#         account_page.add_payment_card(MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME,
#                                       MASTERCARD_CARD_NUMBER)
#         customer_card_name = account_page.CUSTOMER_NAME_ON_CARD()
#         assert customer_card_name == MASTERCARD_CARD_NAME
