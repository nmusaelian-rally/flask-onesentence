from app.create_app import db
import datetime

class Onesentence(db.Model):
    __tablename = 'onesentence'

    id           = db.Column(db.Integer, primary_key=True)
    story        = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime(timezone=True))

    def __init__(self, story, title):
        self.story = story
        self.created_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<id {}: story{}>'.format(self.id, self.story)