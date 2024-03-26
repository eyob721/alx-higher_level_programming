-- Converts the database `hbtn_0c_0`, the table `first_table` and the field
-- `name` in the table `first_table` to UTF8 (utf8mb4 and collate utf8mb4_unicode_ci)
-- select the database
USE hbtn_0c_0;


-- convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- convert the table (which converts all the columns in it as well)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
