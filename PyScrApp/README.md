# Python webscraper ScrApp

## Setting the virtual environment
[**Source**](https://realpython.com/python-virtual-environments-a-primer )
This is similar to the npm init, but python has a little bit more complication.

Let's initailaize the virtual environment with:

      $ python3 -m venv env

So to create an isolated dependency for the project we need to activate it through:

   $ source env/bin/activate

This could be later deactivated simply by running `$ deactivate`.

## Installing the dependencies
[**Source**](https://realpython.com/python-web-scraping-practical-introduction )
We are going to use the `request` and `BeautifulSoup` packages which we can now install inside the venv with:

   $ pip install requests BeautifulSoup4

Following the [BeatifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id16 ), the best way to use it is through the use of a third party parser: [lxml](https://lxml.de ). Let us install it, as well:

   $ pip install lxml
In order to communicate with the MySQL server we also need to install a [mysql/python connector](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html )

   $ pip install mysql-connector-python
To sum up the extra dependencies needed are:
 * requests
 * BeatifulSoup4
 * lxml
 * mysql-connector-python
Moreover, the scraper will depend on the following standard libraries:
 - time
 - json
 - contextlib
 - hashlib
 these should already come with the basic python installation, but in case the program is not running make sure that are installed.
##The scraper

The name of the scraper is  `scrApp.py`, it depends on files from the `./Modules` folder, which are definitions of functions arrenged in such a way to keep everything neater. These files are found in the repo.

In addition to these files there are two other files that need to be created by hand, and these are the keys for the APIs and MySQL database.
For this purpose, create a file called `api.key` in which you need to insert the omdb password; for clarity (this is not the actual password):
```
S0m3NumB3R54nDd1git5
```
Then,touch a text file named `database_credential.key` with the following structure:
```
<database-user-name>
<database-user-password>
<host-address>
<database-name>
```
I chose to create a Docker container to run the MySQL database on it, this has been created with the following command:

  $ docker run -p 3306:3306 -d --rm  --name <container-name> -e MYSQL_USER=<database-user-name> -e MYSQL_ROOT_PASSWORD=<database-root-password> -e MYSQL_DATABASE=<database-name> -e MYSQL_PASSWORD=<database-user-password> -v $(pwd)/.data:/var/lib/mysql mysql:5.7
The flags has the following meaning

       TO BE DONE

In this way the container run on its own isolated environment and it is easy to fire it up or tear it down. Make sure that the fields in the last command match with the digits in the creditial file.

If you decide to use the mysql database on your local machine, then the <host-address> field in the credential file should be simply "localhost" eventually followed by the port. However, if you choose to proceed with the container road instead, in order to retrieve the correct address run the following:

   $ docker inspect <container-name>
and, then, by looking at the "IPAddress" entry.


### Extracting data from the database inside the container

During the course of the project, we had the need to extract manually the data inserted in the database. This was done by logging into the container with:

       $ docker exec -it <container-name> bash
Once inside, move to the folder `/var/run/mysqld` and run the following command:

     $ mysqldump -u <database-user-name> -p <database-name> > <database-record>.sql
To copy it outside of the container run the following comman:

      $ docker cp <container-name>:/var/run/mysqld/<database-record>.sql <path/to/folder/on/local/machine>

This could be useful to make a backup of the database.

## Shipping ScrApp to container

To build the container for the python3 app we are going to touch two files: a `Dockerfile` and a `.dockerignore`. 
In the latter, we are going to add every file of the folder but the `scrapp.py` and the `Modules` folder which contains the functions needed for the main program. 

The Dockerfile contains the followed content:
```
### Dockerfile for ScrApp.py
# base for the container
FROM python:3.8-alpine

# metadata
LABEL author="ninocan" maintainer="ninocangialosi@yahoo.it" 

# import the project files and move to the folder
# where they are located in the container
COPY . /app
WORKDIR /app
RUN mkdir Posters

# needed to avoid errors when installing lxml library
RUN apk add --update --no-cache g++ gcc libxslt-dev
# install dependencies
RUN pip install -r requirements.txt

#open port for connection
EXPOSE 5000

#launch the application
CMD ["python", "./scrapp.py"]

```
Let's comment on their function:

| COMMAND                | FUNCTION                                             | COMMENTS                                                                                                                                                                                                                         |
|------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FROM python:3.8-alpine | Fetches the base image from the dockerhub            | This should be the lightest base for python3.8, the package manager of alpine is `apk`                                                                                                                                           |
| LABEL  ...             | This includes metadata of the produced image         | We are just listing the author and the email for convinience                                                                                                                                                                     |
| COPY . app/            | Copies the files from locale to container            | Thanks to the dockerignore file we are only including the files of interest                                                                                                                                                      |
| WORKDIR /app           | Moves inside the folder of the application           | The container acts as independent filesystem, here is where we do the dirty job                                                                                                                                                  |
| RUN mkdir Posters      | Creates a new folder inside `/app`                   | We are not including Poster to the repo so we need to create it for the app to work properly                                                                                                                                     |
| RUN apk ...            | Installs g++ gcc libxslt-dev                         | First version of the dockerfile did not have this line and the building failed when installing lxml. This line fixes it. Source:  [stackoverflow](https://stackoverflow.com/questions/35931579/how-can-i-install-lxml-in-docker) |
| RUN pip install ...    | Installs the python dependencies for the application | This requires the creation of a `requirements.txt` file. Details below                                                                                                                                                           |
| EXPOSE 5000            | open port for external connection                    | Maybe not needed                                                                                                                                                                                                                 |
| CMD ...                | Launches the app                                   |                                                                                                                                                                                                                                  |
