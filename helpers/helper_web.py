from selenium import webdriver
from helpers.base_helper import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())
