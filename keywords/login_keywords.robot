*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Variables ***
#${browser}    chrome
#${url}    https://wasabi.staging.gb.bink.com/login?debugLogin=true
${email}    QAtest+ws8@bink.com
${password}    Password01


*** Keywords ***

Enter UserName
    set selenium speed    1
    input text        ${txt_login_email}  ${email}


Enter Password
    input password    ${txt_login_password}    ${password}


Click Login
    click element    ${btn_login}




