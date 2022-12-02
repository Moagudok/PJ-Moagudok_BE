FROM node:19-alpine3.15

# Create app directory
RUN mkdir -p /ChattingService
COPY package*.json /ChattingService/
WORKDIR /ChattingService

# Install app dependencies
RUN npm install -g npm@9.1.3
RUN npm install
RUN npm link socket.io
COPY . /ChattingService

# Bundle app source
EXPOSE 8008
