#!/usr/bin/env python

from main import *

account_id = 1


def create_account(permission_level=1):
    global account_id
    account_id += 1
    return ("INSERT INTO Account(Login, Password, Permission_level, Date_of_creation, Last_time_online) VALUES (" + login() + "," + password()
            + " , " + str(permission_level) + " , " + account_created() + " , " + last_time_online() + ");")
