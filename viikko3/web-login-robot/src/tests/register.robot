*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kayttaja
    Set Password  salasana1
    Set Password Confirmation  salasana1
    Submit Credentials
    Register Should Succeed
    

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  salasana3
    Set Password Confirmation  salasana3
    Submit Credentials
    Register Should Fail With Message  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kayttajaa
    Set Password  Sala
    Set Password Confirmation  Sala
    Submit Credentials
    Register Should Fail With Message  Password has to be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kayttajaa
    Set Password  salasana1
    Set Password Confirmation  salasana2
    Submit Credentials
    Register Should Fail With Message  Password doesn't match with confirmation

*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!