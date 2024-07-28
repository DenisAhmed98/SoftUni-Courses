SELECT 
	peak_name,
	RIGHT(peak_name, 4) AS positive_right, -- Get the last 4
	RIGHT(peak_name, -4) AS negative_right -- Get everything but the first 4
FROM 
	peaks;