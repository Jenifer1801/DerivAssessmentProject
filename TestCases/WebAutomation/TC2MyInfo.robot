*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/
${pageTitle}    OrangeHRM

*** Test Cases ***
Login to the App
    open browser    ${url}  ${browser}
    Login To Application          # Logging into teh app
    title should be     ${pageTitle}
    Verify User has landed to Dashboard Page     # Verifying the user has landed on Dashboard page
Update My Info Page
    Navigate To My Info page
    Wait For Condition	return document.readyState == "complete"
    Update and save the Information
*** Keywords ***
Login To Application
    maximize browser window
    Set Browser Implicit Wait   1
    input text  xpath://input[@placeholder='Username']  Admin
    input text  xpath://input[@placeholder='Password']  admin123
    click element   xpath://button[@type='submit']
    sleep   3

Verify User has landed to Dashboard Page
    ${actualResult}    Get Text    //span[@class='oxd-topbar-header-breadcrumb']
    ${actualResult}   Evaluate    "Dashboard"

Navigate To My Info page
    input text      //input[@placeholder='Search']      My Info
    click element   //a[@class='oxd-main-menu-item']/span
    sleep   2

Update and save the Information
    ${dateElements}=    Get WebElements    //input[@placeholder='yyyy-mm-dd']
    should not be equal as strings  ${dateElements[1]}  yyyy-mm-dd
    click element   ${dateElements[1]}
    press keys  ${dateElements[1]}  CTRL+a+BACKSPACE
    input text  ${dateElements[1]}  2022-10-03

    # Save the update
    ${saveButtons}=     Get WebElements     //button[@type='submit']
    click element   ${saveButtons[0]}
    sleep   3

    # Toast Message validation
    ${toastMessage}=  Get text  //div[@id='oxd-toaster_1']/div[1]/div[1]/div[2]/p[1]
    Should be equal  ${toastMessage}  Success
    click element   //div[@role='button']  #closing the toast

    #Logout from teh application
    click element   //p[@class='oxd-userdropdown-name']






