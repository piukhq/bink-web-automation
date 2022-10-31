*** Settings ***
Library    SeleniumLibrary
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/general_keywords.robot
Resource    ../keywords/addpaymentcard_keywords.robot
Resource    ../keywords/deletepaymentcard_keywords.robot
Resource    ../keywords/verifyoffers_keywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser

*** Test Cases ***
Verify Offers Tile
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
    Verify Offers
    Delete Payment Card Visa
