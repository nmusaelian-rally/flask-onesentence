#!/bin/bash

echo "Running the nginx + uwsgi + flask triumvirate"
chmod 755 ./cloud_sql_proxy
./cloud_sql_proxy -instances=saas-rally-dev:us-west2:yogi-berra -dir=/cloudsql &
sleep 5
echo `ps -ef | grep cloud`
nginx && uwsgi --ini wsgi.ini -w run