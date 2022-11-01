*** Settings ***
Library     Selenium2Library
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/general_keywords.robot
Resource    ../keywords/deletepaymentcard_keywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser

*** Test Cases ***
Delete Payment Card
    Launch the Wasabi App
    Enter UserName
    Enter Password
    Click Login
    Click Delete Payment Card Button
