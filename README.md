# start django project
1. create a folder and open it in visual studio
2. python -m venv venv
3. ./venv/Scripts/activate
4. pip install django
5. django-admin startproject [project_name - for example auction_proj] .
6. python manage.py startapp [app_name - for example auction]
7. python manage.py migrate
8. python manage.py createsuperuser

# start server
python manage.py runserver
