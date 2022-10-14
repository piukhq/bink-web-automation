*** Settings ***
Library    SeleniumLibrary
Resource    ../keywords/loginkeywords.robot
Resource    ../keywords/generalkeywords.robot

Suite Setup      Include Browser Drivers
Test Teardown   Kill Browser


*** Test Cases ***
LoginWasabi
    Launch the Wasabi App
    Enter UserName
    Enter Password
    Click Login



