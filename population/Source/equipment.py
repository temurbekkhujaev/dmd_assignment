#!/usr/bin/env python

from main import *
import sys

# n = int(input())
n = int(sys.argv[1])

with open('hospital_postgresql.sql', 'a+') as f:
    equipment_id = 0

    for i in range(n):
        equipment_id += 1

        if chance(70):
            print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
            # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
            print("INSERT INTO Medical_equipment(Equipment_id) VALUES (" + str(equipment_id) + ") ;", file=f)
        else:
            print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + non_medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
            # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
            print("INSERT INTO Nonmedical_equipment(Equipment_id) VALUES (" + str(equipment_id) + ");", file=f)

with open('hospital_postgresql.sql', 'r') as r:
    with open('hospital_mysql', 'w') as w:

        with open('../dmd_create_mysql.sql', 'r') as dmd_create:

            for line in dmd_create:
                w.write(line)

        flag = False
        for line in r:
            if "INSERT" in line: flag = True
            if flag:
                w.write(line)
