from main import *


def create_account(permission_level=1):
    return ("INSERT INTO Account(Login, Password, Permission_level, Date_of_creation, Last_time_online) VALUES (" + login() + "," + password()
            + " , " + str(permission_level) + " , " + account_created() + " , " + last_time_online() + ");")
