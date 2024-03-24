FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .


#CMD ['python', 'manage.py', 'runserver']

#docker built

#docker run

#FROM node:18-alpine
#WORKDIR /app
#COPY . .
#RUN yarn install --production
#CMD ["node", "src/index.js"]
#EXPOSE 3000

#docker build -t getting-started .
#docker run -dp 127.0.0.1:3000:3000 getting-started