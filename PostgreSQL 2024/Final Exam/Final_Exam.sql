-- Task 01

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL,
    age INTEGER NOT NULL,
    job_title VARCHAR(40) NOT NULL,
    ip VARCHAR(30) NOT NULL,

	CONSTRAINT ck_acc_gender
		CHECK (gender IN ('M', 'F'))
);

CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    street VARCHAR(30) NOT NULL,
    town VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    account_id INTEGER NOT NULL,

	CONSTRAINT fk_adresses_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE photos (
    id SERIAL PRIMARY KEY,
    description TEXT,
    capture_date TIMESTAMP NOT NULL,
    views INTEGER DEFAULT 0 NOT NULL,

	CONSTRAINT ck_views_are_positive
		CHECK (views >= 0)
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    published_on TIMESTAMP NOT NULL,
    photo_id INTEGER NOT NULL,

	CONSTRAINT fk_comments_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE accounts_photos (
    account_id INTEGER NOT NULL,
    photo_id INTEGER NOT NULL,
	PRIMARY KEY (account_id, photo_id),
	
	CONSTRAINT fk_accounts_photos_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_accounts_photos_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    photo_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,

	CONSTRAINT fk_likes_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_likes_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Task 02

INSERT INTO 
	addresses (street, town, country, account_id)
SELECT 
	username, 
	password, 
	ip, 
	age
FROM 
	accounts
WHERE 
	gender = 'F';

-- Task 03

UPDATE 
	addresses
SET country = CASE
    WHEN country LIKE 'B%' THEN 'Blocked'
    WHEN country LIKE 'T%' THEN 'Test'
    WHEN country LIKE 'P%' THEN 'In Progress'
    ELSE country
END;

-- Task 04

DELETE FROM 
	addresses
WHERE id % 2 = 0 AND street ILIKE '%r%';

-- Task 05

SELECT 
	username,
	gender,
	age
FROM accounts
WHERE age >= 18 AND LENGTH(username) > 9
ORDER BY age DESC, username ASC;

-- Task 06

SELECT 
	p.id AS photo_id,
	p.capture_date,
	p.description,
	COUNT(c.id) AS comments_count
FROM photos p
JOIN 
	comments c ON p.id = c.photo_id
WHERE p.description IS NOT NULL
GROUP BY p.id
ORDER BY comments_count DESC, p.id ASC
LIMIT 3;

-- Task 07

SELECT 
	CONCAT(a.id, ' ', a.username) AS id_username, 
	a.email
FROM accounts a
JOIN accounts_photos ap ON a.id = ap.account_id AND a.id = ap.photo_id
ORDER BY a.id ASC;

-- Task 08

SELECT p.id AS photo_id, 
       (SELECT COUNT(*) FROM likes l WHERE l.photo_id = p.id) AS likes_count,
       (SELECT COUNT(*) FROM comments c WHERE c.photo_id = p.id) AS comments_count
FROM photos p
ORDER BY likes_count DESC, comments_count DESC, p.id ASC;

-- Task 09

SELECT CASE 
           WHEN p.description IS NULL THEN '...' 
           ELSE LEFT(p.description, 10) || '...' 
       END AS summary, 
       TO_CHAR(p.capture_date, 'DD.MM HH24:MI') AS date
FROM photos p
WHERE EXTRACT(DAY FROM p.capture_date) = 10
ORDER BY p.capture_date DESC;

-- Task 10

CREATE OR REPLACE FUNCTION 
	udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INTEGER AS $$
BEGIN
    RETURN (SELECT COUNT(*) 
            FROM accounts_photos ap
            JOIN accounts a ON ap.account_id = a.id
            WHERE a.username = account_username);
END;
$$ LANGUAGE plpgsql;

-- Task 11

CREATE OR REPLACE PROCEDURE 
	udp_modify_account(address_street VARCHAR(30), address_town VARCHAR(30))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE accounts
    SET job_title = '(Remote) ' || job_title
    WHERE id = (
		SELECT 
			account_id 
		FROM addresses 
		WHERE street = address_street AND town = address_town);
END;
$$;