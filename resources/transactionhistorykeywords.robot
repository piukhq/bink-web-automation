*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Keywords ***
View Transaction History
    wait until page contains    View history
    page should contain    5 stamps
    page should contain    View history
    click element  ${click_viewhistoryicon}
    page should contain    Transaction history
    page should contain    Your recent transaction history
    click element    ${click_close}
