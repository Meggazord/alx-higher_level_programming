-- This script creates a table named unique_id on your MySQL server.
-- The table has two columns: id (INT) with a default value of 1 and must be unique, and name (VARCHAR(256)).
-- The script inserts data into the table and performs a SELECT query to retrieve the data.
-- The database name will be passed as an argument to the mysql command.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
