*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  hei  salasana1
    Output Should Contain  New user registered

Register With Too Short Username And Valid Password
    Input Credentials  hx  salasana1
    Output Should Contain  Username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  user  sala1
    Output Should Contain  Password has to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  salasana
    Output Should Contain  Password can't consist of only a-z letters