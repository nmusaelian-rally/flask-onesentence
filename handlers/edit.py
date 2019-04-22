from flask import render_template
from app.models import Onesentence

def editStory(db, request, id):
    onesentence = Onesentence.query.get(id)
    if request.method == 'GET':
        story = onesentence.story
        return render_template('add.html', id=id, story=story)
    elif request.method == 'POST':
        story = request.form['story']
        onesentence = Onesentence.query.get(id)
        onesentence.story = story
        db.session.commit()
        db.session.flush()
        message = "Successfully updated story"
        return render_template('add_result.html', id=id, message=message)