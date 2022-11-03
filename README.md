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


# Installing the Right Chromedriver 🔨
## MacOS
1. Check chrome version: 
```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
```
2. Download the correct [chromedriver](https://chromedriver.chromium.org/downloads) for that chrome version
3. Move it into an executable path
```
mv /Downloads/chromedriver /usr/local/bin/chromedriver
```
4. Then run the tests

      

# Running Tests 🏃‍♂️
1. Run `export WEBSITE_URL="https://wasabi.staging.gb.bink.com/login?debugLogin=true"`
2. Run `robot -d reports testcases/`
... coming soon
