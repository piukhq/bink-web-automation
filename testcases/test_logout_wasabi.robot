*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/loginkeywords.robot
Resource    ../resources/logoutkeywords.robot

Test Setup    Start Browser
Test Teardown   Kill Browser

*** Test Cases ***
Verify Wasabi Club Modal
    Enter UserName
    Enter Password
    Click Login
    Logout Wasabi
