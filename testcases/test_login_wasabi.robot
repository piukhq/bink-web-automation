*** Settings ***
Library    SeleniumLibrary
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/general_keywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser


*** Test Cases ***
LoginWasabi
    Launch the Wasabi App
    Enter UserName
    Enter Password
    Click Login



