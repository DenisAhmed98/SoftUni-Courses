-- Task 01

SELECT 
	a.address || ' ' || a.address_2 AS apartment_address,
	b.booked_for AS nights
FROM
	apartments AS a
JOIN 
	bookings AS b
USING 
	(booking_id)
ORDER BY
	a.apartment_id ASC;

-- Task 02

SELECT 
	a.name,
	a.country,
	b.booked_at::DATE
FROM
	apartments AS a
LEFT JOIN
	bookings AS b
USING
	(booking_id)
LIMIT 10;

-- Task 03

SELECT 
	a.name,
	a.country,
	b.booked_at::DATE
FROM
	apartments AS a
LEFT JOIN
	bookings AS b
USING
	(booking_id)
LIMIT 10;

-- Task 04

SELECT 
	b.booking_id,
	a.name AS apartment_owner,
	a.apartment_id,
	c.first_name || ' ' || c.last_name AS customer_name
FROM
	bookings AS b
FULL JOIN
	apartments AS a
USING 
	(booking_id)
FULL JOIN
	customers AS c
USING 
	(customer_id)
ORDER BY
	b.booking_id,
	apartment_owner,
	customer_name;

-- Task 05

SELECT 
	b.booking_id,
	c.first_name AS customer_name
FROM
	bookings AS b
CROSS JOIN
	customers AS c
ORDER BY 
	customer_name;

-- Task 06

SELECT 
	b.booking_id,
	b.apartment_id,
	c.companion_full_name
FROM
	bookings AS b
JOIN 
	customers AS c
USING
	(customer_id)
WHERE 
	b.apartment_id IS NULL;

-- Task 07

SELECT 
	b.apartment_id,
	b.booked_for,
	c.first_name,
	c.country
FROM
	bookings AS b
JOIN 
	customers AS c
USING
	(customer_id)
WHERE 
	c.job_type = 'Lead';

-- Task 08

SELECT 
	COUNT(*)
FROM 
	bookings AS b
JOIN
	customers AS c
USING 
	(customer_id)
WHERE 
	c.last_name = 'Hahn';

-- Task 09

SELECT 
	a.name,
	SUM(b.booked_for)
FROM 
	apartments AS a
JOIN
	bookings AS b
USING 
	(apartment_id)
GROUP BY
	a.name
ORDER BY
	a.name;

-- Task 10

SELECT
	a.country,
	COUNT(b.booking_id) AS booking_count
FROM
	bookings AS b
JOIN 
	apartments AS a
USING 
	(apartment_id)
WHERE 
	b.booked_at > '2021-05-18 07:52:09.904+03'
		AND
	b.booked_at < '2021-09-17 19:48:02.147+03' 
GROUP BY
	country
ORDER BY
	booking_count DESC;

-- Task 11

SELECT
	a.country,
	COUNT(b.booking_id) AS booking_count
FROM
	bookings AS b
JOIN 
	apartments AS a
USING 
	(apartment_id)
WHERE 
	b.booked_at > '2021-05-18 07:52:09.904+03'
		AND
	b.booked_at < '2021-09-17 19:48:02.147+03' 
GROUP BY
	country
ORDER BY
	booking_count DESC;

-- Task 12

SELECT 
	mc.country_code,
	COUNT(m.mountain_range) AS mountain_range_count
FROM
	mountains_countries AS mc
JOIN 
	mountains AS m
ON 
	m.id = mc.mountain_id
WHERE 
	mc.country_code IN ('US', 'RU', 'BG')
GROUP BY
	mc.country_code
ORDER BY
	mountain_range_count DESC;

-- Task 13

SELECT
	c.country_name,
	r.river_name
FROM
	countries AS c
LEFT JOIN 
	countries_rivers AS cr
USING
	(country_code)
LEFT JOIN
	rivers  AS r
ON 
	r.id = cr.river_id
WHERE 
	c.continent_code = 'AF'
ORDER BY 
	c.country_name
LIMIT 5;

-- Task 14

SELECT 
	MIN(average_area) AS min_average_area
FROM (
	SELECT
		AVG(area_in_sq_km) AS average_area
	FROM 
		countries 
	GROUP BY
		continent_code
) AS min_average_area

-- Task 15

SELECT
	COUNT(*)
FROM
	countries AS c
LEFT JOIN 
	mountains_countries AS mc
USING 
	(country_code)
WHERE 
	mc.mountain_id IS NULL;

-- Task 16

CREATE TABLE IF NOT EXISTS monasteries (
	id SERIAL PRIMARY KEY,
	monastery_name VARCHAR(255),
	country_code CHAR(2)
);

