# [vsaIT] - Welcome to Jonny's reign

## Technology stack

- Heroku - Deployment
- Django - Framework
- Sqlite3 - Serverless - database

### Plan
```
/
/events/id
/<signup>
/profile/
```

### Setup

```
virtualenv env
source env/bin/activate

pip3 install -r requirements.txt

python manage.py runserver
python manage.py shell
```

### Migration

```
python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
```

### Get Django path

```
python -c "import django; print(django.__path__)"
```
