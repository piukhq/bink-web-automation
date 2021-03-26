""" Todo:
Faker
Randommiser
..
..
..
"""


class TestData:
    """ Happy Path Data """
    BASE_URL = 'https://web.dev.gb.bink.com/develop/wasabi/login'
    BASE_URL_DEBUG = 'https://web.dev.gb.bink.com/develop/wasabi/login?debugLogin=true'
    STAGING_URL = 'https://web.staging.gb.bink.com/staging/wasabi/login'
    USERNAME = 'dkw_binkweb@testbink.com'
    PASSWORD = 'Password01'
    AUTHEN_TEXT = 'Not authenticated'

    PAGE_TITLE = 'React App'
    HOME_PAGE_TITLE = 'Access your loyalty card'

    """ Negative Data"""

    INVALID_USERNAME_FORMAT = 'IAMinvalid_'

