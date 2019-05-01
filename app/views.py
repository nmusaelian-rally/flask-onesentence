import os
import subprocess
import re

from app.appbase import app, db
from flask import request, redirect, url_for, render_template, g

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

@app.route('/healthcheck')
def healthCheck():
    return "The service is operating normally"

@app.route('/shutdown')
def shutdown():
    os.system("nginx -s quit")
    print('{"message": "nginx shut down"}')
    if db and db.session:
        db.session.remove()
        print('{"message": "db session removed"}')
    completed_process = subprocess.run(["ps", "-ef"], capture_output=True)
    ps_out = completed_process.stdout.decode()
    target_procs = [proc for proc in ps_out.split("\n") if re.search('cloud_sql_proxy', proc)]
    if target_procs:
        csp_item = target_procs.pop(0)
        fields = re.split('\s+', csp_item)
        csp_pid = fields[1]
        os.system("kill -s QUIT %s" % csp_pid)
        print('{"message": "cloud_sql_proxy shut down"}')
    try:
        print('{"message": "uwsgi shutting down"}')
        os.system("uwsgi --stop /run/uwsgi.pid")
    except:
        pass
    message = "shutdown complete"
    print('{"message": "%s"}' % message)
    return message
