INSERT INTO Equipment(Name, Quantity) VALUES ( 'Bed',  6 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Nonmedical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Table',  5 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Nonmedical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Nebulizer',  7 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Medical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Bed',  5 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Nonmedical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Lab Refrigerator',  6 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Medical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Table lamp',  9 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Nonmedical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Infusion Pump',  1 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Medical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Lab Refrigerator',  4 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Medical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Bed',  3 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Nonmedical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
INSERT INTO Equipment(Name, Quantity) VALUES ( 'Fetal Monitor',  4 );
SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')
INSERT INTO Medical_equipment(Equipment_id) VALUES ( (SELECT CURRVAL(pg_get_serial_sequence('Equipment', 'Equipment_id')) );
