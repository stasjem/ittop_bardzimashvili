--7.09 сентября
--1 Создать БД со связью таблиц "1 к 1".-
--2. Создать БД со связью таблиц "1 к многим".
--3. Создать БД со связью таблиц "многим к многим".
--4. Создать и заполнить данными таблицы.



--1
--CREATE DATABASE OneToOneDB;
--USE OneToOneDB;
-- CREATE TABLE Person (
--    id INT PRIMARY KEY AUTO_INCREMENT,
--    name VARCHAR(50) NOT NULL
-- );


-- CREATE TABLE Passport (
--    id INT PRIMARY KEY AUTO_INCREMENT,
--    person_id INT UNIQUE,
--    passport_number VARCHAR(20) NOT NULL,
--    FOREIGN KEY (person_id) REFERENCES Person(id)
-- );


-- INSERT INTO Person (name) VALUES ('John Doe'), ('Jane Smith');


-- INSERT INTO Passport (person_id, passport_number) VALUES (1, 'AB1234567'), (2, 'CD9876543');

--2

-- CREATE DATABASE OneToManyDB;
-- USE OneToManyDB;


-- CREATE TABLE Author (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(50) NOT NULL
-- );


-- CREATE TABLE Book (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     author_id INT,
--     title VARCHAR(100) NOT NULL,
--     FOREIGN KEY (author_id) REFERENCES Author(id)
-- );


-- INSERT INTO Author (name) VALUES ('George Orwell'), ('J.K. Rowling');


-- INSERT INTO Book (author_id, title) VALUES (1, '1984'), (1, 'Animal Farm'), (2, 'Harry Potter and the Sorcerer\'s Stone');

--3

-- CREATE DATABASE ManyToManyDB;
-- USE ManyToManyDB;

-- CREATE TABLE Student (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(50) NOT NULL
-- );


-- CREATE TABLE Course (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     course_name VARCHAR(100) NOT NULL
-- );


-- CREATE TABLE Enrollment (
--     student_id INT,
--     course_id INT,
--     FOREIGN KEY (student_id) REFERENCES Student(id),
--     FOREIGN KEY (course_id) REFERENCES Course(id),
--     PRIMARY KEY (student_id, course_id)
-- );


-- INSERT INTO Student (name) VALUES ('Alice'), ('Bob'), ('Charlie');


-- INSERT INTO Course (course_name) VALUES ('Mathematics'), ('History'), ('Computer Science');

-- INSERT INTO Enrollment (student_id, course_id) VALUES (1, 1), (1, 2), (2, 3), (3, 1), (3, 3);
