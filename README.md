# grocery-list
Web app to build a grocery list

## Main GOAL
To build a portfolio application with a predefined stack

## Features / Goals
- CRUD of grocery items
- Selection of items to build a customized grocery list
- Possibility to export as text, maybe to Telegram
- Checkboxes for items ordered and out of stock
- Grocery history

## Techs used so far
- **OS:** Ubuntu 20.04
- **IDE:** VSCode & plugins
- **Version control:** git
- **Branch naming convention:** git-flow
- **Containerization:** Docker & docker-compose
- **Database:** PostgreSQL
- **Web server:** NGINX
- **WSGI HTTP Server:** Gunicorn
- **Backend Main Language:** Python3
- **API Framework:** Flask & Flask Plugins
- **Database manipulation**: SQLAlchemy, Migrate
- **Frontend Main Language:** JavaScript
- **Frontend Framework:** Vue.js

## Techs to be implemented
- **Tests**: pytest/unittest

## Installation
First, be sure that the ports 80 and 8080 are not being used. If they are being used by other applications, change the docker-compose.yml file to map those ports to another.\

Now, we need to make sure some dependencies are installed on the system: Docker and docker-compose. Follow the instructions on this page:\
Docker: https://docs.docker.com/get-docker/\
docker-compose: https://docs.docker.com/compose/install/

Finally, run the following code o terminal to install the app:

    $ cd /path/to/installation/directory

*then*

    $ git clone https://github.com/sergiomafra/grocery-list
    $ cd grocery-list
    $ docker-compose build

*or*

    $ chmod a+x install.sh & ./install.sh

## Run the app
    $ docker-compose up -d

## Application
APP: http://localhost:80\
API: http://localhost:8080