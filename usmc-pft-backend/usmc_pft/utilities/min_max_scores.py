
from usmc_pft.models.cft_models import *
from usmc_pft.models.pft_models import *

def faster_than_max_time(age, gender, time, high_alt, event):
    max_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.high_alt == high_alt)
                                   & (event.score == 100)).first()
    return time < max_score.time

def slower_than_min_time(age, gender, time, high_alt, event):
    min_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.high_alt == high_alt)
                                   & (event.score == 40)).first()
    return time > min_score.time

# Plank time is calculated in "reverse", where a longer time
# correlates to a higher score. Can't rely on the previous two
# methods used for run/row/movement times.
def longer_than_max_plank(age, gender, time):
    max_score = Plank.query.filter((Plank.age == age)
                                   & (Plank.gender == gender)
                                   & (Plank.score == 100)).first()
    return time > max_score.time

def shorter_than_min_plank(age, gender, time):
    min_score = Plank.query.filter((Plank.age == age)
                                   & (Plank.gender == gender)
                                   & (Plank.score == 40)).first()
    return time < min_score.time

def above_max_reps(age, gender, reps, event):
    max_points = 70 if event == Pushups else 100
    max_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.score == max_points)).first()
    return reps > max_score.reps

def below_min_reps(age, gender, reps, event):
    # Per USMC order, the minimum number of points a female can get on pullups is 60.
    # Minimum number of points a Male can get on pullups is 40.
    if(event == Pullups):
        min_allowed = 60 if gender == "F" else 40
        min_score = Pullups.query.filter((Pullups.age == age)
                                         & (Pullups.gender == gender)
                                         & (Pullups.score == min_allowed)).first()
        return reps < min_score.reps
    min_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.score == 40)).first()
    return reps < min_score.reps