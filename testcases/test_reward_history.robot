*** Settings ***
Library     Selenium2Library
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/addpaymentcard_keywords.robot
Resource    ../keywords/rewardhistory_keywords.robot
Resource    ../keywords/general_keywords.robot
Resource    ../keywords/deletepaymentcard_keywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser

*** Test Cases ***
# Scenario  Verify Reward History
Verify Reward History
    Launch the Wasabi App
    Enter UserName
    Enter Password
    Click Login
    Add Payment Button
    Enter Visa CardNumber
    Select Exp Month
    Select Exp Year
    Enter Name on Card
    Click Add Credit Debit card Button
    View Reward History
    View Redeemed voucher
    View Cancelled voucher
    View Expired voucher
    Delete Payment Card Visa
