*** Settings ***
Library    SeleniumLibrary
Variables   ../pageobjects/locators.py

*** Variables ***
${lastfournumber}   7548

*** Keywords ***
Click Delete Payment Card Button
    click element    ${click_deleteIcon}
    page should contain    Delete this card
    input text    ${txt_enter_four_digits}    ${lastfournumber}
    click element    ${btn_remove_card}
    sleep   5
