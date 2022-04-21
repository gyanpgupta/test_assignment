# test_home_assignemnt
This repository contains the data from the csv file.
In this application user will upload the csv file in our system and the user will be able to get all the data in json response

# README
This README covers setup instructions for cloning the project and  running system locally.

## Clone the project
    $ git clone <url>

## Running the application locally

### Set the environment variables

Create the environment file from the template:

    $ cp .env.example .env

Create the postgres database in your local and Modify the variables in `.env` file:
- change the `DJANGO_SECRET_KEY`,
- change the `DATABASE_NAME`
- change the `DATABASE_USER`
- change the `DATABASE_PASSWORD`
- change the `DATABASE_HOST`
- change the `DATABASE_PORT`

## Run migrations:
    $ python manage.py makemigrations
    $ python manage.py migrate

## Run the django server:
    $ python manage.py runserver

## Run the API's:
   ### Go to your browser and hit these api's:
        This api will help you to uplaod the data from csv      
        - <your_domanin_name>/core/upload-csv/
        
        This api will help you to get the data in json response  
        - <your_domanin_name>/core/get-csv-file-data/
  
    
