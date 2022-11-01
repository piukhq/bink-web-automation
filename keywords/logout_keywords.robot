*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py



*** Keywords ***

Logout Wasabi
    wait until element is visible    ${click_wasabi_club_modal}    1s
    click element   ${click_wasabi_club_modal}
    page should contain    Wasabi Club support
    scroll element into view    ${btn_logout}
    wait until element is visible    ${btn_logout}  3
    click button    ${btn_logout}
    sleep    2
