# Dockerized phonebook app for Ops School project
FROM python:3.6
MAINTAINER Nofar Spalter <nofars@gmail.com>

# Create app directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

EXPOSE 8080
CMD ["python","phonebook.py","-w"]