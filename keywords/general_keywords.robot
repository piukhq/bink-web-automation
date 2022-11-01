*** Settings ***
Library     Selenium2Library
Library     OperatingSystem


*** Variables ***
${url}  https:wasabi.staging.gb.bink.com/login?debugLogin=true


*** Keywords ***

Include Browser Drivers
    get window size
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --disable-extensions
    Call Method    ${chrome_options}    add_argument    --headless
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    window-size\=1440,813
    Create Webdriver    Chrome    chrome_options=${chrome_options}

Launch the Wasabi App
    Go To   ${url}


Kill Browser
    Close All Browsers
