from browser import Browser

BEHAVE_DEBUG_ON_ERROR = False
# from allure_behave.hooks import allure_report


# def setup_debug_on_error(userdata):
#     global BEHAVE_DEBUG_ON_ERROR
#     BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_scenario(context, scenario):
    if scenario:
        context.browser = Browser()
        context.browser.maximize()
        context.config.setup_logging()

    # setup_debug_on_error(context.config.userdata)


# def after_step(context, step):
#     if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
#         # -- ENTER DEBUGGER: Zoom in on failure location.
#         # NOTE: Use IPython debugger, same for pdb (basic python debugger).
#         import ipdb
#         ipdb.post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    if scenario:
        context.browser = Browser()
        context.browser.close()
        context.config.setup_logging()


# def before_all(context):
#     config = ConfigParser()
#     print((os.path.join(os.getcwd(), 'setup.cfg')))
#     my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
#     config.read(my_file)
#
#     # Reading the browser type from the configuration file for Selenium Python Tutorial
#     helper_func = get_browser(config.get('Environment', 'Browser'))
#     context.helperfunco = helper_func
#
#     # # Local Chrome WebDriver
#     # if context.browser == "chrome":
#     #     context.driver = webdriver.Chrome()
#
#
# def after_all(context):
#     context.helperfunco.close()
#
# allure_report("path/to/result/dir")
