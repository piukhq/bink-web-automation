*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/loginkeywords.robot
Resource    ../resources/addpaymentcardkeywords.robot

Test Setup    Start Browser
Test Teardown   Kill Browser

*** Test Cases ***
Add Paymentcard
    Enter UserName
    Enter Password
    Click Login
    Click Add Payment Button
    Enter CardNumber
    Select Exp Month
    Select Exp Year
    Enter Name on Card
    Click Add Credit Debit card Button
    Verify Payment card added

