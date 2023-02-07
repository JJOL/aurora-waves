### STAGE 1: Building ###
FROM node:18-alpine AS build
RUN apk add chromium
WORKDIR /usr/src/app
ENV CHROME_BIN=/usr/bin/chromium-browser
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run test
RUN npm run build

### STAGE 2: Running Web Server ###
FROM nginx:1.23.3-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /usr/src/app/dist/dockeraang /usr/share/nginx/html
