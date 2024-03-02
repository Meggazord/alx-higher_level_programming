-- Convert hbtn_0c_0 database, first_table table, and name field to UTF8
-- Database, table, and field should be in utf8mb4, collate utf8mb4_unicode_ci
-- Connect to MySQL server using root user
-- Credentials: root/root

USE hbtn_0c_0;

-- qeuries:
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;