*** Settings ***
Library    SeleniumLibrary
Variables    ../pageobjects/locators.py

*** Variables ***
${cardnumber}   4539985769257548
${nameoncard}   SSD


*** Keywords ***
Click Add Payment Button
    click element    ${btn_addpaymentcard}
    wait until page contains    Add credit/debit card

Enter CardNumber
    select frame    tag:iframe
    wait until page contains element    ${txt_cardnumber}
    input text    ${txt_cardnumber}   ${cardnumber}
    unselect frame

Select Exp Month
    select from list by label   ${drp_expmonth}    01

Select Exp Year
    select from list by label    ${drp_expyear}    25

Enter Name on Card
    input text    ${txt_naneoncard}    ${nameoncard}

Click Add Credit Debit card Button
    click element    ${btn_addcard}
    sleep    4

Verify Payment card added
    execute javascript    window.scrollTo(0,document.body.scrollHeight)
    execute javascript    window.scrollTo(0,-document.body.scrollHeight)






