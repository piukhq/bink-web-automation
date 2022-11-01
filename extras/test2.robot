*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Testing1
    open browser    https://coinmarketcap.com/  chrome
    maximize browser window
    sleep    2
    select from list by label    //*[@id="__next"]/div/div[1]/div[2]/div/div/div[4]/div[2]/div[3]/div[1]/div/svg    50
