CREATE TABLE Account (
	Account_id SERIAL PRIMARY KEY,
	Login VARCHAR(30) NOT NULL,
	Password VARCHAR(30) NOT NULL,
	Permission_level INTEGER NOT NULL,
	Date_of_creation DATE NOT NULL,
	Last_time_online TIMESTAMP NOT NULL
);

CREATE TABLE Patients (
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

CREATE TABLE Doctors (
	Doctor_id INTEGER PRIMARY KEY,
	Specialization VARCHAR(50) NOT NULL
);

CREATE TABLE Schedule (
	Doctor_id INTEGER,
	Day VARCHAR(3),
	Start_time TIME NOT NULL,
	End_time TIME NOT NULL,
	FOREIGN KEY (Doctor_id) REFERENCES Doctors(Doctor_id)
);

CREATE TABLE Appointments (
	Appointment_id SERIAL PRIMARY KEY,
	Doctor_id INTEGER NOT NULL,
	Patient_id INTEGER NOT NULL,
	Date DATE NOT NULL,
	Time TIME NOT NULL,
	Duration INTERVAL,
	Room INTEGER NOT NULL,
	Price INTEGER,
	FOREIGN KEY (Doctor_id) REFERENCES Doctors(Doctor_id),
	FOREIGN KEY (Patient_id) REFERENCES Patients(Patient_id)
);

CREATE TABLE Medical_records (
	Record_id SERIAL PRIMARY KEY,
	Patient_id INTEGER NOT NULL,
	Creation_date DATE NOT NULL,
	Diagnosis VARCHAR(1000),
	Prescription VARCHAR(1000),
	FOREIGN KEY (Patient_id) REFERENCES Patients(Patient_id)
);

CREATE TABLE Notifications (
	Notification_id SERIAL NOT NULL,
	Patient_id INTEGER NOT NULL,
	Date DATE NOT NULL,
	Event VARCHAR(100) NOT NULL,
	Sound INTEGER,
	FOREIGN KEY (Patient_id) REFERENCES Patients(Patient_id)
);

CREATE TABLE Payment (
	Invoice_number SERIAL PRIMARY KEY,
	Patient_id INTEGER NOT NULL,
	Date DATE NOT NULL,
	Description VARCHAR(300),
	Amount INTEGER NOT NULL,
	FOREIGN KEY (Patient_id) REFERENCES Patients(Patient_id)
);

CREATE TABLE Video_records (
	Video_id SERIAL PRIMARY KEY,
	Date DATE NOT NULL,
	Path VARCHAR(100) NOT NULL,
	Camera_number INTEGER NOT NULL
);

CREATE TABLE Staff (
	Passport_number INTEGER PRIMARY KEY,
	Account_id INTEGER UNIQUE NOT NULL,
	Full_name VARCHAR(50) NOT NULL,
	Position VARCHAR(50) NOT NULL,
	FOREIGN KEY (Account_id) REFERENCES Account(Account_id)
);

CREATE TABLE Email (
	Passport_number INTEGER,
	Email VARCHAR(50),
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Medical_staff (
	MS_id INTEGER PRIMARY KEY,
	Passport_number INTEGER,
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Nonmedical_staff (
	NMS_id INTEGER PRIMARY KEY,
	Passport_number INTEGER,
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Messages (
	Message_id SERIAL PRIMARY KEY,
	Passport_number INTEGER,
	Date_sent DATE NOT NULL,
	Time_sent TIME NOT NULL,
	Text VARCHAR(1000) NOT NULL,
	FOREIGN KEY (Passport_number) REFERENCES Staff(Passport_number)
);

CREATE TABLE Receivers (
	Message_id INTEGER,
	Receiver_id INTEGER,
	FOREIGN KEY (Message_id) REFERENCES Messages(Message_id),
	FOREIGN KEY (Receiver_id) REFERENCES Staff(Passport_number)
);

CREATE TABLE Equipment (
	Equipment_id INTEGER PRIMARY KEY,
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