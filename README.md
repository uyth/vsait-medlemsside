# [vsaIT] - Welcome to Jonny's reign

### Plan

```
/
/events/<id>
/signup
/profile
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
python manage.py makemigrations
python manage.py sqlmigrate
```

### Get Django path

```
python -c "import django; print(django.__path__)"
```
