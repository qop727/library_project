# Fedora bash commands for DB installation on the server.

sudo dnf install mariadb-server         # DB installation on server.

sudo systemctl start mariadb            # Run service.
sudo systemctl enable mariadb           # Enable service.
systemctl daemon-reload                 # Reload daemon.

sudo mysql_secure_installation          #Run secure installation of DB.
# Installation will appear - continue with installation steps.
# Most important is to change root password.

mysql -u root -p                        # Login into DB with root user.
# Continue with SQL commands in books_db.sql file.
