-- Update the score of Bob to 10 in table second_table
-- Use the name field, not the id value
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

UPDATE second_table SET score = 10 WHERE name = 'Bob';
