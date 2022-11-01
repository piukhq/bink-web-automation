*** Settings ***
Library     Selenium2Library
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/general_keywords.robot
Resource    ../keywords/logout_keywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser


*** Test Cases ***
Verify Wasabi Club Modal
    Launch the Wasabi App
    Enter UserName
    Enter Password
    Click Login
    Logout Wasabi
