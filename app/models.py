from app.app import db
import datetime

class Onesentence(db.Model):
    __tablename = 'onesentence'

    id           = db.Column(db.Integer, primary_key=True)
    story        = db.Column(db.Text)
    created_date = db.Column(db.DateTime(timezone=True))

    def __init__(self, story):
        self.story = story
        self.created_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<id {}: story{}>'.format(self.id, self.story)