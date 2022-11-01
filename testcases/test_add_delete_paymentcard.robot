*** Settings ***
Library     Selenium2Library
Resource    ../keywords/addpaymentcard_keywords.robot
Resource    ../keywords/general_keywords.robot
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/deletepaymentcard_keywords.robot


Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser

*** Test Cases ***
Add Paymentcard
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
    Add Payment Button
    Enter Master CardNumber
    Select Exp Month
    Select Exp Year
    Enter Name on Card
    Click Add Credit Debit card Button
    Add Payment Button
    Enter American Express CardNumber
    Select Exp Month
    Select Exp Year
    Enter Name on Card
    Click Add Credit Debit card Button
    Verify Payment card added
    Delete Payment Card Visa
    Delete Payment Card Mastercard
    Delete Payment Card American Express
    Verify Add Payment card from Add Credit/Debit card
