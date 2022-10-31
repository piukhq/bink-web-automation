*** Settings ***
Library    SeleniumLibrary
Variables   ../pageobjects/locators.py

*** Variables ***
${lastfournumber_visa}   7548
${lastfournumber_mastercard}  0008
${lastfournumber_americanexpress}   3655


*** Keywords ***
 Delete Payment Card Visa
    click element    ${click_deleteIcon}
    page should contain    Delete this card
    input text    ${txt_enter_four_digits}    ${lastfournumber_visa}
    click element    ${btn_remove_card}
    sleep   3

Delete Payment Card Mastercard
    click element    ${click_deleteIcon}
    page should contain    Delete this card
    input text    ${txt_enter_four_digits}    ${lastfournumber_mastercard}
    click element    ${btn_remove_card}
    sleep   3

Delete Payment Card American Express
    click element    ${click_deleteIcon}
    page should contain    Delete this card
    input text    ${txt_enter_four_digits}    ${lastfournumber_americanexpress}
    click element    ${btn_remove_card}
    sleep   3
