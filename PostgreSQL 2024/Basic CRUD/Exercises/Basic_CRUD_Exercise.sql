-- Task 01

SELECT * FROM cities
ORDER BY id;

-- Task 02

SELECT name || ' ' || state AS "cities_information", area AS "area_km2"
FROM cities;

-- Task 03

SELECT DISTINCT (name)
	name , area AS "area_km2"
FROM cities
ORDER BY name Desc;

-- Task 04

SELECT 
	id,
	first_name || ' ' || last_name AS "full_name",
	job_title
FROM employees
ORDER BY first_name ASC
LIMIT 50;

-- Task 05

SELECT 
	id,
	first_name || ' ' || middle_name || ' ' || last_name AS "full_name",
	hire_date
FROM employees
ORDER BY hire_date ASC
OFFSET 9;

-- Task 06

SELECT 
	id,
	number || ' ' || street AS "address",
	city_id
FROM addresses
WHERE id >= 20;

-- Task 07

SELECT 
	number || ' ' || street AS "address",
	city_id
FROM addresses
WHERE city_id > 0 AND (city_id % 2) = 0
ORDER BY city_id ASC;

-- Task 08

SELECT 
	name,
	start_date,
	end_date
FROM projects
WHERE start_date >= '2016-06-01 07:00:00'  AND end_date < '2023-06-04 00:00:00'
ORDER BY start_date ASC;

-- Task 09

SELECT 
	number,
	street
FROM addresses
WHERE (id BETWEEN 50 AND 100) OR (number < 1000)  

-- Task 10

SELECT
	employee_id,
	project_id
FROM employees_projects
WHERE employee_id IN (200,250)
AND project_id NOT IN (50,100);

-- Task 11

SELECT
	name,
	start_date
FROM projects
WHERE name IN ('Mountain','Road','Touring')
LIMIT 20;

-- Task 12

SELECT 
	first_name || ' ' || last_name AS "full_name",
	job_title,
	salary
FROM employees
WHERE salary IN (12500, 14000, 23600, 25000)
ORDER BY salary DESC;

-- Task 13

SELECT 
	id,
	first_name,
	last_name
FROM employees
WHERE middle_name IS NULL
LIMIT 3;

-- Task 14

INSERT INTO 
	departments (department, manager_id) 
VALUES
	('Finance', 3),
	('Information Services', 42),
	('Document Control', 90),
	('Quality Assurance', 274),
	('Facilities and Maintenance', 218),
	('Shipping and Receiving', 85),
	('Executive', 109);

-- Task 15

CREATE TABLE IF NOT EXISTS company_chart 
AS 
SELECT
	CONCAT(
		first_name,
		' ',
		last_name
	) AS full_name,
	job_title,
	department_id,
	manager_id
FROM
	employees;

-- Task 16

UPDATE 
	projects
SET 
	end_date = start_date + INTERVAL '5 months'
WHERE 
	end_date IS NULL;

-- Task 17

UPDATE 
	employees
SET 
	salary = salary + 1500,
	job_title = 'Senior ' || job_title
WHERE 
	hire_date BETWEEN '1998-01-01' AND '2000-01-05';

-- Task 18

DELETE FROM addresses
WHERE city_id IN (5, 17, 20, 30);

-- Task 19

CREATE VIEW
	view_company_chart
AS
SELECT 
	full_name,
	job_title
FROM 
	company_chart
WHERE
	manager_id = 184;

-- Task 20

CREATE VIEW
	view_addresses
AS
SELECT
	CONCAT(
		e.first_name,
		' ',
		e.last_name
	) AS full_name,
	e.department_id,
	CONCAT(
		a.number,
		' ',
		a.street
	) AS address
FROM 
	employees AS e, addresses as a
WHERE
	a.id = e.address_id
ORDER BY
	address;

-- Task 21

ALTER VIEW
	view_addresses
RENAME TO
	view_employee_addresses_info;

-- Task 22

DROP VIEW view_company_chart;

-- Task 23

UPDATE 
	projects
SET 
	name = UPPER(name)

-- Task 24

CREATE VIEW
	view_initials
AS
SELECT
	SUBSTRING(first_name, 1, 2) AS initial,
	last_name
FROM
	employees
ORDER BY
	last_name;

-- Task 25

SELECT 
	name,
	start_date
FROM
	projects
WHERE
	name LIKE 'MOUNT%';
    