from main import *
from account import *


def create_patient():
    age = fake.random_int(min=1, max=115)
    return "INSERT INTO Patient(Account_id, Full_name, Address, Date_of_birth, Passport_number, Insurance_policy_number, Credit_card_number, Age) VALUES ((SELECT CURRVAL('account_account_id_seq') )," + \
           full_name() + " , " + address() + " , " + wrap(fake.date_of_birth(tzinfo=None, minimum_age=age, maximum_age=age)) + " , " + passport_number() + " , " + insurance_number() + " , " + \
           credit_number() + " , " + wrap(age) + " );"


n = int(input())

with open('/home/temurbek/DMD/dmd_assignment/population/patient.sql', 'w') as f:
    for i in range(n):
        print(create_account(5), file=f)
        print(create_patient(), file=f)
