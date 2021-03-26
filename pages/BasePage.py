""" Base class for all Pages """
from selenium.webdriver.common.by import By

""" Contains all generic methods and utilities """

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def perform_click(self, by_locator):
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
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(page_header))

    def refresh_current_page(self):
        pass

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")






