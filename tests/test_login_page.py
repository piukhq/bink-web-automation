""" As a Bink Wasabi Customer
    I Want to Login to my Bink Web Wasabi Account
    So That I can access my account """


from test_data.test_data import TestData
from pages.LoginPage import LoginPage
from tests.base_class import BaseClass


class LoginTests(BaseClass):

    def test_page_title_visible(self):
        self.login_page = LoginPage(self.driver)

    def test_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_page_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE

    def test_login_with_existing_user_credentials(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.perform_login(TestData.USERNAME, TestData.PASSWORD)

    def test_login_with_invalid_credentials(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.perform_login(TestData.INVALID_USERNAME_FORMAT, TestData.PASSWORD)
