-- This script creates the table force_name on the MySQL server.
-- The force_name table has two columns: id (of type INT) and name (of type VARCHAR(256) which cannot be null).
-- If the table force_name already exists, the script does not fail.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
