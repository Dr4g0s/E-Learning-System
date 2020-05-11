# SETUP
    - pip install -r requirements.txt
    - Configure config/nginx.conf, config/uwsgi.ini with your paths
    - nano /etc/nginx/nginx.conf and Add 'include /home/dr4g0s/Desktop/E-Learning/config/nginx.conf;' to top of http
    - Add your setting file using command 'export DJANGO_SETTINGS_MODULE=educa.settings.pro' or edit it in manage.py file
    - create your own ssl certificate by command 
            'sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl/educa.key -out ssl/educa.crt'
    - Add your domain to /etc/hosts

# Run
    - uwsgi --ini config/uwsgi.ini
    - daphne -u /tmp/daphne.sock educa.asgi:application