import os, sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from helpers.parse_envars import AppSettings

app = Flask(__name__, template_folder="templates")
[AppSettings.loadEnvironment(app_file) for app_file in sys.argv[1:]]
app.secret_key = os.environ["APP_SECRET"]
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

try:
    db.session.execute("SELECT 1")
    print("got result from query of SELECT 1 ...")
except Exception as ex:
    print("problem with d.session.execute", ex)


