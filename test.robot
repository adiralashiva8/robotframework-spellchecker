*** Settings ***
Library    SeleniumLibrary
Suite Setup    Launch Google Application
Suite Teardown    Close All Browsers

*** Test Case ***
Validate Online Correction Page
    # navigate to online correction page
    Go To    https://www.onlinecorrection.com/
    # after navigating to page, test considered as complete
    # now SpellCheckerListener will perform spell check

Validate Metrics - Spell Checker
    # navigate to robotframework-metrics
    Go To    https://github.com/adiralashiva8/robotframework-metrics
    # after navigating to page, test considered as complete
    # now SpellCheckerListener will perform spell check

*** Keywords ***
Launch Google Application
    Open Browser    https://www.google.com/    headlesschrome