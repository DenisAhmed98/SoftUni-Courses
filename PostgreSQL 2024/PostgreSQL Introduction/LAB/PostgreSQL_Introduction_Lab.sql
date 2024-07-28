-- Task 01

CREATE TABLE employees
(
	id serial PRIMARY KEY NOT NULL,
	first_name VARCHAR(30),
	last_name VARCHAR(50),
	hiring_date DATE DEFAULT '2023-01-01',
	salary numeric(10,2),
	devices_number integer
);

CREATE TABLE departments
(
	id serial PRIMARY KEY NOT NULL,
	name VARCHAR(50),
	code CHAR(3),
	description text 
);

CREATE TABLE issues
(
	id serial PRIMARY KEY UNIQUE,
	description VARCHAR(150),
	date DATE,
	start TIMESTAMPTZ
);

-- Task 03

ALTER TABLE employees
ADD COLUMN middle_name VARCHAR(50)

-- Task 04

ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0,
ALTER COLUMN hiring_date SET NOT NULL

-- Task 05

ALTER TABLE employees
ALTER COLUMN middle_name TYPE VARCHAR(100)

-- Task 06

TRUNCATE TABLE issues

-- Task 07

DROP TABLE departments