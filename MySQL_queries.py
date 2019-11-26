import mysql.connector as mysql
from mysql.connector import MySQLConnection, Error


def connect(host, database, user, password):
    try:
        mydb = mysql.connect(host="localhost", database="hospital", user="root", passwd="")
        return mydb
    except (Exception, mysql.DatabaseError) as err:
        print(err)
    finally:
        print("Connection successful")


def query_1(p_id, connection):
    part1 = "SELECT Date FROM Appointment WHERE Patient_id = %s ORDER BY Date DESC LIMIT 1" % p_id
    part2 = "SELECT DISTINCT Doctor_id FROM Appointment as A, (%s) as DD WHERE A.Date=DD.Date" % part1
    part3 = """WITH Dc as (%s) SELECT Full_name FROM Doctor as D, Medical_staff as MS, Staff as S, Dc 
                WHERE Dc.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id AND MS.Passport_number=S.Passport_number 
                AND (Full_name LIKE '[ML]%%');""" % part2

    mycursor = connection.cursor()
    mycursor.execute(part3)
    rows = mycursor.fetchall()
    mycursor.close()
    return rows


def query_2(connection):
    part1 = "SELECT * FROM Appointment WHERE Date>=now() - INTERVAL 1 year"
    part2 = """SELECT DAYNAME(LY.Date)"""
    part3 = "SELECT HOUR(LY.Date)"
    part4 = """SELECT (%s) as Day, (%s) as Time, Doctor_id, Count(*) as Total FROM LY GROUP BY Day, Time, Doctor_id""" % (part2, part3)
    part5 = """SELECT AA.Day, AA.Time, AA.Doctor_id, AA.Total, (AA.Total*1.0/360) as Average FROM AA"""
    part6 = """WITH LY as (%s), AA as (%s), AAA as (%s)
            SELECT Full_name, AAA.Day, AAA.Time, AAA.Total, Average FROM AAA, Doctor as D, Medical_staff as MS, 
            Staff as S WHERE AAA.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id AND MS.Passport_number=S.Passport_number;""" % (part1, part4, part5)

    mycursor = connection.cursor()
    mycursor.execute(part6)
    rows = mycursor.fetchall()
    mycursor.close()
    return rows


def query_3(connection):
    part5 = """SELECT COUNT(*), Patient_id 
                FROM Appointment 
                WHERE Date BETWEEN now() - INTERVAL 7 day AND now() GROUP BY Patient_id"""
    part6 = """SELECT COUNT(Patient_id), Patient_id 
                FROM Appointment 
                WHERE Date BETWEEN now() - INTERVAL 14 day AND now() - INTERVAL 7 days 
                GROUP BY Patient_id"""
    part7 = """SELECT COUNT(Patient_id), Patient_id 
                FROM Appointment 
                WHERE Date BETWEEN now() - INTERVAL 21 day AND now() - INTERVAL 14 day 
                GROUP BY Patient_id"""
    part8 = """SELECT COUNT(Patient_id), Patient_id 
                FROM Appointment 
                WHERE Date BETWEEN now() - INTERVAL 28 day AND now() - INTERVAL 21 day 
                GROUP BY Patient_id"""
    part9 = """WITH W1 as (%s), W2 as (%s), W3 as (%s), W4 as (%s)
                SELECT W1.Patient_id, P.Full_name
                FROM W1, W2, W3, W4, Patient as P
                WHERE W1.Patient_id=W2.Patient_id AND W1.Patient_id=W3.Patient_id AND W1.Patient_id=W4.Patient_id
                AND W1.Patient_id=P.Patient_id AND W1.count>=2 AND W2.count>=2 AND W3.count>=2 AND W4.count>=2
                GROUP BY W1.Patient_id, P.Full_name;""" % (part5, part6, part7, part8)

    mycursor = connection.cursor()
    mycursor.execute(part9)
    rows = mycursor.fetchall()
    mycursor.close()
    return rows


def query_4(connection):
    part1 = """SELECT * FROM Appointment WHERE Date >= now() - INTERVAL 1 month"""
    part2 = """SELECT count(*) as Num_app, LM.Patient_id, Age FROM LM, Patient as P 
                WHERE P.Patient_id=LM.Patient_id GROUP BY LM.Patient_id, Age"""
    part3 = """SELECT (CASE
                            WHEN T.Age<50 AND T.Num_app<3 THEN 200
                            WHEN T.Age<50 AND T.Num_app>=3 THEN 250
                            WHEN T.Age>=50 AND T.Num_app<3 THEN 400
                            WHEN T.Age>=50 AND T.Num_app>=3 THEN 500
            END) as Price FROM T"""
    part4 = """WITH LM as (%s), T as (%s), Price as (%s) SELECT sum (Price) as Income FROM (Price)""" % (part1, part2, part3)

    # part5 = """WITH LM as (%s), T as (%s) SELECT sum(Price) as Income;""" % (part1, part2)

    mycursor = connection.cursor()
    mycursor.execute(part4)
    rows = mycursor.fetchall()
    mycursor.close()
    return rows


def query_5(connection):
    part1 = "SELECT * FROM Appointment WHERE Date>=now()-INTERVAL 10 year"
    part2 = """SELECT TY.Doctor_id, Full_name, count(DISTINCT TY.Patient_id) as Number FROM TY, Doctor as D, 
            Medical_staff as MS, Staff as S WHERE TY.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id 
            AND MS.passport_number=S.passport_number GROUP BY TY.Doctor_id, Full_name"""
    part3 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date>=now()-INTERVAL 1 year 
            GROUP BY Doctor_id"""
    part4 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 1 year 
            AND Date>=now()-INTERVAL 2 year GROUP BY Doctor_id"""
    part5 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 2 year 
            AND Date>=now()-INTERVAL 3 year GROUP BY Doctor_id"""
    part6 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 3 year 
            AND Date>=now()-INTERVAL 4 year GROUP BY Doctor_id"""
    part7 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 4 year 
            AND Date>=now()-INTERVAL 5 year GROUP BY Doctor_id"""
    part8 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 5 year 
            AND Date>=now()-INTERVAL 6 year GROUP BY Doctor_id"""
    part9 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 6 year 
            AND Date>=now()-INTERVAL 7 year GROUP BY Doctor_id"""
    part10 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 7 year 
            AND Date>=now()-INTERVAL 8 year GROUP BY Doctor_id"""
    part11 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 8 year 
            AND Date>=now()-INTERVAL 9 year GROUP BY Doctor_id"""
    part12 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 9 year 
            AND Date>=now()-INTERVAL 10 year GROUP BY Doctor_id"""
    part13 = """WITH TY as (%s), TT as (%s)
            SELECT TT.Doctor_id, TT.Full_name FROM TT WHERE TT.Number>=100 AND 
            EXISTS (SELECT * FROM (%s) as S1 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S2 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S3 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S4 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S5 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S6 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S7 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S8 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S9 WHERE n>=5) AND
            EXISTS (SELECT * FROM (%s) as S10 WHERE n>=5);""" % (part1, part2, part3, part4, part5, part6, part7, part8, part9, part10, part11, part12)

    mycursor = connection.cursor()
    mycursor.execute(part13)
    rows = mycursor.fetchall()
    mycursor.close()
    return rows
