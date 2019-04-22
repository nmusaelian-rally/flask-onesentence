from flask import render_template
from app.models import Onesentence

def showAll(page):
    per_page = 1
    sentences = Onesentence.query.order_by(Onesentence.id.desc()).paginate(page, per_page, error_out=True)
    return render_template('show_all.html', sentences=sentences, page=page)

