""" Confest contains all share fixtures that will be resued in all tests - i.e Browser set up"""

from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@fixture(params=["chrome"], scope='function')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield

    web_driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"

    )

#
# @fixture(scope='class')
# def setup(request):
#     # GO TO WEBSITE
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_name == "fireforx":
#         driver = webdriver.Firefox()
#     driver.get('https://web.staging.gb.bink.com/staging/wasabi/login')
#     driver.maximize_window()
#
#     # request.cls.driver = driver
#     yield driver
#     driver.quit()

#
# @fixture(autouse=True, params=[webdriver.Chrome, webdriver.Firefox])
# def browser(request):
#     driver = request.param
#     browser_driver = driver()
#     yield browser_driver
#     browser_driver.quit()
#     browser_driver.close()
