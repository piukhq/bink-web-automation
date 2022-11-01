*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py

*** Keywords ***
Verify Wasabi Club Modal
    click element   ${click_wasabi_club_modal}
    sleep   2
    page should contain    Wasabi Club support
    sleep   2
    click element    ${link_wasabiclubfaq}
    get window handles  1
    sleep    2
    click element    ${link_wasabi_club_terms_conditions}
    sleep    2
    click element    ${link_binkfaq}
    sleep    3
    click element    ${link_bink_terms_conditions}
    sleep    3
    click element    ${link_bink_privacy_policy}
    sleep    3
    click element    ${link_cookies_policy}
    sleep    2
    click element   ${btn_close}
