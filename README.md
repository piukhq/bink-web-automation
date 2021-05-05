# Bink Web - UI Automation: PyTest-BDD & Selenium 🚀

- This is a Python framework for the test automation of Bink's Web UI.
- The framework has been designed using the Pytest-BDD plugin to implement the BDD approach.
- Modules of the framework are designed in such a way that it can be reused by all merchants in any channels
- This framework will provide a Regression testing suite for Bink Web & also serve for Sanity, Smoke testing & In- Sprint testing for all channels & merchants.


# Set Up 🏋️‍♀️

1. Clone it from this GitLab repository [QA GitLab](https://git.bink.com/dwilliams/bink-web-automation)
2. Run \`pipenv install\` from the project's root directory.
3. * Optional Step : For Django Web UI tests, install the appropriate browser and WebDriver executable
    * Current Django tests use Chrome and
     [chromedriver](https://chromedriver.chromium.org/downloads) 
      

# Running Tests 🏃‍♂️
... coming soon

1. Test Execution:
    - Use `behave` command 
    - Use markers '--tags' to filter tests by BDD tags
    - The default environment is staging
  
2. To run Scenarios, examples:
    - behave --tags=add_mastercard                     : Execute Add Card Behaviour for Mastercard
    - behave --tags=magic_link                         : Execute Request Magic Link Behaviour for New & Existing Users
    - behave --tags=login                              : Execute Login Behaviour for Existing Users
    - behave --tags="magic_link mastercard"            : Execute Request Magic Link Behaviour for New & Existing Users & Add Card Behaviour for Mastercard 


3. To run Features, examples:
    - behave -i wasabi_login                           : Execute All Login Behaviour for Existing Users


4. Reports (WIP)

Currently - to generate a report add the following to the end of the command: -f allure - %allure_result_folder% ./features

Example: behave --tags=magic_link -f allure -o %allure_result_folder% ./features