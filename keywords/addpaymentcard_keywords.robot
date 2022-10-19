*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Variables ***
${Visacardnumber}   4539985769257548
${nameoncard}   Testuser
${Mastercardnumber}    5113468798670008
${Americancardnumber}    378324244483655

*** Keywords ***
Add Payment Button
    click element    ${btn_add_payment_card}
    wait until page contains    Add credit/debit card

Enter Visa CardNumber
    select frame    tag:iframe
    wait until page contains element    ${txt_cardnumber}
    input text    ${txt_cardnumber}   ${Visacardnumber}
    unselect frame

Select Exp Month
    select from list by label   ${drp_expmonth}    01

Select Exp Year
    select from list by label    ${drp_expyear}    25

Enter Name on Card
    input text    ${txt_name_on_card}   ${nameoncard}

Click Add Credit Debit card Button
    click element    ${btn_add_card}
    sleep    4

Verify Payment card added
    execute javascript    window.scrollTo(0,document.body.scrollHeight)
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)






