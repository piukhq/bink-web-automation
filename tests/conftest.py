from pytest import fixture
import logging
from selenium import webdriver


@fixture(autouse=True, params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    browser_driver = driver()
    yield browser_driver
    browser_driver.quit()
    browser_driver.close()

