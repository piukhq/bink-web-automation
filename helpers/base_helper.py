""" Base class for all pages """

""" Contains all generic methods and utilities """

from selenium.webdriver.support.ui import WebDriverWait


class HelperFunc(object):
    __TIMEOUT = 10

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

#     def visit(self, location=''):
#         """
#         navigate webdriver to different pages
#         """
#
#         base_url = 'https://'
#
#         url = base_url + location
#         self._driver.get(url)
#
#     #
#     # def open(self, url):
#     #     self._driver.get(url)
#     #
#     # def maximize(self):
#     #     self._driver.maximize_window()
#     #
#     # def close(self):
#     #     self._driver.quit()
#
#     # Helper functions that are used to identify the web locators in Selenium Python tutorial
#     #
#     # def find_by_xpath(self, xpath):
#     #     return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
#     #
#     # def find_by_name(self, name):
#     #     return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
#     #
#     # def find_by_id(self, id):
#     #     return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))
