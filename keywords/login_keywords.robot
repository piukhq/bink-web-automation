*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py

*** Variables ***
${email}    QAtest+binkwebregression1@bink.com
${password}    Password01


*** Keywords ***

Enter UserName
    set selenium speed    1
    input text        ${txt_login_email}  ${email}


Enter Password
    input password    ${txt_login_password}    ${password}


Click Login
    click element    ${btn_login}

View LCD
    wait until element is visible    ${membership_card_wasabi_hero_img}    1s
    wait until element is visible    ${logo_powered_by_bink}    1s
    execute javascript    window.scrollTo(0,document.body.scrollHeight)
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)
    capture page screenshot
