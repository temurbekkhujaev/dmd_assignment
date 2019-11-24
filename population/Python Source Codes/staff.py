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


def create_nonmedical_staff():
    return "INSERT INTO Nonmedical_staff(Passport_number) VALUES (" + str(passport_number_global) + ");"


def create_doctor():
    return "INSERT INTO Doctor(MS_id, Specialization) VALUES ((SELECT CURRVAL('medical_staff_ms_id_seq')), " + medical_specialization() + " );"


days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def create_schedule(f):
    working_chance = int((40 + fake.random_int(min=0, max=40)) / (7 * 24) * 100)
    for i in range(7 * 24):
        if (chance(working_chance)):
            print("INSERT INTO Schedule(Doctor_id, Day, Time) VALUES ((SELECT CURRVAL('Doctor_doctor_id_seq')), " + wrap(days[i // 24]) + " , '" + str(i % 24) + ":00' );", file=f)


n = int(input())

with open('/home/temurbek/DMD/dmd_assignment/population/staff.sql', 'w') as f:
    for i in range(n):
        if chance(30):
            print(create_account(fake.random_int(min=1, max=2)), file=f)
            print(create_staff("'Doctor'"), file=f)
            print(create_medical_staff(), file=f)
            print(create_doctor(), file=f)
            create_schedule(f)
        elif chance(60):
            print(create_account(3), file=f)
            print(create_staff("'Nurse'"), file=f)
            print(create_medical_staff(), file=f)
        else:
            print(create_account(4), file=f)
            print(create_staff(nonmedical_position()), file=f)
            print(create_nonmedical_staff(), file=f)
