-- Compute the average score of all records in table second_table
-- Result column name: average
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

SELECT AVG(score) AS average FROM second_table;
