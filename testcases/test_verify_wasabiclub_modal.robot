*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/loginkeywords.robot
Resource    ../resources/verifywasabiclubmodalkeywords.robot

Test Setup    Start Browser
Test Teardown   Kill Browser

*** Test Cases ***
Verify Wasabi Club Modal
    Enter UserName
    Enter Password
    Click Login
    sleep    2
    Verify Wasabi Club Modal