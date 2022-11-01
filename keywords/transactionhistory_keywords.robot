*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py

*** Keywords ***
View Transaction History
    wait until element is visible    ${transaction_history_icon}    2s
    wait until page contains    View history
    page should contain    3 stamps
    page should contain    View history
    capture page screenshot
    click element  ${click_view_history_icon}
    page should contain    Transaction history
    page should contain    Your recent transaction history
    page should contain    +1 stamps
    page should contain    01 Dec 2021
    page should contain    Ascot 1 Petty Cury £8.00
    page should contain    +1 stamps
    page should contain    02 Nov 2021
    page should contain    Ascot 2 Petty Cury £15.60
    page should contain    +1 stamps
    page should contain    10 Oct 2021
    page should contain    Ascot 3 Petty Cury £10.02
    page should contain    +1 stamps
    page should contain    10 Sep 2021
    page should contain    Ascot 4 Petty Cury £11.75
    capture page screenshot
    click element    ${click_close}
