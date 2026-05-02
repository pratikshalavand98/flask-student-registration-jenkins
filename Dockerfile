FROM node:18

WORKDIR /app

COPY package.json .

RUN npm install   # cache use karega

COPY . .

CMD ["node", "app.js"]
