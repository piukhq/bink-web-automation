import random
import string

# ------------------------------------------------ Randomised Data -----------------------------------------------

six_random_numbers = random.randint(100, 999999)
length_of_string = 5
random_string = "".join(random.choice(string.ascii_letters) for i in range(length_of_string))


def get_expiry_date():
    months = list(range(1, 13))  # 12 months list
    year = list(range(2022, 2040))  # years list here
    val = '{:02d}/{}'.format(random.choice(months), random.choice(year))
    first_half = val[:3]
    last_half = val[5:]
    two_digit_year = first_half + last_half
    return two_digit_year


card_expiry_date = get_expiry_date()

# ----------------------------------------PAYMENT  CARDS ------------------------------------------------------- #
INVALID_EXPIRY_DATE = '10-30'

""" VISA CARD """

VISA_CARD_NUMBER = "424242" + str(six_random_numbers) + "4242"
VISA_CARD_NUMBER_SPREEDLY = '4111111111111111'
VISA_EXPIRY_DATE = card_expiry_date
VISA_CARD_NAME = 'visame' + random_string

""" AMEX """

AMEX_CARD_NUMBER = "401288" + str(six_random_numbers) + "2023"
AMEX_CARD_NUMBER_SPREEDLY = '378282246310005'
AMEX_EXPIRY_DATE = card_expiry_date
AMEX_CARD_NAME = 'amexme' + random_string

""" MASTERCARD """

MASTERCARD_CARD_NUMBER = "401288" + str(six_random_numbers) + "9111"
MASTERCARD_CARD_NUMBER_SPREEDLY = '5555555555554444'
MASTERCARD_EXPIRY_DATE = card_expiry_date
MASTERCARD_CARD_NAME = 'mastercardme' + random_string


""" Existing User Card """
XRP_CARD_NAME = 'XRP'