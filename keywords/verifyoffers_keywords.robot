*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py

*** Keywords ***
Verify Offers
    wait until page contains     Offers
    execute javascript    window.scrollTo(0,400)
    mouse over    ${mouseover_offer}
    sleep    3
    mouse down on image    ${mouseover_offer}
    capture page screenshot
    sleep    1
