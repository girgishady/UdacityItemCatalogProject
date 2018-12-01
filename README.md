# Item Catalog Project
Item catalog application is a pyhton application created to  provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Files in this project
* **"project.py"** python file that contain the application
* **"Database_setup.py"** python file to create the Database
* **"lotsofitems.py"** python file to create multiple categories and initial items
* **"client_secrets.json"** json file contain data for the authentication
* **"requirements.txt"** contain all application dependencies
* **"templates"** folder that contain html template files
* **"static"** folder that comtain css and images


## Prerequisite
* **Virtualbox** prefered version 5.1.30 from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* **Vagrant** prefered version 1.8.5 from [here](https://releases.hashicorp.com/vagrant/1.8.5/)
* **Udacity vagrant file** from [here](https://github.com/udacity/fullstack-nanodegree-vm)
* Existing **google+** account

## dependencies
This application depend on many python modules, its included in **requirements.txt** file and how you can install them in  **Quickstart** 
* flask==1.0.2
* packaging==18.0
* oauth2client==4.1.3
* redis==2.10.6
* passlib==1.7.1
* flask-httpauth==3.2.4
* sqlalchemy==1.2.12
* flask-sqlalchemy==2.3.2
* psycopg2-binary==2.7.5
* bleach==3.0.2
* requests==2.19.1

## Quickstart
To run this application:
* install **virtualbox** and **Vagrant**.
* Clone the **fullstack-nanodegree-vm**.
* Using your terminal application browse the folder that contain the vagrant configuration file.
* Launch the Vagrant VM `vagrant up` while you are in this folder.
* Add **"catalog"** folder after unzip it into **vagrant** folder.
* As this application has many dependencies, run the following command to download all dependencies `pip install -r requirements.txt`
* from your terminal run `python Database_setup.py` to create the Database.
* then run `python lotsofitems.py` to fill it with the initial items.
* then run `python project.py` to run the application
* finally use your browser to browse the application using http://localhost:5000

## Notes
In case you have error with `vagrant up` write the following command to your terminal `chcp.com 1252`


## License
**Item catalog** is a public domain work, Feel free to do whatever you want with it.