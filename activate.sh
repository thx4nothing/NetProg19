#!/bin/bash
if [ ! -d ".env" ] 
then
    virtualenv .env --python=python3
fi
source .env/bin/activate
pip3 install -r requirements.txt
