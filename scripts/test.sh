#!/bin/bash

set -e

#Install dependencies
sudo apt-get update > /dev/null
sudo apt-get install python3 python3-venv libpq-dev -y > /dev/null

#Install pip requirements
python3 -m venv venv && source venv/bin/activate
for i in {1..4}; do 
pip3 install -r service_${i}/requirements.txt > /dev/null; 
done 

#Unit testing
python3 -m pytest --disable-warnings --cov --cov-config=.coveragerc --cov-report=term-missing