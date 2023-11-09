*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/
${pageTitle}    OrangeHRM

*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    loginToApp          # Logging into teh app
    title should be     ${pageTitle}
    VerifyDashboardPage     # Verifying the user has landed on Dashboard page

*** Keywords ***
loginToApp
    maximize browser window
    Set Browser Implicit Wait   5
    input text  xpath://input[@placeholder='Username']  Admin
    input text  xpath://input[@placeholder='Password']  admin123
    click element   xpath://button[@type='submit']
    sleep   5

VerifyDashboardPage
    ${actualResult}    Get Text    //span[@class='oxd-topbar-header-breadcrumb']
    ${actualResult}   Evaluate    "Dashboard"


