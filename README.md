# medlemmer.vsait.org

## Technology stack

* Heroku - Deployment
* Django - Backend
* PostgreSQL - Database
* React.js - Frontend

## Setting up a virtual environment

To be able to run the project you need python 3.6 or
 higher. To setup a virtual environment, make sure 
that you have `python3-venv` installed.

To setup a virtual environment, run the commands

    python -m venv env
    source env/bin/activate

To install the required modules, run the command

    pip install -r requirements.txt


## Local deployment

Local deployment is for test purposes. The local deployment
won't contain any real data from the actual Heroku server.

To make sure everything is ready to be deployed, we set up
a virtual environment and run the server.

Set up a virtual enironment as described in the previous chapter.
Then in the root folder, run the command

    python manage.py runserver


## Heroku Deployment

The Heroku application is connected to the Github master branch.
Every new commits to master will therefore be deployed by
Heroku. It is therefore important that you pull from master
before every pull request, and that everything works.

It is still possible to deploy your local code to Heroku
with the Heroku CLI.
To deploy your local code with Heroku CLI,
use the command

    git push heroku master

### Heroku App Configuration

Read more [here](https://devcenter.heroku.com/articles/django-app-configuration).

### Setting up a redirect from the host subdomain to the Heroku application

This section is about how you redirect the Heroku 
application from the heroku servers to your subdomain.
This only needs to be done once.

Run the command 
 
    heroku domains:add medlemmer.vsait.org

You will then get instructions and an address of the
form xxx-xxx-xxx.herokudns.com.

Add this in the DNS provider as CNAME. When this is done
run the command

    heroku domains:wait 'medlemmer.vsait.org'

The subdomain ´medlemmer.vsait.org´ will now link to the 
heroku application.
