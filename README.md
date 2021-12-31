# odoo-fe-test
Setup dedicated for new a engineer to show ability to modify Odoo FE functionality

Prerequisites:
Docker and docker-compose should be installed your machine.

Project setup:
1. Navigate to ./env folder and build containers with database and web service by running a command:
   `docker-compose build`
2. Run the web service by executing command:
    `docker-compose up`
3. Go to the web browser navigate to the service page using the local port specified in compose file. (e.g. http://localhost:8019/);
4. Create a database;
5. In Apps menue search and install Odoo FE test module;
It will also install Contacts and Website modules as a dependency, that is how you know the module installed successfully.

Hint: Going to settings and activating developer mode/ developer mode (with assets) could be useful.