# test_home_assignemnt
This repository contains the data from the csv file.
In this application user will upload the csv file in our system and the user will be able to get all the data in json response

# README
This README covers setup instructions for cloning the project and  running system locally.

## Clone the project
    $ git clone https://github.com/gyanpgupta/test_assignment.git

## Running the application on local/staging/production

### Set the environment variables

Create the environment file from the template:

    $ cp development.env .env  ## if you run project locally
    $ cp staging.env .env      ## if you run the project in staging environment
    $ cp production.env .env  ## if you run the project in production environment

Create the postgres database in your environment and Modify the variables in `.env` file and also add your domain name in `ALLOWED_HOST` variable:
- change the `DATABASE_NAME`
- change the `DATABASE_USER`
- change the `DATABASE_PASSWORD`
- change the `DATABASE_HOST`
- change the `DATABASE_PORT`
- change the `ALLOWED_HOST`

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

## Upload csv from browser:
* you just simply need to write the domain name in your browser then you will see the UI where you can directly upload your csv file also check your uploaded data in a tabular form