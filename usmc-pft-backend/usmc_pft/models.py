from usmc_pft import db, app

class Three_Mile(db.Model):
    __tablename__ = "three_mile"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    high_alt = db.Column(db.Boolean, unique=False, nullable=False)

class Row(db.Model):
    __tablename__ = "row"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    high_alt = db.Column(db.Boolean, unique=False, nullable=False)


class Crunches(db.Model):
    __tablename__ = "crunches"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)

class Plank(db.Model):
    __tablename__ = "plank"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    
class Pullups(db.Model):
    __tablename__ = "pullups"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    
class Pushups(db.Model):
    __tablename__ = "pushups"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    