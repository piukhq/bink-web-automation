# Bink Web - UI Automation: Robot Framework🚀

- This is a Python framework for the test automation of Bink's Web UI.
- The framework has been designed using the Pytest-BDD plugin to implement the BDD approach.
- Modules of the framework are designed in such a way that it can be reused by all merchants in any channels
- This framework will provide a Regression testing suite for Bink Web & also serve for Sanity, Smoke testing & In- Sprint testing for all channels & merchants.


# Set Up 🏋️‍♀️

1. Clone it from this GitLab repository (https://github.com/binkhq/bink-web-automation)
2. Then install the project dependencies:

```shell
poetry config <pypi-url> <pypi-user> <pypi-pass>
poetry install
```
# Running Tests 🏃‍♂️
Use ``robot`` command to run the test and specify a folder where you need
to generate the reports and mention the path of the testcases (.robot files)

example: ``robot -d reports testcases/test_login_wasabi.robot``