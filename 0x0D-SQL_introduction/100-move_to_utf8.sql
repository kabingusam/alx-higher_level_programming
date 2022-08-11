-- Convert hbtn_0c_0 database to UTF8
-- utf8mb4, collate utf8mb4_unicode_ci in the MySQL server
USE DATABASE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT CHARACTER SET TO utf8mb4 collate utf8mb4_unicode_ci;