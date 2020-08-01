# Pull node image from Docker HUB
FROM node:lts-alpine

# Work directory
WORKDIR /srv/app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Copy both 'package.json' and 'package-lock.json'
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy project files and folders to the current working directory
COPY . /srv/app/