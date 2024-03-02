-- List the number of records with the same score in table second_table
-- Display score and number of records with label number
-- Sort the list by the number of records (descending)
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

USE hbtn_0c_0;

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
