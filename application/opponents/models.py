from application import db

class Opponent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    year_of_birth = db.Column(db.Integer, nullable=True)
    strengths = db.Column(db.String(10000), nullable=True)
    weaknesses = db.Column(db.String(10000), nullable=True)

    def __init__(self, name):
        self.name = name