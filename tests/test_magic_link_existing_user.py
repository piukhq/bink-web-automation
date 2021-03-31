""" The MAGIC LINK TEST CLASS contains all functions test in relation to Request a Magic Link
    for an Existing User """

import time

from pages.LoginPage import LoginPage
from test_data.test_data import TestData
from tests.base_class import BaseClass


class MagicLinkNewUserTests(BaseClass):

    def test_user_can_request_magic_link(self):
        """ Enter Email & Click Login Button """

        self.login_page = LoginPage(self.driver)
        login_page = self.login_page

        """ Request Magic Link """
        login_page.request_magic_link(TestData.MAGIC_LINK_EMAIL)
        time.sleep(1)

    def test_user_can_access_valid_magic_link(self):
        self.login_page = LoginPage(self.driver)
        login_page = self.login_page

        """ Request Magic Link """
        login_page.request_magic_link(TestData.MAGIC_LINK_EMAIL)
        time.sleep(1)

        # page_title = login_page.get_the_page_header(test_data.PAGE_TITLE_CHECK_INBOX)
        # assert page_title == test_data.PAGE_TITLE_CHECK_INBOX
