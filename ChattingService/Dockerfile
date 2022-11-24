FROM node:12.22.9-alpine3.14

# Create app directory
RUN mkdir -p /ChattingService
WORKDIR /ChattingService

# Install app dependencies
COPY package.json /ChattingService
RUN npm install

# Bundle app source
COPY . /ChattingService

EXPOSE 8008