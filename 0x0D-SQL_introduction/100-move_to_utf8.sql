-- Converts the database `hbtn_0c_0`, the table `first_table`, and the column
-- `name` to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- Select the database
USE hbtn_0c_0;


-- Convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- Convert the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- Convert the column
ALTER TABLE first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
