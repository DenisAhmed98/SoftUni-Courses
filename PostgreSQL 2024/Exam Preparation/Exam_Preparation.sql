-- Task 01

CREATE TABLE IF NOT EXISTS addresses (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL 
);

CREATE TABLE IF NOT EXISTS categories (
	id SERIAL PRIMARY KEY,
	name VARCHAR(10) NOT NULL 
);

CREATE TABLE IF NOT EXISTS clients (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(50) NOT NULL,
	phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS drivers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	age INT NOT NULL,
	rating NUMERIC(2) DEFAULT 5.5, 
	
	CONSTRAINT ck_drivers_age_is_postive
		CHECK (age > 0)
);

CREATE TABLE IF NOT EXISTS cars (
	id SERIAL PRIMARY KEY,
	make VARCHAR(20) NOT NULL,
	model VARCHAR(20),
	year INT NOT NULL DEFAULT 0,
	mileage INT DEFAULT 0,
	condition CHAR(1) NOT NULL,
	category_id INT NOT NULL,
	
	CONSTRAINT ck_car_year_is_positive
		CHECK (year > 0),
	CONSTRAINT ck_car_mileage_is_positive
		CHECK (mileage > 0),
	CONSTRAINT fk_cars_categories
		FOREIGN KEY (category_id)
		REFERENCES categories(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS courses (
	id SERIAL PRIMARY KEY,
	from_address_id INT NOT NULL,
	start TIMESTAMP NOT NULL,
	bill NUMERIC(10, 2) DEFAULT 10,
	car_id INT NOT NULL,
	client_id INT NOT NULL,
	
	CONSTRAINT ck_courses_bill_is_positive
		CHECK (bill > 0),
	
	CONSTRAINT fk_courses_addresses
		FOREIGN KEY (from_address_id)
		REFERENCES addresses(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_courses_cars
		FOREIGN KEY (car_id)
		REFERENCES cars(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_courses_clients
		FOREIGN KEY (client_id)
		REFERENCES clients(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cars_drivers (
	car_id INT NOT NULL,
	driver_id INT NOT NULL,
	
	CONSTRAINT fk_cars_drivers_cars
		FOREIGN KEY (car_id)
		REFERENCES cars(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_cars_drivers_drivers
		FOREIGN KEY (driver_id)
		REFERENCES drivers(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Task 02

INSERT INTO
	clients(full_name, phone_number)
SELECT 
	first_name || ' ' || last_name,
	'(088) 9999' || id * 2
FROM 
	drivers
WHERE
	id BETWEEN 10 AND 20;

-- Task 03

UPDATE 
	cars
SET 
	condition = 'C'
WHERE
	(mileage >= 800000 OR mileage IS NULL) 
		AND
	year <= 2010
		AND
	make <> 'Mercedes-Benz';

-- Task 04

DELETE FROM
	clients
WHERE
	LENGTH(full_name) > 3
		AND
	id NOT IN (
		SELECT
			client_id
		FROM
			courses
	)

-- Task 05

SELECT 
	make,
	model,
	condition
FROM
	cars
ORDER BY
	id;

-- Task 06

SELECT 
	d.first_name,
	d.last_name,
	c.make,
	c.model,
	c.mileage
FROM 
	drivers AS d
JOIN
	cars_drivers AS cd
ON 
	d.id = cd.driver_id
JOIN 
	cars AS c
ON
	cd.car_id = c.id
WHERE 
	c.mileage IS NOT NULL
ORDER BY
	c.mileage DESC,
	d.first_name ASC;

-- Task 07

SELECT
	cr.id AS car_id,
	cr.make,
	cr.mileage,
	COUNT(co.id) AS count_of_courses,
	ROUND(AVG(co.bill), 2) AS average_bill
FROM
	cars AS cr
LEFT JOIN
	courses AS co
ON 
	cr.id = co.car_id
GROUP BY
	cr.id
HAVING 
	COUNT(co.id) <> 2
ORDER BY
	count_of_courses DESC,
	cr.id ASC;

-- Task 08

SELECT 
	cl.full_name,
	COUNT(co.car_id) AS count_of_cars,
	SUM(co.bill) AS total_sum
FROM
	clients AS cl
JOIN
	courses AS co
ON 
	cl.id = co.client_id
WHERE 
	SUBSTRING(cl.full_name, 2, 1) = 'a' 
GROUP BY
	cl.full_name
HAVING
	COUNT(car_id) > 1
ORDER BY 
	cl.full_name;

-- Task 09

SELECT
	a.name,
	CASE 
		WHEN EXTRACT(HOUR FROM c.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	c.bill,
	cl.full_name,
	cr.make,
	cr.model,
	ca.name
FROM
	courses AS c
JOIN
	clients AS cl
ON 
	c.client_id = cl.id
JOIN 
	cars AS cr
ON
	cr.id = c.car_id
JOIN
	categories AS ca
ON
	ca.id = cr.category_id
JOIN
	addresses AS a
ON
	a.id = c.from_address_id
ORDER BY 
	c.id;

-- Task 10

CREATE OR REPLACE FUNCTION fn_courses_by_client(
	phone_num VARCHAR(20)
) RETURNS INT
AS
$$
BEGIN
	RETURN (
		SELECT 
			COUNT(*)
		FROM
			clients AS cl
		JOIN	
			courses AS co
		ON
			co.client_id = cl.id
		WHERE 
			cl.phone_number = phone_num
	);
END;
$$
LANGUAGE plpgsql;

-- Task 11

CREATE TABLE IF NOT EXISTS search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(
	address_name VARCHAR(100)
) 
AS
$$
BEGIN
	TRUNCATE search_results;
	
	INSERT INTO search_results (
		address_name,
		full_name,
		level_of_bill,
		make,
		condition,
		category_name
	)
	SELECT
		address_name,
		cl.full_name,
		CASE
			WHEN co.bill <= 20 THEN 'Low'
			WHEN co.bill <= 30 THEN 'Medium' 
			ELSE 'High'
		END, 
		cr.make,
		cr.condition,
		ca.name
	FROM
		addresses AS a
	JOIN
		courses AS co
	ON
		a.id = co.from_address_id
	JOIN
		cars AS cr
	ON
		co.car_id = cr.id
	JOIN
		categories AS ca
	ON
		ca.id = cr.category_id
	JOIN
		clients AS cl
	ON
		cl.id = co.client_id
	WHERE
		a.name = address_name
	ORDER BY
		cr.make,
		cl.full_name;
END;
$$
LANGUAGE plpgsql;