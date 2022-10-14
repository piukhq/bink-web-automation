*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Keywords ***

View Reward History
    wait until page contains    Reward History
    page should contain    See your past rewards
    click element    ${click_rewardhistory}
    page should contain    Rewards history
    page should contain    Your past rewards
    click element    ${clickbtn_close}