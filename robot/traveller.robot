*** Settings ***
Documentation     Gofore junior developer assignment cracking roboto.
Library  Browser
Library  String
Library  Collections
Library  OperatingSystem
Library  ./libraries/MapHandler.py

*** Variables ***
${OUTPUT_DIR}  ./output
${RESULTS}  results.txt

*** Tasks ***
Traverse Map And Calculate Steps
  Navigate To Assignment Page
  ${mapString}  Get Current Map
  ${mapCode}  Get Current Map Id  ${mapString}
  ${map}  Prepare Map For Manipulation  ${mapString}
  Navigate Map  ${map}  ${mapCode}

*** Keywords ***
Navigate To Assignment Page
  New Browser    chromium    headless=true
  New Page       https://gofore.com/junior-developer-assignment/
  Get Title      ==    Junior-developer-assignment - Gofore
  Click  //button[@class='cmplz-btn cmplz-accept cc-allow cc-btn']

Get Current Map
  ${mapString}  Get Text  id=map
  [Return]  ${mapString}

Get Current Map Id
  [Arguments]  ${mapString}
  ${mapCode}  Get Line  ${mapString}  0
  ${mapCode}  Convert To Integer  ${mapCode}
  [Return]  ${mapCode}

Prepare Map For Manipulation
  [Arguments]  ${mapString}
  ${mapRows}  Split To Lines  ${mapString}  1
  ${map}  Create List
  FOR  ${row}  IN  @{mapRows}
    ${tempRow}  Turn String Into List Of Characters  ${row}
    Append To List  ${map}  ${tempRow}
  END
  [Return]  ${map}

Navigate Map
  [Arguments]  ${map}  ${mapCode}
  ${location}  Find Robot Location  ${map}
  ${steps}  Traverse Map  ${map}  ${location}
  ${result}  Set Variable
  ...  Map ID ${mapCode} solved in ${steps} steps
  Log  ${result}
  Append To File  ${OUTPUT_DIR}/${RESULTS}  ${result}\n