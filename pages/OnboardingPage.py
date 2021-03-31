from selenium.webdriver.common.by import By

from test_data.test_data import TestData
from pages.BasePage import BasePage


class OnboardingPage(BasePage):
    """ Constructor """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.STAGING_URL_DEBUG)

    """ Page Actions """

    GET_CARD_BUTTON = (By.XPATH, "//button[contains(text(),'Get a new card')]")
    FIRST_NAME_ENROLMENT_INPUT_FIELD = (By.ID, "bink-form-field-first_name")
    LAST_NAME_ENROLMENT_INPUT_FIELD = (By.ID, "bink-form-field-last_name")
    EMAIL_ENROLMENT_INPUT_FIELD = (By.ID, "bink-form-field-email")
    DOB_ENROLMENT_INPUT_FIELD = (By.ID, "bink-form-field-date_of_birth")
    TERMS_AND_CONDITIONS_ENROLMENT = (By.ID, "bink-form-field-retailer-terms-and-conditions")
    ADD_CARD_ENROLMENT_BUTTON = (By.XPATH, "//button[contains(text(),'Add my card')]")

    """ Click Get Card Button to Start Enrolment """

    def click_the_get_card_button(self):
        self.perform_click(self.GET_CARD_BUTTON)

    """ Complete & Submit the enrolment form """

    def switch_to_onboarding_modal(self):
        self.switch_to_element()

    def complete_enrolment_form_input_fields(self, first_name, last_name, email, dob):
        self.perform_send_keys(self.FIRST_NAME_ENROLMENT_INPUT_FIELD, first_name)
        self.perform_send_keys(self.LAST_NAME_ENROLMENT_INPUT_FIELD, last_name)
        self.perform_send_keys(self.EMAIL_ENROLMENT_INPUT_FIELD, email)
        self.perform_send_keys(self.DOB_ENROLMENT_INPUT_FIELD, dob)
        self.scroll_down()
        self.perform_click(self.TERMS_AND_CONDITIONS_ENROLMENT)
        self.perform_click(self.ADD_CARD_ENROLMENT_BUTTON)
