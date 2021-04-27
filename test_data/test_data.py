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
    STAGING_URL_DEBUG = 'https://web.staging.gb.bink.com/staging/wasabi/login?debugLogin=true'
    USERNAME = 'dkw_binkweb@testbink.com'
    PASSWORD = 'Password01'
    AUTHEN_TEXT = 'Not authenticated'

    PAGE_TITLE = 'React App'
    PAGE_TITLE_CHECK_INBOX = 'Check your inbox!'
    HOME_PAGE_TITLE = 'Access your loyalty card'
    FIRST_NAME = 'Terrence'
    LAST_NAME = 'Bud'
    EMAIL_ENROL = 'tbud@gmailck.com'
    DOB_ENROL = '10/04/1987'

    MAGIC_LINK_EMAIL = 'dwilliams@bink.com'
    MAILTRAP_PASSWORD = 'Qabinktest'
    MAILTRAP_EMAIL = "33cc7471de-f34439@inbox.mailtrap.io"
    TEMP_LOYALTY_NUMBER = '1048734113'

    """ Negative Data"""

    INVALID_USERNAME_FORMAT = 'IAMinvalid_'
