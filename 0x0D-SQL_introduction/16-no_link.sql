-- List all records of table second_table
-- Only list rows with a name value
-- Display score and name (in this order)
-- Sort records by descending score
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
