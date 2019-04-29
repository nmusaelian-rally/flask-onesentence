from flask import render_template
from app.models import Onesentence
from helpers.encdec import decrypt_symmetric, PROJECT_ID, LOCATION_ID, KEY_RING_ID, CRYPTOKEY_ID


def showAll(page):
    per_page = 1
    sentences = Onesentence.query.order_by(Onesentence.id.desc()).paginate(page, per_page, error_out=True)
    decrypted_sentences = []
    for sentence in sentences.items:
        decrypted_story = decrypt_symmetric(PROJECT_ID, LOCATION_ID, KEY_RING_ID, CRYPTOKEY_ID, sentence.story)
        sentence.story = decrypted_story.decode()
        decrypted_sentences.append(sentence)

    return render_template('show_all.html', sentences=decrypted_sentences, page=page)


