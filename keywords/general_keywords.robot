*** Settings ***
Library    SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${browser}  chrome
${url}  https:wasabi.staging.gb.bink.com/login?debugLogin=true


*** Keywords ***

Include Browser Drivers
    get window size

Launch the Wasabi App
    open browser   ${url}  ${browser}
    maximize browser window


Kill Browser
    close browser
