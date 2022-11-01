*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py

*** Keywords ***
Verify in progress voucher
    page should contain    Vouchers
    page should contain    Spend £7 or more to get a new stamp on each order. Once you collect 7 stamps, you will get a £7 off Meal Voucher!
    wait until element is visible    ${txt_in_progress_voucher}   1s
    page should contain    Free Meal
    page should contain    for collecting 7 stamps
    page should contain    4 stamps to go
    wait until element is visible    ${stamp_in_progress_1}    1s
    wait until element is visible    ${stamp_in_progress_2}    1s
    wait until element is visible    ${stamp_in_progress_3}    1s
    page should contain    Collected
    page should contain    3/7 stamps


Verify Earned voucher
    wait until element is visible    ${btn_earned_voucher}    1s
    mouse over    ${btn_earned_voucher}
    mouse down    ${btn_earned_voucher}
    page should contain    Free Meal
    page should contain    for collecting 7 stamps
    page should contain    Earned
    wait until element is visible    ${stamp_earned_1}    0.5s
    wait until element is visible    ${stamp_earned_2}    0.5s
    wait until element is visible    ${stamp_earned_3}    0.5s
    wait until element is visible    ${stamp_earned_4}    0.5s
    wait until element is visible    ${stamp_earned_5}    0.5s
    wait until element is visible    ${stamp_earned_6}    0.5s
    wait until element is visible    ${stamp_earned_7}    0.5s
    capture page screenshot

Verify Earned voucher code
    click element    ${btn_earned_voucher}
    wait until element is visible    ${alt_hero_logo}
    page should contain    Free Meal for collecting 7 stamps
    page should contain    1
    page should contain    2
    page should contain    D
    page should contain    Q
    page should contain    6
    page should contain    9
    page should contain    6
    page should contain    S
    page should contain    Show your Wasabi Club reward code in store to redeem £7 off your next meal.
    page should contain    Added 10 Jun 2020
    page should contain    Expires 10 Jan 2023
    page should contain    Terms & Conditions
    click link    ${link_terms_conditions}
    sleep    2
    click element    ${btn_earned_close}
