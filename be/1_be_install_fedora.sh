# Fedora bash commands for creation of virtual environment and installation of packages needed on the server.

python3 -m venv venv                                    # Creation of virtual environment.

sudo chmod +x ~/library_project/app.py                  # Adding execute permissions to BE scrypt.

source venv/bin/activate                                # Activation of virtual environment.

pip install Flask flask_sqlalchemy flask_cors PyMySQL   # Installation of needed packages.