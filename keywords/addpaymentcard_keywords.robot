*** Settings ***
Library      Selenium2Library
Variables    ../pageobjects/locators.py

*** Variables ***
${Visacardnumber}   4539985769257548
${nameoncard}   Testuser
${Mastercardnumber}    5113468798670008
${AmericanExpresscardnumber}    378324244483655

*** Keywords ***
Add Payment Button
    click element    ${btn_add_payment_card}
    sleep    1
    wait until page contains    Add credit/debit card

#Add Visa card
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


#Add Master card
Enter Master CardNumber
    select frame    tag:iframe
    wait until page contains element    ${txt_cardnumber}
    input text    ${txt_cardnumber}   ${Mastercardnumber}
    unselect frame

#Add Amercan Express card
Enter American Express CardNumber
    select frame    tag:iframe
    wait until page contains element    ${txt_cardnumber}
    input text    ${txt_cardnumber}   ${AmericanExpresscardnumber}
    unselect frame


Verify Payment card added
    execute javascript    window.scrollTo(0,document.body.scrollHeight)
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)
    capture page screenshot

Verify Add Payment card from Add Credit/Debit card
    wait until element is visible    ${btn_img_red}    1s
    click element    ${btn_add_payment_card}
    sleep    2
    click link    ${link_security_privacy}
    sleep    1
    click element    ${btn_add_payment_card_modal_close}
