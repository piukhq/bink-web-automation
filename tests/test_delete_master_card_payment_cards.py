# """ As a Bink Wasabi Customer
#     I Want to Delete One/Multiple MASTERCARD Payment Cards
#     So that I don't collect points """
#
# from pages.AccountPage import AccountPage
# from pages.LoginPage import LoginPage
# from test_data.test_data import TestData
# from test_data.test_data_staging import MASTERCARD_CARD_NUMBER, MASTERCARD_CARD_NAME
# from tests.base_class import BaseClass
#
#
# class DeleteMasterCardPaymentCardTests(BaseClass):
#
#     def test_delete_one_payment_card(self):
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
#         """ Delete Payment Card """
#         # TBC
