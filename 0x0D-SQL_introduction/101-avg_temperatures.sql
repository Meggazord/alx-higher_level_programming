-- Display average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Connect to MySQL server using root user
-- Credentials: root/root

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY (city)
ORDER BY avg_temp DESC;
