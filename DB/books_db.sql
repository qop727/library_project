-- SQL commands for DB installation on the server.

CREATE DATABASE books_db;                                       -- Creating DB.
CREATE USER 'qop'@'localhost' IDENTIFIED BY 'Pwd1234';          -- Creating user and pwd.
GRANT ALL PRIVILEGES ON books_db.* TO 'qop'@'localhost';        -- Granting privileges for qop user.
FLUSH PRIVILEGES;                                               -- Apply the changes.
EXIT;                                                           -- Exit the DB shell.