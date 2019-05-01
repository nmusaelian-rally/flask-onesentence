import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv("APP_SECRET")

def dburl(template):
    replaceables = ['db_user', 'db_password', 'db_name', 'gcp_project', 'gcp_zone', 'gcloud_sql_instance']
    environ_vars = ['DB_USER', 'DB_PASSWORD', 'DB_NAME', 'PROJECT_ID',  'GCP_ZONE', 'GCLOUD_SQL_INSTANCE']
    result = template
    for target, jewel in zip(replaceables, environ_vars):
        result = result.replace("{%s}" % target, os.getenv(jewel))
    return result

app.config['SQLALCHEMY_DATABASE_URI'] = dburl(os.getenv('TEMPLATE_DATABASE_URL'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

try:
    db.session.execute("SELECT 1")
    print("got result from query of SELECT 1 ...")
except Exception as ex:
    print("problem with d.session.execute", ex)

