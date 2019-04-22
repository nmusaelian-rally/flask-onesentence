from flask import render_template
from app.models import Onesentence

def addStory(db, request):
    if request.method == 'GET':
        return render_template('add.html')

    elif request.method == 'POST':
        story = request.form['story']
        onesentence = Onesentence(story)
        db.session.add(onesentence)
        db.session.commit()
        message = "Successfully added a story"
        return render_template('add_result.html', id=onesentence.id, message=message)