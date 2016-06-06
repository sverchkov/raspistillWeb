#!/bin/sh

export PATH=/opt/vc/bin:$PATH

cd /home/alarm/python-env
source bin/activate
cd raspistillWeb
../bin/pserve development.ini > /home/alarm/raspistillWeb.log.txt 2>&1
