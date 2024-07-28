SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
	-- LTRIM(continent_name) AS "trim" -- same thing as the upper solution
FROM
	continents;