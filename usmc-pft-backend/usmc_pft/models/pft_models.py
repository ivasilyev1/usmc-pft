from usmc_pft import db

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import case

class Three_Mile(db.Model):
    __tablename__ = "three_mile"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    high_alt = db.Column(db.Boolean, unique=False, nullable=False)
    max_score = 100
    min_score = 40

class Row(db.Model):
    __tablename__ = "row"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    high_alt = db.Column(db.Boolean, unique=False, nullable=False)
    max_score = 100
    min_score = 40


class Crunches(db.Model):
    __tablename__ = "crunches"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    max_score = 100
    min_score = 40

class Plank(db.Model):
    __tablename__ = "plank"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    max_score = 100
    min_score = 40

class Pullups(db.Model):
    __tablename__ = "pullups"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    max_score = 100

    # Per USMC order, the minimum number of points a female can get on pullups is 60.
    # Minimum number of points a Male can get on pullups is 40.
    @hybrid_property
    def min_score(self):
        if self.gender == 'F':
            return 60
        else:
            return 40

    @min_score.expression
    def min_score(cls):
        return case([
                    (cls.gender == 'F', 60),
                    ], else_ = 40)

class Pushups(db.Model):
    __tablename__ = "pushups"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    reps = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    max_score = 70
    min_score = 40