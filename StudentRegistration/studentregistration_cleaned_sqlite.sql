
-- Cleaned SQLite-Compatible SQL Schema and Data

-- Drop tables if they already exist
DROP TABLE IF EXISTS StudentNotifications;
DROP TABLE IF EXISTS StudentBalances;
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Session;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Department;

-- Department Table
CREATE TABLE Department (
    DepartmentID INTEGER PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL
);

INSERT INTO Department (DepartmentID, Department_Name) VALUES 
(675, 'Information Systems'),
(564, 'Marketing'),
(786, 'Management'),
(453, 'Accounting');

-- Course Table
CREATE TABLE Course (
    CourseID INTEGER PRIMARY KEY,
    Course_Name VARCHAR(150) NOT NULL,
    Credits INTEGER NOT NULL,
    DepartmentID INTEGER,
    Class_Time VARCHAR(50),
    Days VARCHAR(20),
    is_synchronous BOOLEAN
);

INSERT INTO Course (CourseID, Course_Name, Credits, DepartmentID, Class_Time, Days, is_synchronous) VALUES 
(45235, 'INFO 465', 3, 675, '9:00 AM - 9:50 AM', 'M/W/F', 1),
(45288, 'INFO 450', 3, 675, '10:00 AM -12:40 PM', 'THUR', 1),
(35513, 'INFO 364', 3, 675, '11:00 AM - 11:50 AM', 'M/W/F', 1),
(63354, 'MKTG 310', 3, 564, '12:00 PM - 12:50 PM', 'M/W/F', 1),
(63875, 'MKTG 320', 3, 564, '1:00 PM - 2:15 PM', 'TUES/THURS', 1),
(53864, 'MKTG 264', 2, 564, '2:00 PM - 3:15 PM', 'M/W', 1),
(12542, 'MGMT 101', 1, 786, '9:00 AM - 11:40 AM', 'F', 1),
(22985, 'MGMT 205', 2, 786, '10:00 AM - 11:15 AM', 'THURS', 1),
(22364, 'MGMT 210', 2, 786, '11:00 AM - 11:50 AM', 'M/W/F', 1),
(71664, 'ACCT 250', 2, 453, '1:00 PM - 2:15 PM', 'TUES/THUR', 1),
(81687, 'ACCT 364', 3, 453, '3:00 PM - 4:15 AM', 'THURS', 1),
(91234, 'ACCT 406', 2, 453, '3:00 PM - 3:50 PM', 'M/W/F', 1);

-- Student Table
CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    S_First_Name VARCHAR(45) NOT NULL,
    S_Last_Name VARCHAR(45) NOT NULL,
    S_Email VARCHAR(255) NOT NULL,
    Year INTEGER NOT NULL,
    Major VARCHAR(255) NOT NULL,
    Class1 VARCHAR(100) NOT NULL,
    Class2 VARCHAR(100) NOT NULL,
    Class3 VARCHAR(100) NOT NULL,
    Password_Hash VARCHAR(255)
);

INSERT INTO Student (StudentID, S_First_Name, S_Last_Name, S_Email, Year, Major, Class1, Class2, Class3) VALUES
(1561, 'Peter', 'Smith', 'smith07@vcu.edu', 3, 'Finance', 'Business Law', 'Macroeconomics', 'Intro to Finance'),
(1374, 'David', 'Burns', 'burns01@vcu.edu', 2, 'Marketing', 'International Marketing', 'Microeconomics', 'Marketing Principles'),
(1648, 'Lily', 'Davidson', 'davidson05@vcu.edu', 1, 'Management', 'Intro to Business', 'Microeconomics', 'Marketing Principles'),
(1945, 'Mary', 'Collins', 'collins08@vcu.edu', 3, 'Information Systems', 'Programming', 'Database Systems', 'Data Mining'),
(1821, 'Mark', 'Oliver', 'oliver03@vcu.edu', 3, 'Information Systems', 'Programming', 'Database Systems', 'Business Law'),
(1865, 'Riley', 'Waters', 'waters01@vcu.edu', 2, 'Marketing', 'Business Law', 'Marketing Principles', 'Financial Management'),
(1468, 'Kenny', 'Lin', 'lin06@vcu.edu', 4, 'Accounting', 'Programming', 'Data Mining', 'Auditing'),
(1798, 'Mai', 'Kurosawa', 'kurosawa@vcu.edu', 3, 'Accounting', 'Intro to Finance', 'Financial Management', 'Auditing'),
(1693, 'James', 'Walsh', 'walsh01@vcu.edu', 1, 'Management', 'Microeconomics', 'Marketing Principles', 'Intro to Business'),
(1267, 'Winnie', 'Gonzalez', 'gonzalez@vcu.edu', 3, 'Marketing', 'International Marketing', 'Business Law', 'Macroeconomics');

-- Instructor Table
CREATE TABLE Instructor (
    InstructorID INTEGER PRIMARY KEY,
    I_First_Name VARCHAR(100) NOT NULL,
    I_Last_Name VARCHAR(100) NOT NULL,
    DepartmentID INTEGER NOT NULL,
    CourseName VARCHAR(100) NOT NULL,
    Semester VARCHAR(20) NOT NULL,
    Password_Hash VARCHAR(255),
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

INSERT INTO Instructor (InstructorID, I_First_Name, I_Last_Name, DepartmentID, CourseName, Semester) VALUES 
(1001, 'John', 'Doe', 675, 'Database Management', 'Spring 2025'),
(1002, 'Jane', 'Smith', 564, 'Digital Management', 'Spring 2025'),
(1003, 'Alice', 'Johnson', 675, 'Web Development', 'Spring 2025'),
(1004, 'Bob', 'Brown', 786, 'Operational Management', 'Spring 2025'),
(1005, 'Charlie', 'Davis', 453, 'Accounting', 'Spring 2025');

-- Session Table
CREATE TABLE Session (
    SessionID INTEGER PRIMARY KEY,
    CourseID INTEGER NOT NULL,
    InstructorID INTEGER NOT NULL,
    Max_Students INTEGER NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
);

INSERT INTO Session (SessionID, CourseID, InstructorID, Max_Students) VALUES
(1, 45235, 1001, 30),
(2, 45288, 1001, 29),
(3, 35513, 1003, 27),
(4, 63354, 1002, 32),
(5, 63875, 1002, 20),
(6, 53864, 1002, 15),
(7, 12542, 1004, 25),
(8, 22985, 1004, 28),
(9, 22364, 1004, 40),
(10, 71664, 1005, 35),
(11, 81687, 1005, 30),
(12, 91234, 1005, 25);
