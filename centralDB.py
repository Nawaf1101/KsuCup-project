import sqlite3
import  hashlib

connection = sqlite3.connect("CentralDataBase.db")
connection.execute('''CREATE TABLE Reg
 (StudentID TEXT,
 EventNumber TEXT,
 EventName TEXT NOT NULL,
 EventLocation TEXT NOT NULL,
 EventDate DATETIME NOT NULL,
 PRIMARY KEY(StudentID,EventNUmber));''')

connection.execute('''Create Table Users
(FirstName TEXT NOT NULL,
 LastName TEXT NOT NULL,
 StudentID TEXT PRIMARY KEY,
 Password TEXT NOT NULL,
 Email TEXT NOT NULL,
 Phone TEXT NOT NULL)''')

connection.execute('''Create table Events
(EventNumber TEXT PRIMARY KEY,
 EventName TEXT NOT NULL,
 EventLocation TEXT NOT NULL,
 EventCapacity INT NOT NULL,
 EventDate DATETIME NOT NULL,
 EventAttendance INT NOT NULL)''')
tmp = "Admin123"
passs = hashlib.sha256(tmp.encode()).hexdigest()
eml = "Admin@ksu.edu.sa"
connection.execute( """INSERT INTO Users(FirstName, LastName, StudentID,Password,Email,Phone) VALUES (?,?,?,?,?,?);""",("Admin", "Admin", "0123456789", passs,eml, "0551822304"))
connection.commit()
connection.close()
