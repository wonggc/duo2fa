## Setup

* Install python3 and python3-pip

* (Optional) Setup virtualenv

* Install python modules with `pip3 install -r requirements.txt`

* Head to https://console.developers.google.com and create a Gmail OAuth 2.0 credential and download the client secret JSON and save to the same directory as duofa.py

## About

This script utilizes the Gmail API to retrieve your 2FA codes sent via SMS and automatically copies to the clipboard.

To prevent retrieving the same 2FA and ensure only unique 2FA is retrieved, a hashed 2FA is saved to compare against.
