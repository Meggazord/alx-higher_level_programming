-- This script creates or ensures the existence of the database hbtn_0d_2 and the user user_0d_2.
-- The user_0d_2 is granted only the SELECT privilege in the hbtn_0d_2 database, and its password is set to user_0d_2_pwd.
-- If the database hbtn_0d_2 already exists, the script does not fail.
-- If the user user_0d_2 already exists, the script does not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
