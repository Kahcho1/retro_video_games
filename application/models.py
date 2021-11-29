from application import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gname = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    gdate = db.Column(db.DateTime(), nullable=False)
    console_id = db.Column(db.Integer, db.ForeignKey('console.id'), nullable=False)

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    cdescription = db.Column(db.String(120), nullable=False)
    cdate = db.Column(db.DateTime(), nullable=False)
    games = db.relationship('Games', backref='consoles')