INSERT INTO 
	monasteries (monastery_name, country_code)
VALUES
  ('Rila Monastery "St. Ivan of Rila"', 'BG'),
  ('Bachkovo Monastery "Virgin Mary"', 'BG'),
  ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
  ('Kopan Monastery', 'NP'),
  ('Thrangu Tashi Yangtse Monastery', 'NP'),
  ('Shechen Tennyi Dargyeling Monastery', 'NP'),
  ('Benchen Monastery', 'NP'),
  ('Southern Shaolin Monastery', 'CN'),
  ('Dabei Monastery', 'CN'),
  ('Wa Sau Toi', 'CN'),
  ('Lhunshigyia Monastery', 'CN'),
  ('Rakya Monastery', 'CN'),
  ('Monasteries of Meteora', 'GR'),
  ('The Holy Monastery of Stavronikita', 'GR'),
  ('Taung Kalat Monastery', 'MM'),
  ('Pa-Auk Forest Monastery', 'MM'),
  ('Taktsang Palphug Monastery', 'BT'),
  ('Sümela Monastery', 'TR');

ALTER TABLE 
	countries
ADD COLUMN 
	three_rivers BOOLEAN DEFAULT FALSE;

UPDATE
	countries
SET three_rivers = (
	SELECT
		COUNT(*) >= 3
	FROM 
		countries_rivers AS cr
	WHERE 
		cr.country_code = countries.country_code
);

SELECT 
	m.monastery_name,
	c.country_name
FROM
	monasteries AS m
JOIN 
	countries AS c
USING
	(country_code)
WHERE 
	NOT three_rivers
ORDER BY
	monastery_name;

-- Task 17

UPDATE countries
SET 
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';

INSERT INTO monasteries(monastery_name,country_code)
VALUES
	(
	'Hanga Abbey', 
	(SELECT
		country_code
	FROM
		countries
	WHERE 
	country_name = 'Tanzania')
	);

SELECT
	c.continent_name,
	cs.country_name,
	count(m.country_code) AS monasteries_count
FROM
	continents AS c
JOIN
	countries AS cs
USING
	(continent_code)
LEFT JOIN
	monasteries AS m -- left cause there can be countries with no monasteries
USING
	(country_code)
WHERE cs.three_rivers IS NOT TRUE
GROUP BY
	cs.country_name,
	c.continent_name
ORDER BY
	monasteries_count DESC,
	country_name;

-- Task 18

SELECT
	tablename,
	indexname,
	indexdef
FROM 
	pg_indexes
WHERE
	schemaname = 'public'
ORDER BY
	tablename,
	indexname;

-- Task 19

CREATE VIEW continent_currency_usage
AS
SELECT
	ru.continent_code,
	ru.currency_code,
	ru.currency_usage
FROM (
	SELECT 
		ct.continent_code,
		ct.currency_code,
		ct.currency_usage,
		DENSE_RANK() OVER (PARTITION BY ct.continent_code ORDER BY ct.currency_usage DESC) AS ranked_usage
	FROM (
		SELECT 
			continent_code,
			currency_code,
			COUNT(currency_code) AS currency_usage
		FROM
			countries
		GROUP BY
			continent_code,
			currency_code
		HAVING
			COUNT(*) > 1
		ORDER BY
			continent_code
	) AS ct
) AS ru
WHERE 
	ru.ranked_usage = 1
ORDER BY
	ru.currency_usage DESC,
	ru.continent_code ASC,
	ru.currency_code ASC;

-- Task 20

WITH
	"row_number"
AS
	(
	SELECT
		c.country_name,
		COALESCE(p.peak_name,'(no highest peak)') AS highest_peak_name,
		COALESCE(p.elevation, 0) AS highest_peak_elevation,
		COALESCE(m.mountain_range, '(no mountain)') AS mountain,
		ROW_NUMBER() OVER(PARTITION BY c.country_name ORDER BY p.elevation DESC) AS row_num
	FROM
		countries AS c
	LEFT JOIN
		mountains_countries AS mc
	USING	
		(country_code)
	LEFT JOIN
		peaks AS p
	USING
		(mountain_id)
	LEFT JOIN
		mountains AS m
	ON
		m.id = p.mountain_id
	)

SELECT
	country_name,
	highest_peak_name,
	highest_peak_elevation,
	mountain
FROM	
	"row_number"
WHERE
	row_num = 1
ORDER BY
	country_name,
	highest_peak_elevation DESC
;