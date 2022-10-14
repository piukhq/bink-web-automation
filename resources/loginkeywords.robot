*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Variables ***
${browser}    chrome
${url}    https://wasabi.staging.gb.bink.com/login?debugLogin=true
${email}    testbink123+ml56@gmail.com
${password}    Password01


*** Keywords ***
Start Browser
    open browser    ${url}  ${browser}
    MAXIMIZE BROWSER WINDOW


Enter UserName
    set selenium speed    1
    input text        ${txt_loginEmail}  ${email}


Enter Password
    input password    ${txt_lpginPassword}  ${password}


Click Login
    click element    ${btn_login}


Kill Browser
    close browser