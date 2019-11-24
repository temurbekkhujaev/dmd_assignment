import random

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


def create_email(f):
    for i in range(fake.random_int(min=0, max=3)):
        print("INSERT INTO Email(Passport_number, Email) VALUES(" + str(passport_number_global) + " , " + wrap(fake.email()) + " );", file=f)


days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def create_schedule(f):
    working_chance = int((10 + fake.random_int(min=0, max=50)) / (7 * 24) * 100)
    for i in range(7 * 24):
        if (chance(working_chance)):
            print("INSERT INTO Schedule(Doctor_id, Day, Time) VALUES ((SELECT CURRVAL('Doctor_doctor_id_seq')), " + wrap(days[i // 24]) + " , '" + str(i % 24) + ":00' );", file=f)


def create_message(f):
    print("INSERT INTO Message(Passport_number, Time_sent, Text) VALUES (" + str(passport_number_global) + " , " + account_created() + " , " +
          wrap(fake.sentence().replace("\n", "")) + ");", file=f)
    print("INSERT INTO Receiver(Message_id, Receiver_id) VALUES ( (SELECT CURRVAL('Message_message_id_seq')) , " +
          str(random.sample(used_passport_numbers - {'-1'}, 1)[0]) + ");", file=f)


n = int(input())

with open('/home/temurbek/DMD/dmd_assignment/population/staff.sql', 'w') as f:
    for i in range(n):
        if chance(30) or i < 4:
            print(create_account(fake.random_int(min=1, max=2)), file=f)
            print(create_staff("'Doctor'"), file=f)
            create_email(f)
            print(create_medical_staff(), file=f)
            print(create_doctor(), file=f)
            create_schedule(f)
        elif chance(60):
            print(create_account(3), file=f)
            print(create_staff("'Nurse'"), file=f)
            create_email(f)
            print(create_medical_staff(), file=f)
        else:
            print(create_account(4), file=f)
            print(create_staff(nonmedical_position()), file=f)
            create_email(f)
            print(create_nonmedical_staff(), file=f)
        if i > 4:
            for j in range(fake.random_int(min=0, max=5)):
                create_message(f)
