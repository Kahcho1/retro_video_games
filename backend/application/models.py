from application import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    consoles_id = db.Column(db.Integer, db.ForeignKey('console.id'), nullable=True)

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    console_name = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    games = db.relationship("Games", backref="console")