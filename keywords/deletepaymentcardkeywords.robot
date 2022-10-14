*** Settings ***
Library    SeleniumLibrary
Variables   ../pageobjects/locators.py

*** Variables ***
${lastfournumber}   7548

*** Keywords ***
Click Delete Payment Card Button
    click element    ${click_deleteIcon}
    page should contain    Delete this card
    input text    ${txt_enterlastfourdigits}    ${lastfournumber}
    click element    ${btn_removeCard}
    sleep   5
