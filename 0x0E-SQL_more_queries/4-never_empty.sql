-- This script creates the table id_not_null on the MySQL server.
-- The id_not_null table has two columns: id (of type INT with a default value of 1) and name (of type VARCHAR(256)).
-- If the table id_not_null already exists, the script does not fail.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
