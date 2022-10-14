*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Keywords ***
Verify Wasabi Club Modal
    click element   ${click_wasabiclubModal}
    sleep   2
    page should contain    Wasabi Club support
    sleep   2
    click element    ${link_wasabiclubfaq}
    get window handles  1
    sleep    2
    click element    ${link_wasabiclubtermsandconditions}
    sleep    2
    click element    ${link_binkfaq}
    sleep    3
    click element    ${link_binktermsandconditions}
    sleep    3
    click element    ${link_binkprivacypolicy}
    sleep    3
    click element    ${link_cookiespolicy}
    sleep    2
    click element   ${btn_click}