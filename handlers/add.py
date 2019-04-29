from flask import render_template
from app.models import Onesentence
from helpers.encdec import encrypt_symmetric, PROJECT_ID, LOCATION_ID, KEY_RING_ID, CRYPTOKEY_ID

def addStory(db, request):
    if request.method == 'GET':
        return render_template('add.html')

    elif request.method == 'POST':
        story = request.form['story']
        encrypted = encrypt_symmetric(PROJECT_ID, LOCATION_ID, KEY_RING_ID, CRYPTOKEY_ID, story.encode())
        onesentence = Onesentence(encrypted)
        db.session.add(onesentence)
        db.session.commit()
        message = "Successfully added a story"
        return render_template('add_result.html', id=onesentence.id, message=message)