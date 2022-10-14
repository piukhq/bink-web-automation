*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/loginkeywords.robot

Test Setup      Start Browser
Test Teardown   Kill Browser


*** Test Cases ***
LoginWasabi

    Enter UserName
    Enter Password
    Click Login



