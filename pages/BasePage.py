""" Base class for all pages """

""" Contains all generic methods and utilities """

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def perform_click_int(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def perform_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def get_home_page_title(self, page_header):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_any_elements_located(page_header))

    def refresh_current_page(self):
        pass

    def switch_to_element(self):
        element = self.driver.switch_to_active_element
        return element

    def switch_to_iframe(self, by_locator):
        size = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(by_locator))
        return size

    def switch_to_first_frame(self, position):
        self.driver.switch_to.frame(position)

    def switch_to_relevant_parent_frame(self):
        self.driver.switch_to.default_content()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
