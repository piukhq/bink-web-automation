*** Settings ***
Library    SelenoumLibrary
Resource    ../resources/loginkeywords.robot
Resource    ../resources/deletepaymentcardkeywords.robot

Test Setup    Start Browser
Test Teardown   Kill Browser

*** Test Cases ***
Delete Payment Card
    Enter UserName
    Enter Password
    Click Login
    Click Delete Payment Card Button
