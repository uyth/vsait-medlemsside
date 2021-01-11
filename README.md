<h1 align="center">VSAIT medlemsside</h1>

## Table of contents
- [Table of contents](#table-of-contents)
- [About the project](#about-the-project)
  - [Built with and using](#built-with-and-using)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Good-to-know commands](#good-to-know-commands)

## About the project
A membership management system for VSAiT that manages events and registrations for its members.

### Built with and using
- Django
- Python
- sqlite
- JQuery
- HTML5
- CSS3

## Getting started
To get a local copy up and running follow these simple steps.

### Prerequisites
- git
- python3

### Installation
1. Clone the repo

```sh
git clone https://github.com/uyth/vsait-medlemsside.git
```

2. Navigate into the folder and install required python libraries

```sh
cd vsait-medlemsside
pip3 install -r requirements.txt
```

3. Django version used is 2.2.10, create a virtualenv if there's conflict with django versions. (Skip this if never used django before)
```sh
virtualenv env
source env/bin/activate
```

4. Generate a new SECRET_KEY by writing the command under in a terminal and save it in a .txt file
```sh
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Example text file:
```
wz+-4!mgwv4cpku&h5=m@hogy6dse5+d*x3u!7%(#-4zzp8iq%
email@domain.com
write_email_password_here
```
Here `email@domain.com` and it's password respectively being the email that is going to send to confirm registrations and forgot password.

5. Navigate to `vsait-medlemsside/vsait` and change EMAIL_HOST and EMAIL_PORT to use the provided email domains SMTP server. (If needed, you might have to set either EMAIL_USE_SSL or EMAIL_USE_TLS to True)
```python
EMAIL_HOST = 'send.one.com'
EMAIL_PORT = 465
```

6. On the same file, change line 29 of `settings.py` to point to the location of the text file created at step 4
```python
with open('/home/juki/vsait_secret.txt') as f:
```

7. Navigate back to `vsait-medlemsside`

8. Run the server
```sh
python3 manage.py runserver
```

## Good-to-know commands

```sh
python3 -c "import django; print(django.__path__)" # Gets django path
python3 manage.py shell # Opens a python shell with API Django

# Migrations
python3 manage.py migrate
python3 manage.py makemigrations
```
