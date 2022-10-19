*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/loginkeywords.robot
Resource    ../resources/verifybarcodekeywords.robot

Test Setup    Start Browser
Test Teardown   Kill Browser

*** Test Cases ***
Verify Barcode
    Enter UserName
    Enter Password
    Click Login
    Verify Barcode
