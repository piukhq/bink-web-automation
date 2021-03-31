import random
import string

# ------------------------------------------------ Randomised Data -----------------------------------------------

six_random_numbers = random.randint(100, 999999)
length_of_string = 5
random_string = "".join(random.choice(string.ascii_letters) for i in range(length_of_string))


def get_expiry_date():
    months = list(range(1, 13))  # 12 months list
    year = list(range(2022, 2040))  # years list here
    val = '{}/{:02d}'.format(random.choice(year), random.choice(months))
    return val


card_expiry_date = get_expiry_date()

# ----------------------------------------PAYMENT  CARDS ------------------------------------------------------- #

""" VISA CARD """

VISA_CARD_NUMBER = "401288" + str(six_random_numbers) + "1813"
VISA_EXPIRY_DATE = card_expiry_date
VISA_CARD_NAME = 'Just For the' + random_string

# visa_payment_card = {
#     "first_six_digits": "401288",
#     "middle_six_digits": six_random_number,
#     "last_four_digits": "1813",
#     "name_on_card": "Avery",
#     "month": 10,
#     "year": 2026
# }
