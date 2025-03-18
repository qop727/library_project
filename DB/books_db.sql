-- SQL commands for DB installation on the server.

CREATE DATABASE books_db;                                       -- Creating DB.
CREATE USER 'qop'@'localhost' IDENTIFIED BY 'password';         -- Creating user and pwd (mypwd).
GRANT ALL PRIVILEGES ON books_db.* TO 'username'@'localhost';   -- Granting privileges for qop user.
FLUSH PRIVILEGES;
EXIT;