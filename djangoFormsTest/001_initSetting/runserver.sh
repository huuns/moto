#!/bin/bash

# variables setting
projectName="formstest"   # ---> lower case 
addAppName="formstestapp" 
CHOST="192.168.0.20"     # ---> django development runserver ip address
CPORT="8000"              # ---> django development runserver port number

python /var/www/html/$projectName/manage.py makemigrations $addAppName
python /var/www/html/$projectName/manage.py migrate
python /var/www/html/$projectName/manage.py runserver $CHOST:$CPORT

