-- 1-create_user.sql
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
ALTER USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'%';
FLUSH PRIVILEGES;
