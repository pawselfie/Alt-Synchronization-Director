# Alt Synchronization Director
A python script that, utilizing Discord POST requests and a GUI, makes moving alternate accounts fast and easy.

Notes:
This script uses [aqts](https://github.com/aqts-aqts)' [Natro Alt Synchronization](https://github.com/aqts-aqts/Natro-Alt-Synchronization) extension for [Natro Macro](https://github.com/NatroTeam/NatroMacro), so make sure to set it up before utilizing this script.
Make sure to check out the [AHK version](https://github.com/pawselfie/AHK-Alt-Synchronization-Director) too.

## Setup:
1. Set any alts you want to use this script on as "follower" accounts in [aqts](https://github.com/aqts-aqts)' [Natro Alt Synchronization](https://github.com/aqts-aqts/Natro-Alt-Synchronization) first, and keep track of which channel(s) you're using.
2. Download the files and place them in the same directory, the script won't run if 'followto.ini' and 'map.png' are not in the directory.
3. Open 'followto.ini' and get your Discord Authentication Token, which you can find how to get [here](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6), then paste it on 'token'.
4. Change 'altnum' to the number of channels you want to control, and paste the Channel IDs, which you can find how to get [here](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID), on 'channel1', 'channel2' and 'channel3'.
5. Once 'followto.ini' has been setup, you'll just need to run 'Alt Synchronization Director.exe' (maybe whitelist it off Windows Defender, as it's an unsigned .exe and it may be flagged as malware), or run the main.py file if you have python and know how to install the required libraries installed.
6. Accept the free trial or make a hobbyist account in PySimpleGui, then you're done!

## Usage:
1. Select the field you want the alt to go to.
2. Select which alt to send. (if you only have 1 alt/channel enabled you don't need to worry about this)
3. Click "Go to field!" and if you've set everything correctly, the alt account will reset/walk to hive, and travel to the field you selected.

## Useful Applications:
1. Robo Bear Challenge:
    -   Send up to 3 alts to the fields you need to complete quests of.
    -   Easily be able to keep precision mid-rounds, as sending the account takes no time.
    -   Even when using less than 3 alts, sending the alts to the next field can be done easily while playing as it only takes 2 clicks. 

2. Stick Bug Challenge:
    -   Send alts to far-away totems when you can't afford to spend the time to get them yourself.
    -   Be able to send them while fighting stick bug.

3. Remote Computers:
    -   Remotely control alts even if you cannot access the computer in which they are running.
    -   Have your friends run the macro in their computers if you cannot macro them while playing.

Make sure to dm @pawselfie for any bug reports or questions you may have!
