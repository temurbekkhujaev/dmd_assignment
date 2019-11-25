--query_1--
SELECT Full_name 
FROM Doctor as D, Medical_staff as MS, Staff as S,
	(SELECT DISTINCT Doctor_id 
     FROM Appointment as A, (SELECT Date 
            				FROM Appointment 
            				WHERE Patient_id=417 ORDER BY Date DESC LIMIT 1) as D 
     WHERE A.Date=D.Date) as Dc 
WHERE Dc.Doctor_id=D.Doctor_id
AND D.MS_id=MS.MS_id
AND MS.Passport_number=S.Passport_number 
AND (Full_name LIKE '[ML]%');

--query_2--
SELECT Full_name, AAA.Day, AAA.Time, AAA.Total, Average
FROM Doctor as D, Medical_Staff as MS, Staff as S,
	(SELECT AA.Day, AA.Time, AA.Doctor_id, AA.Total, (AA.Total*1.0/360) as Average
<<<<<<< HEAD
	FROM (SELECT (SELECT DAYNAME(LY.Date)) as Day, (SELECT HOUR(LY.Date)) as Time, Doctor_id, Count(*) as Total
		 FROM (SELECT *
		 	   FROM Appointment
		 	   WHERE Date>=now() - INTERVAL 1 year) as LY
=======
	FROM (SELECT (SELECT to_char(LY.Date, 'Day')) as Day, (SELECT EXTRACT (hour FROM LY.Date)) as Time, Doctor_id, Count(*) as Total
		 FROM (SELECT *
		 	   FROM Appointment
		 	   WHERE Date>=now()::timestamp - INTERVAL '1 year') as LY
>>>>>>> 7ccece47526ea2d0ad3b8704a8778bbb6ab58e4d
		 GROUP BY Day, Time, Doctor_id) as AA) as AAA
WHERE AAA.Doctor_id=D.Doctor_id
AND D.MS_id=MS.MS_id
AND MS.Passport_number=S.Passport_number 
ORDER BY Full_name, AAA.Day, AAA.Time;

--query_3--
SELECT W1.Patient_id, P.Full_name
FROM Patient as P,
	(SELECT COUNT(*), Patient_id 
     FROM Appointment 
<<<<<<< HEAD
     WHERE Date BETWEEN now() - INTERVAL 7 day AND now()
     GROUP BY Patient_id) as W1,
	(SELECT COUNT(Patient_id), Patient_id 
     FROM Appointment 
     WHERE Date BETWEEN now() - INTERVAL 14 day AND now() - INTERVAL 7 day 
     GROUP BY Patient_id) as W2,
	(SELECT COUNT(Patient_id), Patient_id 
     FROM Appointment 
     WHERE Date BETWEEN now() - INTERVAL 21 day AND now() - INTERVAL 14 day 
     GROUP BY Patient_id) as W3,
	(SELECT COUNT(Patient_id), Patient_id 
     FROM Appointment 
     WHERE Date BETWEEN now() - INTERVAL 28 day AND now() - INTERVAL 21 day 
=======
     WHERE Date BETWEEN now()::timestamp - INTERVAL '7 days' AND now()::timestamp
     GROUP BY Patient_id) as W1,
	(SELECT COUNT(Patient_id), Patient_id 
     FROM Appointment 
     WHERE Date BETWEEN now()::timestamp - INTERVAL '14 days' AND now()::timestamp - INTERVAL '7 days' 
     GROUP BY Patient_id) as W2,
	(SELECT COUNT(Patient_id), Patient_id 
     FROM Appointment 
     WHERE Date BETWEEN now()::timestamp - INTERVAL '21 days' AND now()::timestamp - INTERVAL '14 days' 
     GROUP BY Patient_id) as W3,
	(SELECT COUNT(Patient_id), Patient_id 
     FROM Appointment 
     WHERE Date BETWEEN now()::timestamp - INTERVAL '28 days' AND now()::timestamp - INTERVAL '21 days' 
>>>>>>> 7ccece47526ea2d0ad3b8704a8778bbb6ab58e4d
     GROUP BY Patient_id) as W4
WHERE W1.Patient_id=W2.Patient_id
AND W1.Patient_id=W3.Patient_id
AND W1.Patient_id=W4.Patient_id
AND W1.Patient_id=P.Patient_id
AND W1.count>=2 AND W2.count>=2 AND W3.count>=2 AND W4.count>=2
GROUP BY W1.Patient_id, P.Full_name;

--query_4--
<<<<<<< HEAD
SELECT sum(Price) as Income
FROM (SELECT(CASE
=======
SELECT sum ((CASE
>>>>>>> 7ccece47526ea2d0ad3b8704a8778bbb6ab58e4d
            WHEN T.Age<50 AND T.Num_app<3 THEN 200
            WHEN T.Age<50 AND T.Num_app>=3 THEN 250
            WHEN T.Age>=50 AND T.Num_app<3 THEN 400
            WHEN T.Age>=50 AND T.Num_app>=3 THEN 500
<<<<<<< HEAD
            END) as Price
            FROM (SELECT count(*) as Num_app, LM.Patient_id, Age
            		   FROM Patient as P,
            		   		(SELECT *
            		   		 FROM Appointment
            		   		 WHERE Date >= now() - INTERVAL 1 month) as LM 
            WHERE P.Patient_id=LM.Patient_id
            GROUP BY LM.Patient_id, Age) as T);

--query_5--
SELECT TT.Doctor_id, TT.Full_name 
FROM (SELECT TY.Doctor_id, Full_name, count(DISTINCT TY.Patient_id) as Number
	  FROM Doctor as D, Medical_staff as MS, Staff as S,
	  	   (SELECT *
	  		FROM Appointment
	  		WHERE Date>=now()-INTERVAL 10 year) as TY
	  WHERE TY.Doctor_id=D.Doctor_id
	  AND D.MS_id=MS.MS_id 
      AND MS.passport_number=S.passport_number
      GROUP BY TY.Doctor_id, Full_name) as TT
WHERE TT.Number>=100
AND 
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date>=now()-INTERVAL 1 year 
            GROUP BY Doctor_id) as S1 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 1 year 
            AND Date>=now()-INTERVAL 2 year GROUP BY Doctor_id) as S2 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 2 year 
            AND Date>=now()-INTERVAL 3 year GROUP BY Doctor_id) as S3 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 3 year 
            AND Date>=now()-INTERVAL 4 year GROUP BY Doctor_id) as S4 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 4 year 
            AND Date>=now()-INTERVAL 5 year GROUP BY Doctor_id) as S5 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 5 year 
            AND Date>=now()-INTERVAL 6 year GROUP BY Doctor_id) as S6 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 6 year 
            AND Date>=now()-INTERVAL 7 year GROUP BY Doctor_id) as S7 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 7 year 
            AND Date>=now()-INTERVAL 8 year GROUP BY Doctor_id) as S8 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 8 year 
            AND Date>=now()-INTERVAL 9 year GROUP BY Doctor_id) as S9 WHERE n>=5) AND
    EXISTS (SELECT * FROM (SELECT TY.Doctor_id, count(*) as n FROM TY WHERE Date<now()-INTERVAL 9 year 
            AND Date>=now()-INTERVAL 10 year GROUP BY Doctor_id) as S10 WHERE n>=5);
=======
            END) FROM (SELECT count(*) as Num_app, LM.Patient_id, Age
            		   FROM Patient as P,
            		   		(SELECT *
            		   		 FROM Appointment
            		   		 WHERE Date >= now()::timestamp - INTERVAL '1 month') as LM 
            WHERE P.Patient_id=LM.Patient_id GROUP BY LM.Patient_id, Age) as T) as Income;

--query_5--
SELECT TT.Doctor_id, TT.Full_name 
FROM (SELECT TY.Doctor_id, count(*) as n
	  FROM (SELECT TY.Doctor_id, Full_name, count(DISTINCT TY.Patient_id) as Number
	  		FROM Doctor as D, Medical_staff as MS, Staff as S,
	  		(SELECT *
	  		 FROM Appointment
	  		 WHERE Date>=now()::timestamp-INTERVAL '10 years') as TY
	  		WHERE TY.Doctor_id=D.Doctor_id
	  		AND D.MS_id=MS.MS_id 
            AND MS.passport_number=S.passport_number
            GROUP BY TY.Doctor_id, Full_name) as TT
WHERE TT.Number>=100
AND 
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
>>>>>>> 7ccece47526ea2d0ad3b8704a8778bbb6ab58e4d
