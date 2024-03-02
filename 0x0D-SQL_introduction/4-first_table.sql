-- Create table first_table in the specified database
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
