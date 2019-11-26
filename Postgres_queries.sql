CREATE VIEW Forgotten AS WITH Dc as (SELECT DISTINCT Doctor_id
            FROM Appointment as A, (SELECT Date
									FROM Appointment
									WHERE Patient_id = 136 ORDER BY Date DESC FETCH FIRST 1 ROWS ONLY) as D
            WHERE A.Date=D.Date)
			SELECT Full_name 
            FROM Doctor as D, Medical_staff as MS, Staff as S, Dc 
            WHERE Dc.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id AND MS.Passport_number=S.Passport_number 
            AND (Full_name LIKE 'M%%' OR Full_name LIKE 'L%%');

CREATE VIEW Appointments_per_doctor AS WITH LY as (SELECT * FROM Appointment WHERE Date>=now()::timestamp - INTERVAL '1 year'),
	 AA as (SELECT (SELECT to_char(LY.Date, 'Day')) as Day, (SELECT EXTRACT (hour FROM LY.Date)) as Time, Doctor_id, Count(*) as Total FROM LY GROUP BY Day, Time, Doctor_id),
	 AAA as (SELECT AA.Day, AA.Time, AA.Doctor_id, AA.Total, (AA.Total*1.0/360) as Average FROM AA)
				SELECT Full_name, AAA.Day, AAA.Time, AAA.Total, Average FROM AAA, Doctor as D, Medical_Staff as MS, 
				Staff as S WHERE AAA.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id AND MS.Passport_number=S.Passport_number 
				ORDER BY Full_name, AAA.Day, AAA.Time;

CREATE VIEW Home_visits AS WITH W1 as (SELECT COUNT(*), Patient_id
            FROM Appointment 
            WHERE Date BETWEEN now()::timestamp - INTERVAL '7 days' AND now()::timestamp GROUP BY Patient_id),
	 W2 as (SELECT COUNT(Patient_id), Patient_id 
            FROM Appointment 
            WHERE Date BETWEEN now()::timestamp - INTERVAL '14 days' AND now()::timestamp - INTERVAL '7 days' 
            GROUP BY Patient_id),
	 W3 as (SELECT COUNT(Patient_id), Patient_id 
            FROM Appointment 
            WHERE Date BETWEEN now()::timestamp - INTERVAL '21 days' AND now()::timestamp - INTERVAL '14 days' 
            GROUP BY Patient_id),
	 W4 as (SELECT COUNT(Patient_id), Patient_id 
            FROM Appointment 
            WHERE Date BETWEEN now()::timestamp - INTERVAL '28 days' AND now()::timestamp - INTERVAL '21 days' 
            GROUP BY Patient_id)
            	SELECT W1.Patient_id, P.Full_name
            	FROM W1, W2, W3, W4, Patient as P
            	WHERE W1.Patient_id=W2.Patient_id AND W1.Patient_id=W3.Patient_id AND W1.Patient_id=W4.Patient_id
            	AND W1.Patient_id=P.Patient_id AND W1.count>=2 AND W2.count>=2 AND W3.count>=2 AND W4.count>=2
            	GROUP BY W1.Patient_id, P.Full_name;

CREATE VIEW Income AS WITH LM as (SELECT * FROM Appointment WHERE Date >= now()::timestamp - INTERVAL '1 month'),
 	  T as (SELECT count(*) as Num_app, LM.Patient_id, Age FROM LM, Patient as P 
      	WHERE P.Patient_id=LM.Patient_id GROUP BY LM.Patient_id, Age)
            SELECT sum (CASE
                            WHEN T.Age<50 AND T.Num_app<3 THEN 200
                            WHEN T.Age<50 AND T.Num_app>=3 THEN 250
                            WHEN T.Age>=50 AND T.Num_app<3 THEN 400
                            WHEN T.Age>=50 AND T.Num_app>=3 THEN 500
            END) as Income FROM T;

CREATE VIEW Doctors_for_reward AS WITH TY as (SELECT * FROM Appointment WHERE Date>=now()::timestamp-INTERVAL '10 years'),
	 TT as (SELECT TY.Doctor_id, Full_name, count(DISTINCT TY.Patient_id) as Number FROM TY, Doctor as D, 
            Medical_staff as MS, Staff as S WHERE TY.Doctor_id=D.Doctor_id AND D.MS_id=MS.MS_id 
            AND MS.passport_number=S.passport_number GROUP BY TY.Doctor_id, Full_name)
            	SELECT TT.Doctor_id, TT.Full_name FROM TT WHERE TT.Number>=100 AND 
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date>=now()::timestamp-INTERVAL '1 year' 
            			GROUP BY Doctor_id) as S1 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '1 year' 
            			AND Date>=now()::timestamp-INTERVAL '2 years' GROUP BY Doctor_id) as S2 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '2 year' 
            			AND Date>=now()::timestamp-INTERVAL '3 years' GROUP BY Doctor_id) as S3 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '3 year' 
            			AND Date>=now()::timestamp-INTERVAL '4 years' GROUP BY Doctor_id) as S4 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '4 year' 
            			AND Date>=now()::timestamp-INTERVAL '5 years' GROUP BY Doctor_id) as S5 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '5 year' 
            			AND Date>=now()::timestamp-INTERVAL '6 years' GROUP BY Doctor_id) as S6 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '6 year' 
            			AND Date>=now()::timestamp-INTERVAL '7 years' GROUP BY Doctor_id) as S7 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '7 year' 
            			AND Date>=now()::timestamp-INTERVAL '8 years' GROUP BY Doctor_id) as S8 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '8 year' 
            			AND Date>=now()::timestamp-INTERVAL '9 years' GROUP BY Doctor_id) as S9 WHERE n>=5) AND
	            EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()::timestamp-INTERVAL '9 year' 
            			AND Date>=now()::timestamp-INTERVAL '10 years' GROUP BY Doctor_id) as S10 WHERE n>=5);