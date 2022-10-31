*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Keywords ***

View Reward History
    wait until element is visible    ${reward_icon}    2s
    wait until page contains    Reward History
    page should contain    See your past rewards
    capture page screenshot
    click element    ${click_reward_history}
    page should contain    Rewards history
    page should contain    Your past rewards

View Redeemed voucher
    page should contain    Free Meal
    page should contain    for collecting 7 stamps
    element text should be    ${txt_redeemed}   redeemed
    page should contain    on 27 Jan 2022


View Cancelled voucher
    page should contain    Free Meal
    page should contain    for collecting 7 stamps
    element text should be  ${txt_cancelled}    cancelled
    page should contain    on 20 Jan 2022


View Expired voucher
    page should contain    Free Meal
    page should contain    for collecting 7 stamps
    element text should be  ${txt_expired}    expired
    page should contain    on 30 Dec 2021
    capture page screenshot
    click element    ${reward_btn_close}