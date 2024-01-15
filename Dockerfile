FROM python:3.11-slim-bookworm

LABEL maintainer="Joaquin Gonzalez <joagonzalez@gmail.com>"
LABEL application="Observability as a Service - Dashboards as a Service component"
LABEL VERSION="1.0.0"

# setup environment variable  
ENV APP_DIR=app 
ENV APP_NAME=observability_workflows
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