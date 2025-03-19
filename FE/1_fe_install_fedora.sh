# Fedora bash commands to install dependaces for FE.

sudo dnf install nodejs npm                             # Install node.js and node package manager.

sudo npm install -g @vue/cli                            # Install vue CLI.

cd ~/qop/GitHub/library-project/FE                      # Change directory to where I want to create new project.

sudo vue create my-vue-app                              # Create new project.
# During creation choose the TypeScript version.

sudo chown -R l_qopd:l_qopd my-vue-app                  # Change ownership to current user to have permissions to change configs easily.

cd my-vue-app                                           # Go to project folder.

sudo npm install axios                                  # Install Axios for API calling.