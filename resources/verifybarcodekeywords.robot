*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py


*** Variables ***
${Membershipcardnumber}  1048447393


*** Keywords ***
Verify Barcode
    click element    ${click_membershipcard}
    sleep    2
    page should contain    ${Membershipcardnumber}
    click element    ${btn_close}
