import os, sys
import datetime

from flask import Flask
from flask import request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from helpers.parse_envars import AppSettings
from app.create_app import app, db

# # ----------------- models ---------------------------------------
# class Onesentence(db.Model):
#     __tablename = 'onesentence'
#
#     id           = db.Column(db.Integer, primary_key=True)
#     story        = db.Column(db.Text)
#     created_date = db.Column(db.DateTime(timezone=True))
#
#     def __init__(self, story):
#         self.story = story
#         self.created_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#
#     def __repr__(self):
#         return '<id {}: story{}>'.format(self.id, self.story)

# ----------------- views ---------------------------------------

# from handlers.add      import addStory
# from handlers.show_all import showAll
# from handlers.edit     import editStory
# from handlers.delete   import deleteStory
#
# @app.route('/')
# def index():
#     return redirect(url_for('stories', page=1))
#
# @app.route('/stories/page/<int:page>',methods=['GET'])
# def stories(page=1):
#     return showAll(page)
#
#
# @app.route('/add', methods=['GET','POST'])
# def add():
#     return addStory(db, request)
#
# @app.route('/edit/<int:id>', methods=['GET','POST'])
# def edit(id):
#     return editStory(db, request, id)
#
#
# @app.route('/delete/<int:id>', methods=['GET','POST'])
# def delete(id):
#     return deleteStory(db, request, id)
#
# @app.route('/confirm')
# def confirm():
#     return render_template('confirm.html')

########################################################################################################
########################################################################################################

if __name__ == '__main__':
    print("about to run the app...")
    app.run(port=os.environ['PORT'])