-- Display the max temperature of each state ordered by state name
-- Connect to MySQL server using root user
-- Credentials: root/root

USE hbtn_0c_0;

SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
