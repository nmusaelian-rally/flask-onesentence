from app.appbase import db
import datetime

class Onesentence(db.Model):
    __tablename__ = 'onesentence'

    id           = db.Column(db.Integer, primary_key=True)
    story        = db.Column(db.Text, nullable=False)
    stars        = db.Column(db.Integer)
    created_date = db.Column(db.DateTime(timezone=True))

    def __init__(self, story, stars=5):
        self.story = story
        self.stars = stars
        self.created_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<id {}: story{}>'.format(self.id, self.story, self.stars)



