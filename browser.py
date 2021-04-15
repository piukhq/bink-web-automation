from selenium import webdriver

""" Contains all generic methods and utilities """

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Browser(object):
    __TIMEOUT = 10

    base_url = 'https://'
    driver = webdriver.Chrome()

    # def __init__(self):
    #     super(Browser, self).__init__()
    #     self.driver_wait = 10
    #     self.driver_wait = WebDriverWait(Browser.__TIMEOUT)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def visit_manually(self, url):
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))

    def find_by_xpath(self, selector):
        """
        find a page element in the DOM
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))

    def find_by_class(self, selector):
        """
        find a page element in the DOM
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, selector)))

    def find_by_css(self, selector):
        """
        find a page element in the DOM
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def find_by_link_text(self, selector):
        """
        find a page element in the DOM
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))

    def find_by_name(self, selector):
        """
        find a page element in the DOM
        """

        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, selector)))

    def maximize(self):
        """
        maximise
        """
        self.driver.maximize_window()

    def get_magic_link_iframe(self, frame_ref):
        """
        Switch to iframe by index
        """
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, frame_ref)))
        self.driver.switch_to.frame(el)

    def get_magic_link(self, selector):
        magic_link_raw_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        return magic_link_raw_text.text

    def assert_page_title(self, page_header):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_any_elements_located(page_header))
    # Helper functions that are used to identify the web locators in Selenium Python tutorial

    # def find_by_xpath(self, xpath):
#        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#
#    def find_by_name(self, name):
#        return self.driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
#
#    def find_by_id(self, id):
#        return self.driver_wait.until(EC.visibility_of_element_located((By.ID, id)))
#
#
