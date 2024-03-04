-- This script creates the database hbtn_0d_usa and the table states on your MySQL server.
-- The states table has two columns: id (INT) as a unique auto-generated primary key and name (VARCHAR(256)).
-- The script then inserts data into the states table and performs a SELECT query to retrieve the data.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; 
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
