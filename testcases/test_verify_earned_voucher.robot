*** Settings ***
Library    SeleniumLibrary
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/general_keywords.robot
Resource    ../keywords/addpaymentcard_keywords.robot
Resource    ../keywords/deletepaymentcard_keywords.robot
Resource    ../keywords/vouchers_keywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser

*** Test Cases ***
Verify vouchers in progress
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
    Verify Payment card added
    Verify in progress voucher
    Verify Earned voucher
    Verify Earned voucher code
    Delete Payment Card Visa
