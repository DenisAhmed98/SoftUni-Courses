SELECT 
	peak_name,
	LEFT(peak_name, 4) AS positive_left, -- Get the first 4
	LEFT(peak_name, -4) AS negative_left -- Get everything but the last 4
FROM 
	peaks;