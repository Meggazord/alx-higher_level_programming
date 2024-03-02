-- Convert hbtn_0c_0 database, first_table table, and name field to UTF8
-- Database, table, and field should be in utf8mb4, collate utf8mb4_unicode_ci
-- Connect to MySQL server using root user
-- Credentials: root/root

-- Convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table
ALTER TABLE first_table MODIFY name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
