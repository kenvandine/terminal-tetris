*** Settings ***
Documentation    Test cases for terminal-tetris snap
Resource         kvm.resource
Library          Process


*** Test Cases ***
Terminal Tetris Launches And Renders
    [Documentation]    Verify terminal-tetris snap launches in a foot terminal on Mir
    [Tags]    smoke    yarf:certification_status: blocker
    Start Process    /usr/bin/foot    snap    run    terminal-tetris    alias=terminal-tetris
    Sleep    3s
    Log Screenshot
    [Teardown]    Terminate Process    terminal-tetris
