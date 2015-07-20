#!/bin/sh
chown django /static
chown django /media
su -m django -c "python /app/manage.py collectstatic --noinput"
su -m django -c "/usr/local/bin/uwsgi --socket :5000 --wsgi-file /app/config/wsgi.py --master --processes 4 --threads 2 --chdir /app"