-- SQL commands to change pwd for qop user in DB.

ALTER USER 'qop'@'localhost' IDENTIFIED BY 'Pwd1234';   -- Change pwd for qop user.
FLUSH PRIVILEGES;                                       -- Apply changes.
EXIT;

-- if ALTER USER does not work.
UPDATE mysql.user SET authentication_string = PASSWORD('Pwd1234') WHERE User = 'qop';
FLUSH PRIVILEGES;
EXIT;