from flask import render_template, redirect, url_for
from app.models import Onesentence

def deleteStory(db, request, id):
    onesentence = Onesentence.query.get(id)
    if request.method == 'POST':
        story = onesentence.story
        db.session.delete(onesentence)
        db.session.commit()
        return redirect(url_for('confirm', story=story))
    return render_template('delete.html', onesentence=onesentence, id=id)
