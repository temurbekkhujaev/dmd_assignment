from main import *

def make_staff(position):

    if position == "Doctor" or position == "Nurse":
        return ("INSERT INTO Staff(Passport_number, Password, Permission_level, Date_of_creation, Last_time_online) VALUES (" + login() + "," + password()
                + " , " + str(permission_level) + " , " + account_created() + " , " + last_time_online() + ");")
    else:

