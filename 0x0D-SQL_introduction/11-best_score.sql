-- List records with score >= 10 in table second_table
-- Display score and name columns
-- Order records by score in descending order
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
