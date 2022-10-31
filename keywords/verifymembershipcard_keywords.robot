*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py


*** Variables ***
${Membershipcardnumber}  1048170400


*** Keywords ***
Verify Membershipcard Wasabi
    wait until element is visible    ${membership_card_wasabi_hero_img}    1s
    page should contain    ${Membershipcardnumber}
    mouse over    ${membership_card_wasabi_hero_img}
    sleep    1
    mouse down    ${membership_card_wasabi_hero_img}
    capture page screenshot
    click element    ${membership_card_wasabi_hero_img}
    sleep    2
    page should contain    Wasabi
    page should contain image    ${membership_card_wasabi_alt_hero_img}
    page should contain    Share this number in-store just like you would a physical loyalty card.
    page should contain    Membership number:
    page should contain    ${Membershipcardnumber}
    capture page screenshot
    click element    ${btn_close}
