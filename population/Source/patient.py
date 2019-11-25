#!/usr/bin/env python

from main import *
import sys
from account import *


def create_patient():
    age = fake.random_int(min=1, max=115)

    if chance(50):
        name = wrap(fake.name_female())
        gender = wrap("F")
    else:
        name = wrap(fake.name_male())
        gender = wrap("M")

    return "INSERT INTO Patient(Account_id, Full_name, Address, Date_of_birth, Gender, Passport_number, Insurance_policy_number, Credit_card_number, Age) VALUES ((SELECT CURRVAL('account_account_id_seq') )," + \
           name + " , " + address() + " , " + wrap(fake.date_of_birth(tzinfo=None, minimum_age=age, maximum_age=age)) + " , " + passport_number() + " , " + gender + " , " + insurance_number() + " , " + \
           credit_number() + " , " + wrap(age) + " );"


def create_appointment():
    return "INSERT INTO Appointment(Doctor_id, Patient_id, Room, Date, Price) VALUES ( (SELECT floor(random() * ( (SELECT CURRVAL('Doctor_doctor_id_seq')) ) + 1 )) , (SELECT CURRVAL('Patient_patient_id_seq') ), " \
           + str(fake.random_int(min=1, max=999)) + " , " + account_created() + " , " + str(fake.random_int(min=0, max=999)) + " );"


def create_medical_record():
    return "INSERT INTO Medical_record(Patient_id, Creation_date, Diagnosis, Prescription) VALUES ((SELECT CURRVAL('Patient_patient_id_seq') ), " + account_created() + " , " + \
           wrap(fake.word(ext_word_list=diagnosis_list)) + " , " + wrap(fake.word(ext_word_list=prescription_list)) + " );"


def create_notification():
    return "INSERT INTO Notification(Patient_id, Date, Event, Sound) VALUES ((SELECT CURRVAL('Patient_patient_id_seq') ), " + account_created() + " , " + \
           wrap(fake.sentence().replace("\n", "")) + " , " + str(fake.random_int(min=0, max=10)) + " );"


def create_payment():
    return "INSERT INTO Payment(Patient_id, Date, Description, Amount) VALUES ((SELECT CURRVAL('Patient_patient_id_seq') ), " + account_created() + " , " + \
           wrap(fake.sentence().replace("\n", "")) + " , " + str(fake.random_int(min=1, max=9999999)) + " );"


# n = int(input())

n = int(sys.argv[1])

with open('hospital.sql', 'a+') as f:
    for i in range(n):
        print(create_account(5), file=f)
        print(create_patient(), file=f)
        for j in range(25): print(create_appointment(), file=f)
        print(create_medical_record(), file=f)
        print(create_notification(), file=f)
        print(create_notification(), file=f)
        print(create_payment(), file=f)
        print(create_payment(), file=f)
