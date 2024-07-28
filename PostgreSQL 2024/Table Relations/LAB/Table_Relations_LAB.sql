-- Task 01

CREATE TABLE mountains(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE peaks(
    id INT GENERATED ALWAYS AS IDENTITY UNIQUE,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_peaks_mountains
        FOREIGN KEY (mountain_id)
            REFERENCES mountains(id)
);

-- Task 02

SELECT driver_id, vehicle_type,
    CONCAT(first_name, ' ', last_name) AS driver_name
FROM vehicles AS v
JOIN campers AS c
    ON v.driver_id = c.id;

-- Task 03

SELECT start_point, end_point, leader_id,
    CONCAT(c.first_name, ' ', c.last_name) AS
leader_name
FROM routes AS r
JOIN campers AS c
    ON r.leader_id = c.id;

-- Task 04

CREATE TABLE peaks(
 id SERIAL PRIMARY KEY,
 name VARCHAR(50) NOT NULL,
 mountain_id INT,
 CONSTRAINT fk_mountain_id
 FOREIGN KEY(mountain_id)
 REFERENCES mountains(id)
 ON DELETE CASCADE
);

-- Task 05

CREATE TABLE mountains(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
CREATE TABLE peaks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_mountain_id
    FOREIGN KEY(mountain_id)
    REFERENCES mountains(id)
    ON DELETE CASCADE
);
