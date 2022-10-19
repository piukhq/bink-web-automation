*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Keywords ***
Verify Offers
    wait until page contains     Offers
    execute javascript    window.scrollTo(0,400)
    mouse over    ${mouseover_offer}
    sleep    3
    mouse down on image    ${mouseover_offer}
    click element    ${click_offer}
    sleep    3
