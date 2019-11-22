from main import *
from account import *

passport_number_global = 0


def create_staff(position):
    global passport_number_global
    passport_number_global = passport_number()
    return "INSERT INTO Staff(Passport_number, Account_id, Full_name, Position) VALUES (" + str(passport_number_global) + \
           " , (SELECT CURRVAL('account_account_id_seq') )," + full_name() + " , " + position + " );"


def create_medical_staff():

    return "INSERT INTO Medical_staff(Passport_number) VALUES (" + str(passport_number_global) + ");"


def create_doctor():
    return "INSERT INTO Doctors(MS_id, Specialization) VALUES ((SELECT CURRVAL('medical_staff_ms_id_seq')), " + medical_specialization() + " );"


n = int(input())

with open('/home/temurbek/DMD/dmd_assignment/population/staff.sql', 'w') as f:
    for i in range(n):
        print(create_account(3), file = f)
        print(create_staff("'Doctor'"), file = f)
        print(create_medical_staff(), file = f)
        print(create_doctor(), file = f)
