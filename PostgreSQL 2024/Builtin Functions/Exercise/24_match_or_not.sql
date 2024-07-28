SELECT
	companion_full_name,
	email
FROM
	users
WHERE
	companion_full_name ILIKE '%aNd%' -- and And aNd anD....
		AND
	email NOT LIKE '%@gmail'; -- sasho@gmail - not valid; sasho@gmail.com - valid cause its not ending gmail