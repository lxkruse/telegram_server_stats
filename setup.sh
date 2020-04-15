#!/bin/bash


echo "RUNNING SETUP

"



echo "#####################################################
INSTALLING NESCESSARY PYTHON PACKAGES
#####################################################

"

#install all nescessary python-packages
pip3 install watchdog
pip3 install psutil
pip3 install python-telegram-bot --upgrade

echo "
#####################################################
REMOVING JUNK
#####################################################

"

rm README.md
rm LICENSE

echo "
#####################################################
GENERATING CONFIG-FILES
#####################################################

"

touch api_token.txt
