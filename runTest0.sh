#!/bin/bash python3

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='envJen'
virtualenv $VIRTUAL_ENV_NAME

echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/bin/activate

#echo '#### Install requirements ####'
#pip install -r requirements.txt 

echo '#### Run Test ####'
py.test --headless --alluredir=../../allure-results test/login_scenario.py

echo '#### deactivate virtual enviroment'
deactivate