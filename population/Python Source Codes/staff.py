from main import *

passport_number_global


def create_staff(position):
    global passport_number_global
    passport_number_global = passport_number();
    return "INSERT INTO Staff(Passport_number, Account_id, Full_name, Position) VALUES (" + str(passport_number_global) + \
           " , (SELECT CURRVAL('account_account_id_seq') )," + full_name() + " , " + position + " );"


def create_medical_staff():
    return "INSERT INTO Medical_staff(Passport_number) VALUES (" + str(passport_number_global) + ");"


def create_doctor():
    return "INSERT INTO Doctors(MS_id, Account_id, Full_name, Position) VALUES (SELECT CURRVAL('account_account_id_seq') ," + full_name() + " , " + position + " );"
