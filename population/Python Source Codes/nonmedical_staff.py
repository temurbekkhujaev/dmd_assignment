from main import *

n = int(input())

with open('/home/temurbek/DMD/dmd_assignment/population/nonmedical_staff.sql', 'w') as f:
    for i in range(n):
        print("INSERT INTO Equipment(Name, Quantity) VALUES (", "'" + medical_equipment() + "', ", fake.random_digit_not_null(), ");", file=f)
        # print("SELECT CURRVAL('Equipment_equipment_id_seq') ;", file=f)
        print("INSERT INTO Medical_equipment(Equipment_id) VALUES (SELECT CURRVAL('Equipment_equipment_id_seq') ) ;", file=f)
