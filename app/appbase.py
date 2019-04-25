import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.secret_key = os.environ["APP_SECRET"]
app.secret_key = "whitershadeofpale"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

try:
    db.session.execute("SELECT 1")
    print("got result from query of SELECT 1 ...")
except Exception as ex:
    print("problem with d.session.execute", ex)

