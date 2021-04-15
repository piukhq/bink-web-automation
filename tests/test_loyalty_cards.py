# import time
#
# from test_data.test_data import TestData
# from pages.LoginPage import LoginPage
# from pages.OnboardingPage import OnboardingPage
# from tests.base_class import BaseClass
#
#
# class NewUserEnrolLoyaltyCardTests(BaseClass):
#
#     def test_enrol_loyalty_card(self):
#         """ Enter Email & Click Login Button """
#
#         self.login_page = LoginPage(self.driver)
#         self.onboarding_page = OnboardingPage(self.driver)
#         login_page = self.login_page
#         login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)
#
#         """ User Clicks Get Card Button """
#         self.onboarding_page.click_the_get_card_button()
#         time.sleep(2)
#
#         """ User Completes & Submit Enrolment Form """
#         self.onboarding_page.complete_enrolment_form_input_fields(TestData.FIRST_NAME, TestData.LAST_NAME,
#                                                                   TestData.EMAIL_ENROL, TestData.DOB_ENROL)
