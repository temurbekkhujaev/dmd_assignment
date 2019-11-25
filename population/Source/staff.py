#!/usr/bin/env python

import random
import sys
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


n = int(sys.argv[1])

with open('hospital.sql', 'w') as f:
    print('''CREATE TABLE Account (
	Account_id SERIAL PRIMARY KEY,
	Login VARCHAR(30) NOT NULL,
	Password VARCHAR(30) NOT NULL,
	Permission_level INTEGER NOT NULL,
	Date_of_creation DATE NOT NULL,
	Last_time_online TIMESTAMP NOT NULL
);

CREATE TABLE Staff (
	Passport_number INTEGER PRIMARY KEY,
	Account_id INTEGER UNIQUE NOT NULL,
	Full_name VARCHAR(50) NOT NULL,
	Position VARCHAR(50) NOT NULL,
	FOREIGN KEY (Account_id) REFERENCES Account(Account_id)
);

CREATE TABLE Medical_staff (
	MS_id SERIAL PRIMARY KEY,
	Passport_number INTEGER,
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Nonmedical_staff (
	NMS_id SERIAL PRIMARY KEY,
	Passport_number INTEGER,
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Doctor (
	Doctor_id SERIAL PRIMARY KEY,
	MS_id INTEGER NOT NULL,
	Specialization VARCHAR(50) NOT NULL,
	FOREIGN KEY (MS_id) REFERENCES Medical_staff(MS_id)
);

CREATE TABLE Patient (
	Patient_id SERIAL PRIMARY KEY,
	Account_id INTEGER,
	Full_name VARCHAR(50) NOT NULL,
	Address VARCHAR(200) NOT NULL,
	Date_of_birth DATE NOT NULL,
	Passport_number INTEGER UNIQUE NOT NULL,
	Insurance_policy_number VARCHAR(50) UNIQUE NOT NULL,
	Credit_card_number VARCHAR(16) UNIQUE NOT NULL,
	Age INTEGER NOT NULL,
	FOREIGN KEY (Account_id) REFERENCES Account(Account_id)
);

CREATE TABLE Schedule (
	Doctor_id INTEGER,
	Day VARCHAR(3),
	Time TIME NOT NULL,
	FOREIGN KEY (Doctor_id) REFERENCES Doctor(Doctor_id)
);

CREATE TABLE Appointment (
	Appointment_id SERIAL PRIMARY KEY,
	Doctor_id INTEGER NOT NULL,
	Patient_id INTEGER NOT NULL,
	Room INTEGER NOT NULL,
	Date TIMESTAMP NOT NULL,
	Price INTEGER,
	FOREIGN KEY (Doctor_id) REFERENCES Doctor(Doctor_id),
	FOREIGN KEY (Patient_id) REFERENCES Patient(Patient_id)
);

CREATE TABLE Medical_record (
	Record_id SERIAL PRIMARY KEY,
	Patient_id INTEGER NOT NULL,
	Creation_date DATE NOT NULL,
	Diagnosis VARCHAR(1000),
	Prescription VARCHAR(1000),
	FOREIGN KEY (Patient_id) REFERENCES Patient(Patient_id)
);

CREATE TABLE Notification (
	Notification_id SERIAL NOT NULL,
	Patient_id INTEGER NOT NULL,
	Date DATE NOT NULL,
	Event VARCHAR(100) NOT NULL,
	Sound INTEGER,
	FOREIGN KEY (Patient_id) REFERENCES Patient(Patient_id)
);

CREATE TABLE Payment (
	Invoice_number SERIAL PRIMARY KEY,
	Patient_id INTEGER NOT NULL,
	Date DATE NOT NULL,
	Description VARCHAR(300),
	Amount INTEGER NOT NULL,
	FOREIGN KEY (Patient_id) REFERENCES Patient(Patient_id)
);

CREATE TABLE Video_record (
	Video_id SERIAL PRIMARY KEY,
	Date DATE NOT NULL,
	Path VARCHAR(100) NOT NULL,
	Camera_number INTEGER NOT NULL
);

CREATE TABLE Email (
	Passport_number INTEGER,
	Email VARCHAR(50),
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Message (
	Message_id SERIAL PRIMARY KEY,
	Passport_number INTEGER,
	Time_sent TIMESTAMP NOT NULL,
	Text VARCHAR(1000) NOT NULL,
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Receiver (
	Message_id INTEGER,
	Receiver_id INTEGER,
	FOREIGN KEY (Message_id) REFERENCES Message(Message_id),
	FOREIGN KEY (Receiver_id) REFERENCES Staff(Passport_number)
);

CREATE TABLE Equipment (
	Equipment_id SERIAL PRIMARY KEY,
	Name VARCHAR(50) NOT NULL,
	Quantity INTEGER NOT NULL
);

CREATE TABLE Medical_equipment (
	ME_id SERIAL PRIMARY KEY,
	Equipment_id INTEGER,
	FOREIGN KEY (Equipment_id) REFERENCES Equipment(Equipment_id)
);

CREATE TABLE Nonmedical_equipment (
	NME_id SERIAL PRIMARY KEY,
	Equipment_id INTEGER,
	FOREIGN KEY (Equipment_id) REFERENCES Equipment(Equipment_id)
);
''', file=f)

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
