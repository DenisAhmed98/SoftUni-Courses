-- Task 01

SELECT
	COUNT("id") AS "count"
FROM wizard_deposits

-- Task 02

SELECT
	SUM("deposit_amount") AS "total_amount"
FROM wizard_deposits

-- Task 03

SELECT
	TRUNC(AVG("magic_wand_size"),3) AS "average_magic_wand_size"
FROM wizard_deposits

-- Task 04

SELECT
	MIN("deposit_charge") AS "mininimum_deposit_charge"
FROM wizard_deposits

-- Task 05

SELECT
	MAX("age") AS "maximum_age"
FROM wizard_deposits

-- Task 06

SELECT "deposit_group",
	SUM("deposit_interest")
FROM wizard_deposits
GROUP BY "deposit_group"
ORDER BY SUM("deposit_interest") DESC; 

-- Task 07

SELECT magic_wand_creator,
	MIN(magic_wand_size) AS magic_wand_size
FROM wizard_deposits
GROUP BY magic_wand_creator
ORDER BY magic_wand_size ASC
LIMIT 5;

-- Task 08

SELECT deposit_group,
	is_deposit_expired,
	FLOOR(AVG("deposit_interest")) AS "deposit_interest"
FROM wizard_deposits
WHERE deposit_start_date > '1985-01-01'
GROUP BY deposit_group, is_deposit_expired
ORDER BY deposit_group DESC, is_deposit_expired ASC;

-- Task 09

SELECT last_name,
	COUNT(notes) AS notes_with_dumbledor
FROM wizard_deposits
WHERE notes LIKE '%Dumbledor%'
GROUP BY last_name;

-- Task 10

CREATE VIEW
	"view_wizard_deposits_with_expiration_date_before_1983_08_17"
AS
SELECT
	CONCAT_WS(' ', first_name, last_name) AS wizard_name,
	deposit_start_date AS start_date,
	deposit_expiration_date AS expiration_date,
	SUM(deposit_amount) AS amount
FROM wizard_deposits
WHERE deposit_expiration_date <= '1983-08-17'
GROUP BY wizard_name,start_date,expiration_date
ORDER BY expiration_date ASC;

-- Task 11

SELECT magic_wand_creator,
	MAX(deposit_amount) AS max_deposit_amount
FROM wizard_deposits
GROUP BY magic_wand_creator
HAVING MAX(deposit_amount) NOT BETWEEN 20000 AND 40000
ORDER BY max_deposit_amount DESC
LIMIT 3;

-- Task 12

SELECT
	CASE
		WHEN age BETWEEN 0 and 10 THEN '[0-10]'
		WHEN age BETWEEN 11 and 20 THEN '[11-20]'
		WHEN age BETWEEN 21 and 30 THEN '[21-30]'
		WHEN age BETWEEN 31 and 40 THEN '[31-40]'
		WHEN age BETWEEN 41 and 50 THEN '[41-50]'
		WHEN age BETWEEN 51 and 60 THEN '[51-60]'
		ELSE '[61+]'
	END AS age_group,
		COUNT(age) as "count"
FROM wizard_deposits
GROUP BY age_group
ORDER BY age_group ASC

-- Task 13

SELECT
	COUNT(CASE department_id WHEN 1 THEN 1 END) AS "Engineering",
	COUNT(CASE department_id WHEN 2 THEN 1 END) AS "Tool Design",
	COUNT(CASE department_id WHEN 3 THEN 1 END) AS "Sales",
	COUNT(CASE department_id WHEN 4 THEN 1 END) AS "Marketing",
	COUNT(CASE department_id WHEN 5 THEN 1 END) AS "Purchasing",
	COUNT(CASE department_id WHEN 6 THEN 1 END) AS "Research and Development",
	COUNT(CASE department_id WHEN 7 THEN 1 END) AS "Production"
FROM employees

-- Task 14

UPDATE employees
SET salary =
    CASE
        WHEN hire_date < '2015-01-16' THEN salary + 2500
        WHEN hire_date < '2020-03-04' THEN salary + 1500
        ELSE salary
    END,
    job_title =
    CASE
        WHEN hire_date < '2015-01-16' THEN CONCAT('Senior ', job_title)
        WHEN hire_date < '2020-03-04' THEN CONCAT('Mid-', job_title)
        ELSE job_title
    END

-- Task 15

SELECT 
    job_title,
    CASE
        WHEN AVG("salary") > 45800 THEN 'Good'
        WHEN AVG("salary") BETWEEN 27500 AND 45800 THEN 'Medium'
        WHEN AVG("salary") < 27500 THEN 'Need Improvement'
    END AS category
FROM employees
GROUP BY job_title
ORDER BY category, job_title

-- Task 16

SELECT
    project_name,
    CASE
        WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
        WHEN start_date IS NOT NULL AND end_date IS NULL THEN 'In Progress'
        ELSE 'Done'
    END AS project_status
FROM projects
WHERE project_name LIKE '%Mountain%'

-- Task 17

SELECT 
    department_id,
    COUNT(department_id) AS num_employees,
    CASE
        WHEN AVG(salary) > 50000 THEN 'Above average'
        ELSE 'Below average'
    END AS salary_level
FROM employees
GROUP BY department_id
HAVING AVG("salary") > 30000
ORDER BY department_id

-- Task 18

CREATE VIEW view_performance_rating AS
SELECT
    first_name,
    last_name,
    job_title,
    salary,
    department_id,
    CASE
        WHEN salary >= 25000 and job_title LIKE 'Senior%' THEN 'High-performing Senior' 
        WHEN salary >= 25000 and job_title NOT LIKE 'Senior%' THEN 'High-performing Employee'
        ELSE 'Average-performing'
    END AS performance_rating
FROM employees

-- Task 19

CREATE TABLE employees_projects(
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    project_id INTEGER REFERENCES projects(id)
)

-- Task 20

SELECT
    *
FROM departments as d
    JOIN employees as e
        ON d.id = e.department_id