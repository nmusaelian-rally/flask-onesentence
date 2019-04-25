from app.appbase import app, db
from flask import request, redirect, url_for, render_template

from handlers.add import addStory
from handlers.show_all import showAll
from handlers.edit import editStory
from handlers.delete import deleteStory

@app.route('/')
def index():
    return redirect(url_for('stories', page=1))

@app.route('/stories/page/<int:page>',methods=['GET'])
def stories(page=1):
    return showAll(page)


@app.route('/add', methods=['GET','POST'])
def add():
    return addStory(db, request)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    return editStory(db, request, id)


@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    return deleteStory(db, request, id)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')