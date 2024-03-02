-- Display the max temperature of each state ordered by state name
-- Connect to MySQL server using root user
-- Credentials: root/root

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
