#!/usr/bin/env python

import random
import sys
from main import *
from account import *
from account import account_id

passport_number_global = 0
medical_staff_id = 1
nonmedical_staff_id = 1
doctor_id = 1
message_id = 1


def create_staff(position):
    global passport_number_global
    passport_number_global = passport_number()
    return "INSERT INTO Staff(Passport_number, Account_id, Full_name, Position) VALUES (" + str(passport_number_global) + \
           " , " + str(account_id) + "," + full_name() + " , " + position + " );"


def create_medical_staff():
    global medical_staff_id
    medical_staff_id += 1
    return "INSERT INTO Medical_staff(Passport_number) VALUES (" + str(passport_number_global) + ");"


def create_nonmedical_staff():
    global nonmedical_staff_id
    nonmedical_staff_id += 1
    return "INSERT INTO Nonmedical_staff(Passport_number) VALUES (" + str(passport_number_global) + ");"


def create_doctor():
    global doctor_id
    doctor_id += 1
    return "INSERT INTO Doctor(MS_id, Specialization) VALUES (" + str(medical_staff_id) + " , " + medical_specialization() + " );"


def create_email(f):
    for i in range(fake.random_int(min=0, max=3)):
        print("INSERT INTO Email(Passport_number, Email) VALUES(" + str(passport_number_global) + " , " + wrap(fake.email()) + " );", file=f)


days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def create_schedule(f):
    working_chance = int((10 + fake.random_int(min=0, max=30)) / (7 * 24) * 100)
    for i in range(7 * 24):
        if (chance(working_chance)):
            print("INSERT INTO Schedule(Doctor_id, Day, Time) VALUES (" + str(doctor_id) + " , " + wrap(days[i // 24]) + " , '" + str(i % 24) + ":00' );", file=f)


def create_message(f):
    global message_id
    message_id += 1
    print("INSERT INTO Message(Passport_number, Time_sent, Text) VALUES (" + str(passport_number_global) + " , " + account_created() + " , " +
          wrap(fake.sentence().replace("\n", "")) + ");", file=f)
    print("INSERT INTO Receiver(Message_id, Receiver_id) VALUES (" + str(message_id) + " , " +
          str(random.sample(used_passport_numbers - {'-1'}, 1)[0]) + ");", file=f)


n = int(sys.argv[1])


with open('hospital_postgresql.sql', 'w') as f:
    with open('../dmd_create_postgre.sql', 'r') as dmd_create:

        for line in dmd_create:
            f.write(line)

    for i in range(n):
        if chance(30) or i < 30:
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
        if i > 30:
            for j in range(fake.random_int(min=0, max=5)):
                create_message(f)
