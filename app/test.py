import psycopg2

def connect(host, database, user, password):
    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("connection done")

def query_1(id, conn):
    part1 = "SELECT Date FROM Appointment WHERE Patient_id=%s ORDER BY Date FETCH FIRST 1 ROWS ONLY" % id
    part2 = "SELECT Doctor_id FROM Appointment as A, (%s) as D WHERE A.Date=D.Date" % part1
    part3 = """SELECT Full_name FROM Doctor as D, Medical_staff as MS, Staff as S, (%s) as Dc 
            WHERE Dc.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id AND MS.Passport_number=S.Passport_number 
            AND Full_name LIKE '[ML]%%';""" % part2
    cur = conn.cursor()
    cur.execute(part3)
    rows = cur.fetchall()
    cur.close()
    return rows
    '''print("the number of names: ", cur.rowcount)
    for row in rows:
        print(row)
    '''

def query_2(conn):
    pass

def query_3(conn):
    part1 = "SELECT Patient_id FROM Appointment WHERE Date BETWEEN now()::timestamp - INTERVAL '7 days' AND now()::timestamp"
    part2 = """SELECT Patient_id FROM Appointment WHERE Date BETWEEN now()::timestamp - INTERVAL '14 days' 
            AND now()::timestamp - INTERVAL '7 days'"""
    part3 = """SELECT Patient_id FROM Appointment WHERE Date BETWEEN now()::timestamp - INTERVAL '21 days' 
            AND now()::timestamp - INTERVAL '14 days'"""
    part4 = """SELECT Patient_id FROM Appointment WHERE Date BETWEEN now()::timestamp - INTERVAL '28 days' 
            AND now()::timestamp - INTERVAL '21 days'"""
    part5 = """SELECT P.Patient_id, P.Full_name FROM Patient as P, Appointment as A WHERE EXISTS (%s) AND EXISTS (%s) 
            AND EXISTS (%s) AND EXISTS (%s) GROUP BY P.Patient_id HAVING count((%s))>=2 AND count((%s))>=2 
            AND count((%s))>=2 AND count((%s))>=2;""" % (part1, part2, part3, part4, part1, part2, part3, part4)
    cur = conn.cursor()
    cur.execute(part5)
    rows = cur.fetchall()
    cur.close()
    return rows

def query_4(conn):
    part1 = """SELECT * FROM Appointment WHERE Date >= now()::timestamp - INTERVAL '1 month'"""
    part2 = """SELECT count(*) as Num_app, LM.Patient_id, Age FROM LM, Patient as P 
            WHERE P.Patient_id=LM.Patient_id GROUP BY LM.Patient_id, Age"""
    part3 = """WITH LM as (%s), T as (%s) SELECT sum (CASE
                            WHEN T.Age<50 AND T.Num_app<3 THEN 200
                            WHEN T.Age<50 AND T.Num_app>=3 THEN 250
                            WHEN T.Age>=50 AND T.Num_app<3 THEN 400
                            WHEN T.Age>=50 AND T.Num_app>=3 THEN 500
            END) FROM T""" % (part1, part2)
    #part4 = """WITH LM as (%s), T as (%s)
     #       SELECT sum(Price) as Income;""" % (part1, part2)
    cur = conn.cursor()
    cur.execute(part3)
    rows = cur.fetchall()
    cur.close()
    return rows

def query_5(conn):
    part1 = "SELECT * FROM Appointment WHERE Date>=now()::timestamp-INTERVAL '10 years'"
    part2 = """SELECT TY.Doctor_id, Full_name, count(DISTINCT TY.Patient_id) as Number FROM TY, Doctor as D, 
            Medical_staff as MS, Staff as S WHERE TY.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id 
            AND MS.passport_number=S.passport_number GROUP BY TY.Doctor_id, Full_name"""
    part3 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date>=now()::timestamp-INTERVAL '1 year' 
            GROUP BY Doctor_id"""
    part4 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '1 year' 
            AND Date>=now()::timestamp-INTERVAL '2 years' GROUP BY Doctor_id"""
    part5 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '2 year' 
            AND Date>=now()::timestamp-INTERVAL '3 years' GROUP BY Doctor_id"""
    part6 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '3 year' 
            AND Date>=now()::timestamp-INTERVAL '4 years' GROUP BY Doctor_id"""
    part7 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '4 year' 
            AND Date>=now()::timestamp-INTERVAL '5 years' GROUP BY Doctor_id"""
    part8 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '5 year' 
            AND Date>=now()::timestamp-INTERVAL '6 years' GROUP BY Doctor_id"""
    part9 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '6 year' 
            AND Date>=now()::timestamp-INTERVAL '7 years' GROUP BY Doctor_id"""
    part10 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '7 year' 
            AND Date>=now()::timestamp-INTERVAL '8 years' GROUP BY Doctor_id"""
    part11 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '8 year' 
            AND Date>=now()::timestamp-INTERVAL '9 years' GROUP BY Doctor_id"""
    part12 = """SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '9 year' 
            AND Date>=now()::timestamp-INTERVAL '10 years' GROUP BY Doctor_id"""
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
    cur = conn.cursor()
    cur.execute(part13)
    rows = cur.fetchall()
    cur.close()
    return rows


if __name__=='__main__':
    connection = connect("localhost", "hospital_test", "postgres", "90trks125")
    query_5(connection)
