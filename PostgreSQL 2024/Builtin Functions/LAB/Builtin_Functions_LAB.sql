-- Task 01

SELECT title FROM books
WHERE SUBSTRING(title, 1, 3) = 'The' 
ORDER BY id;

-- Task 02

SELECT REPLACE(title, LEFT(title, 3),'***')
AS "Title" FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

-- Task 03

SELECT id,
    (side*height)/2 AS area
FROM triangles
ORDER BY id;

-- Task 04

SELECT title,
    round(cost, 3) AS modified_price
FROM books
ORDER BY id;

-- Task 05

SELECT first_name, last_name,
    EXTRACT(year FROM born)
    AS year
FROM authors;

-- Task 06

SELECT last_name AS "Last Name",
TO_CHAR(born,
'DD (Dy) Mon YYYY') AS
"Date of Birth"
FROM authors;

-- Task 07

SELECT title FROM books
WHERE title LIKE '%Harry Potter%'
ORDER BY id;
