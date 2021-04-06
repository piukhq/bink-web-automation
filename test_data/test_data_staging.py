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

""" VISA CARD """

VISA_CARD_NUMBER = "401288" + str(six_random_numbers) + "1813"
VISA_CARD_NUMBER_SPREEDLY = '4111111111111111'
VISA_EXPIRY_DATE = card_expiry_date
VISA_CARD_NAME = 'Justhe' + random_string


