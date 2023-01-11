# this project is my first python django app

## create virtual env

python -m venv tutorial-env

## create project

django-admin startproject chefsTable

## create app inside project

django-admin startapp LittleLemon

## Run App by starting manage.py in project filter

python manage.py runserver

## CREATE A MODEL AND MAKE A MIGRATION and them migrate it to apply model to the database

python manage.py makemigrations

python manage.py migrate

## for using template 
you need to add your project template path to the settings.py 's "TEMPLATES = []" and remember to return the view's render like this "render(req, 'form.html', context)"
