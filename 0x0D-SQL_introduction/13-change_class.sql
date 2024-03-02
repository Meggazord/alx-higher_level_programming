-- Remove records with score <= 5 in table second_table
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

USE hbtn_0c_0;

DELETE FROM second_table WHERE score <= 5;
