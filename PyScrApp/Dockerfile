### Dockerfile for ScrApp.py
# base for the container
FROM python:3.8-alpine

LABEL author="ninocan" maintainer="ninocangialosi@yahoo.it" 

# import the project files and move to the folder
# where they are located in the container
COPY . /app
WORKDIR /app
RUN mkdir Posters

# install dependencies
RUN pip install -r requirements.txt

#open port for connection
#EXPOSE 5000

#launch the application
CMD ["python", "./scrapp.py"]
