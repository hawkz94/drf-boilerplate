#!/bin/bash

echo 'Iniciando deploy...'
ssh IPSERVER << EOF
cd drf-boilerplate;
git pull origin master;
source venv/bin/activate;
pip install -r requirements/base.txt;
cd src/
python3.5 manage.py makemigrations --settings=settings.production;
python3.5 manage.py migrate --settings=settings.production;
# python3.5 manage.py collectstatic --settings=settings.production;
# yes;
kill -9 $(lsof -i:8000 -t) 2> /dev/null;
gunicorn --bind 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=settings.production wsgi --daemon; 
echo 'DONE!'
EOF

