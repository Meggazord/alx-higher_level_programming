-- Create table second_table and add multiple rows
-- Connect to MySQL server using root user
-- Credentials: root/root
-- Database name passed as an argument

USE hbtn_0c_0;

-- Create second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Add multiple rows to second_table
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
