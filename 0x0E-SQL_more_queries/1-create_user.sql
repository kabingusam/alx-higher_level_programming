-- Create user 
-- User should have all privileges
pass :user_0d_1_pwd
CREATE USER
    IF NOT EXISTS `user_0d_1`@`localhost`
    IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL PRIVILEGES
    ON *.*
    TO USER `user_0d_1`@`localhost`
    IDENTIFIED BY `user_0d_1_pwd`;
FLUSH PRIVILEGES;
