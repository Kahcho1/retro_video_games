from application import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gname = db.Column(db.String(30), nullable=True)
    grelease = db.Column(db.DateTime(), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    console = db.relationship("Console", backref="games")

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=True)
    crelease = db.Column(db.DateTime(), nullable=True)
    games_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)