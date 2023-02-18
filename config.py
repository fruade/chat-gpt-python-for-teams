#!/usr/bin/env python3

from os import environ

class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = environ.get("MICROSOFTAPPID")
    APP_PASSWORD = environ.get("MICROSOFTAPPPASSWORD")
    
