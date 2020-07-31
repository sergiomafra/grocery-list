# grocery-list
Web app to build a grocery list

## Main GOAL
To build a portfolio application utilizing a predefined stack

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

## Techs to be implemented
- **Backend Main Language:** Python3
- **API Framework:** Flask & Flask Plugins
- **Database manipulation**: SQLAlchemy
- **Tests**: pytest/unittest
- **Frontend Main Language:** JavaScript
- **Frontend Framework:** Vue.js

## Installation
1) Docker should be installed on the system. Follow the instructions on this page:\
https://docs.docker.com/get-docker/
2) Next, docker-compose should also be installed. docker-compose set up:\
https://docs.docker.com/compose/install/
3) Now, run the following code o terminal:

    `$ cd /path/to/installation/directory`

    *then*

    `$ git clone https://github.com/sergiomafra/grocery-list`\
    `$ cd grocery-list`\
    `$ docker-compose build`\
    `$ docker-compose up`

    *or*

    `$ chmod a+x install.sh & ./install.sh`