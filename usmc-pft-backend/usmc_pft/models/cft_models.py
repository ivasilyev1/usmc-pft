from usmc_pft import app, db

class Movement_Contact(db.Model):
    __tablename__ = "movement_contact"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    high_alt = db.Column(db.Boolean, unique=False, nullable=False)

class Maneuver_Fire(db.Model):
    __tablename__ = "maneuver_fire"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    high_alt = db.Column(db.Boolean, unique=False, nullable=False)

class Ammo_Lift(db.Model):
    __tablename__ = "ammo_lift"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)