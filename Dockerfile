FROM python:3.11-slim-bookworm

LABEL maintainer="Joaquin Gonzalez <joagonzalez@gmail.com>"
LABEL application="Calculator seed project for python apps"
LABEL VERSION="0.0.1"

# setup environment variable  
ENV APP_DIR=app 
ENV APP_NAME=calculator
ENV APP_PORT=8000 
ENV APP_HOST=0.0.0.0

# set work directory  
RUN mkdir -p ${APP_DIR}

# where your code lives  
WORKDIR ${APP_DIR} 

# copy whole project to your docker home directory. 
COPY ./ /app

# install iamge pre reqs 
RUN apt update && apt install make

# install app libraries
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["make", "run"]