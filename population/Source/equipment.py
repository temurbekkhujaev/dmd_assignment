#!/usr/bin/env python

from main import *
import sys

# n = int(input())
n = int(sys.argv[1])

with open('hospital.sql', 'a+') as f:
    equipment_id = 1

    for i in range(n):
        equipment_id += 1

        if chance(70):
            print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
            # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
            print("INSERT INTO Medical_equipment(Equipment_id) VALUES (" + equipment_id + ") ;", file=f)
        else:
            print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + non_medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
            # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
            print("INSERT INTO Nonmedical_equipment(Equipment_id) VALUES (" + equipment_id + ");", file=f)

with open('hospital_mysql.sql', 'a+') as f:
    equipment_id = 1

    for i in range(n):
        equipment_id += 1

        if chance(70):
            print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
            # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
            print("INSERT INTO Medical_equipment(Equipment_id) VALUES (" + equipment_id + ") ;", file=f)
        else:
            print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + non_medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
            # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
            print("INSERT INTO Nonmedical_equipment(Equipment_id) VALUES (" + equipment_id + ");", file=f)
