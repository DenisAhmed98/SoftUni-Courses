-- Task 01

CREATE TABLE products(
	product_name VARCHAR(50)
);

INSERT INTO
	products
VALUES
	('Broccoli'),
	('Shampoo'),
	('Toothpaste'),
	('Candy');

ALTER TABLE products
ADD COLUMN
	"id" SERIAL PRIMARY KEY;

-- Task 02

ALTER TABLE products
DROP CONSTRAINT
	products_pkey;

-- Task 03

CREATE TABLE passports (
    id INT GENERATED ALWAYS AS IDENTITY (START WITH 100 INCREMENT BY 1) PRIMARY KEY,
    nationality VARCHAR(50)
);

INSERT INTO passports (nationality) VALUES
('N34FG21B'),
('K65LO4R7'),
('ZE657QP2');

CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    salary NUMERIC(10, 2),
    passport_id INT,
    CONSTRAINT fk_passport
      FOREIGN KEY(passport_id) 
	  REFERENCES passports(id)
);

INSERT INTO people (first_name, salary, passport_id) VALUES
('Roberto', 43300.00, 101),
('Tom', 56100.00, 102),
('Yana', 60200.00, 100);

-- Task 04

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE models (
    id INT GENERATED ALWAYS AS IDENTITY (START WITH 1000 INCREMENT 1) PRIMARY KEY,
    model_name VARCHAR(50),
    manufacturer_id INT,
    CONSTRAINT fk_manufacturer
      FOREIGN KEY(manufacturer_id) 
      REFERENCES manufacturers(id)
);

CREATE TABLE production_years (
    id SERIAL PRIMARY KEY,
    established_on DATE,
    manufacturer_id INT,
    CONSTRAINT fk_manufacturer_year
      FOREIGN KEY(manufacturer_id) 
      REFERENCES manufacturers(id)
);

INSERT INTO manufacturers (name) VALUES
('BMW'),
('Tesla'),
('Lada');

INSERT INTO models (model_name, manufacturer_id) VALUES
('X1', 1),
('i6', 1),
('Model S', 2),
('Model X', 2),
('Model 3', 2),
('Nova', 3);

INSERT INTO production_years (established_on, manufacturer_id) VALUES
('1916-03-01', 1),
('2003-01-01', 2),
('1966-05-01', 3);

-- Task 06

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    date DATE
);

CREATE TABLE photos (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255),
    place VARCHAR(50),
    customer_id INT,
    CONSTRAINT fk_customer
      FOREIGN KEY(customer_id) 
      REFERENCES customers(id)
);

INSERT INTO customers (name, date) VALUES
('Bella', '2022-03-25'),
('Philip', '2022-07-05');

INSERT INTO photos (url, place, customer_id) VALUES
('bella_1111.com', 'National Theatre', 1),
('bella_1112.com', 'Largo', 1),
('bella_1113.com', 'The View Restaurant', 1),
('philip_1121.com', 'Old Town', 2),
('philip_1122.com', 'Rowing Canal', 2),
('philip_1123.com', 'Roman Theater', 2);

-- Task 08

INSERT INTO
	students(student_name)
VALUES 
	('Mila'),
	('Toni'),
	('Ron');

INSERT INTO 
	exams(exam_name)
VALUES 	
	('Python Advanced'),
	('Python OOP'),
	('PostgreSQL');

INSERT INTO
	study_halls(study_hall_name, exam_id)
VALUES 
	('Open Source Hall', 102),
	('Inspiration Hall', 101),
	('Creative Hall', 103),
	('Masterclass Hall', 103),
	('Information Security Hall', 103);;

INSERT INTO 
	students_exams
VALUES 
	(1, 101),
	(1, 102),
	(2, 101),
	(3, 103), 
	(2, 102),
	(2, 103);;

-- Task 10

CREATE TABLE item_types (
	id SERIAL PRIMARY KEY,
	item_type_name VARCHAR(50)
);

CREATE TABLE cities (
	id SERIAL PRIMARY KEY,
	city_name VARCHAR(50)
);

CREATE TABLE items (
	id SERIAL PRIMARY KEY,
	item_name VARCHAR(50),
	item_type_id INT,
	
	CONSTRAINT fk_items_item_types
	FOREIGN KEY (item_type_id)
	REFERENCES item_types(id)
);

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(50),
	birthday DATE,
	city_id INT,
	
	CONSTRAINT fk_customers_cities
	FOREIGN KEY (city_id)
	REFERENCES cities(id)
);

CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	customer_id INT,
	
	CONSTRAINT fk_orders_customers
	FOREIGN KEY (customer_id)
	REFERENCES customers(id)
);

CREATE TABLE order_items (
	order_id INT,
	item_id INT,
	
	CONSTRAINT pk_order_items
	PRIMARY KEY (order_id, item_id),
	
	CONSTRAINT fk_order_items_orders
	FOREIGN KEY (order_id)
	REFERENCES orders(id),
	
	CONSTRAINT fk_order_items_items
	FOREIGN KEY (item_id)
	REFERENCES items(id)
);

-- Task 11

ALTER TABLE 
	countries
	
ADD CONSTRAINT
	fk_countries_continents
FOREIGN KEY
	(continent_code)
REFERENCES
	continents(continent_code)
ON DELETE CASCADE,

ADD CONSTRAINT 
	fk_countries_currencies
FOREIGN KEY
	(currency_code)
REFERENCES
	currencies(currency_code)
ON DELETE CASCADE;

-- Task 12

ALTER TABLE 
	countries_rivers
	
ADD CONSTRAINT 
	fk_countries_rivers_rivers
FOREIGN KEY 
	(river_id)
REFERENCES 
	rivers(id)
ON UPDATE CASCADE,

ADD CONSTRAINT 
	fk_countries_rivers_countries
FOREIGN KEY 
	(country_code)
REFERENCES 
	countries(country_code)
ON UPDATE CASCADE;

-- Task 13

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(50)
);

CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	contact_name VARCHAR(50),
	phone VARCHAR(50),
	email VARCHAR(50),
	customer_id INT,
	
	CONSTRAINT fk_contacts_customers
	FOREIGN KEY (customer_id)
	REFERENCES customers(id)
	ON DELETE SET NULL
	ON UPDATE CASCADE
);

INSERT INTO 
	customers(customer_name)
VALUES 
	('BlueBird Inc'),
	('Dolphin LLC');

INSERT INTO
	contacts(customer_id, contact_name, phone, email)
VALUES 
	(1,'John Doe','(408)-111-1234','john.doe@bluebird.dev'),
    (1,'Jane Doe','(408)-111-1235','jane.doe@bluebird.dev'),
    (2,'David Wright','(408)-222-1234','david.wright@dolphin.dev');
	
DELETE FROM
	customers
WHERE 
	id = 1;

-- Task 14

SELECT 
	mountain_range,
	peak_name,
	elevation
FROM
	peaks
JOIN
	mountains
ON
	peaks.mountain_id = mountains.id
WHERE 
	mountain_range LIKE '%Rila%'
ORDER BY
	elevation DESC;

-- Task 15

SELECT
	COUNT(*)
FROM 
	countries
LEFT JOIN
	countries_rivers
-- ON
--     countries.country_code = countries_rivers.country_code
USING
	(country_code)
WHERE river_id IS NULL;