*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/loginkeywords.robot
Resource    ../resources/addpaymentcardkeywords.robot
Resource    ../resources/verifyofferskeywords.robot

Test Setup    Start Browser
Test Teardown   Kill Browser

*** Test Cases ***
Verify Offers Tile
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
    Verify Offers