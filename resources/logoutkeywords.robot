*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py



*** Keywords ***

Logout Wasabi
    click element   ${click_wasabiclubModal}
    page should contain    Wasabi Club support
    wait until element is visible    ${btn_logout}  3
    click button    ${btn_logout}
    sleep    2

