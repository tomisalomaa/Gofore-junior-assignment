# A robot for solving Gofore Junior Developer Assignment

## Description
Peep poop I am a robot who loves travelling hashtag filled maps. My only weaknesses are the inabilities to foresee obstables and then turn anywhere but right when conforted with them.

This robot visits https://gofore.com/junior-developer-assignment/ and takes one good look at the map available during that specific instance. After a bit of map manipulation into a more suitable format, it traverses the map and logs the whole adventure into the robot Framework (RF) log file available after the run. Also writes memoirs into the results.txt file.

## Executing

If requirements (see below) are already met, the robot can be put to work by running the following command in the project root directory:

    robot -d .\robot\output\ .\robot\traveller.robot

After the execution logs are available in the output folder:
- log.html produced by the RF run (id and steps available here as well)
- results.txt written by the program (includes map id and steps)

## Requirements
This project was built with Robot Framework 4.1.2 and it uses the following libraries:
- Browser
- Builtin
- String
- Collections
- OperatingSystem
- MapHandler (custom library)

Required python version is 3.7 or newer.

The Browser library requires node.js which is available for download [here](https://nodejs.org/en/download/).

Pip can be used to install the library itself

    pip install robotframework-browser

or by using pip together with the requirements.txt in the root of this project

    pip install -r requirements.txt

in which case both the Robot Framework and the Browser library will be installed.
