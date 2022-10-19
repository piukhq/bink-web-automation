*** Settings ***
Library    SeleniumLibrary
Library     OperatingSystem


*** Variables ***
${browser}  chrome
${url}  https:wasabi.staging.gb.bink.com/login?debugLogin=true


*** Keywords ***

Include Browser Drivers
    Append To Environment Variable  PATH   ${EXECDIR}/resources/driver
    Set Environment Variable  webdriver.chrome.driver  ${EXECDIR}/resources/driver/chromedriver
    log   ${EXECDIR}/resources/driver/chromedriver

Launch the Wasabi App
    open browser   ${url}  ${browser}
    maximize browser window


Kill Browser
    close browser
