-- Task 01

SELECT id,
    first_name || ' ' || last_name
    AS "Full Name",
    job_title AS "Job Title"
FROM employees;

-- Task 02

SELECT id,
    first_name || ' ' || last_name
    AS "full_Name",
    job_title, salary
FROM employees
WHERE salary > 1000.00;

-- Task 03

SELECT id, first_name, last_name, job_title, department_id, salary
FROM employees
WHERE salary > 1000.00 AND department_id = 4
ORDER BY id;

-- Task 04

INSERT INTO employees (first_name, last_name, job_title, department_id, salary)
VALUES
    ('Samantha','Young', 'Housekeeping', 4, 900),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33);
SELECT * FROM employees;

-- Task 05

UPDATE employees
SET salary = salary + 100
WHERE job_title  = 'Manager';
SELECT * FROM employees
WHERE job_title  = 'Manager';

-- Task 06

DELETE FROM employees
WHERE department_id = 1 OR department_id = 2;
SELECT * FROM employees
ORDER BY id;

-- Task 07

CREATE VIEW top_paid_employee AS SELECT * FROM employees
ORDER BY salary DESC LIMIT 1;
SELECT * FROM top_paid_employee;