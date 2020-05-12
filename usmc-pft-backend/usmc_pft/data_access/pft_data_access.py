from usmc_pft import app, db
from usmc_pft.models import *
from usmc_pft.utilities.usmc_utilities import *
   
def get_pft_score(request_body):
    gender = request_body.get("gender")
    run = request_body.get("run")
    row = request_body.get("row")
    pullups = request_body.get("pullups")
    pushups = request_body.get("pushups")
    crunches = request_body.get("crunches")
    plank = request_body.get("plank")
    high_alt = request_body.get("high_alt") != "False"
    age = get_age_range(request_body.get("age"))

    run_row_time = get_run_row_time_to_seconds(run, row)

    scores = {}
    scores["events"] = []
    if(run is not None):
        scores["events"].append("Three Mile Run")
        scores["Three Mile Run"] = get_pft_run(age, gender, run_row_time, high_alt)
    if(row is not None):
        scores["events"].append("Five Km Row")
        scores["Five Km Row"] = get_pft_row(age, gender, run_row_time, high_alt)
    if(pullups is not None):
        scores["events"].append("Pullups")
        scores["Pullups"] = get_pft_pullups(age, gender, int(pullups))
    if(pushups is not None):
        scores["events"].append("Pushups")
        scores["Pushups"] = get_pft_pushups(age, gender, int(pushups))
    if(crunches is not None):
        scores["events"].append("Crunches")
        scores["Crunches"] = get_pft_crunches(age, gender, int(crunches))
    if(plank is not None):
        age = 17
        plank_time = get_plank_time_to_seconds(plank)
        scores["events"].append("Plank")
        scores["Plank"] = get_pft_plank(age, gender, plank_time)
    scores["total"] = get_total_pft_score_and_class(scores)
    return scores

def above_max_run(age, gender, time, high_alt):
    max_score = Three_Mile.query.filter((Three_Mile.age == age)
                                            & (Three_Mile.gender == gender)
                                            & (Three_Mile.high_alt == high_alt)
                                            & (Three_Mile.score == 100)).first()
    return time < max_score.time

def above_max_row(age, gender, time, high_alt):
    max_score = Row.query.filter((Row.age == age)
                                            & (Row.gender == gender)
                                            & (Row.high_alt == high_alt)
                                            & (Row.score == 100)).first()
    return time < max_score.time

def below_min_run(age, gender, time, high_alt):
    min_score = Three_Mile.query.filter((Three_Mile.age == age)
                                            & (Three_Mile.gender == gender)
                                            & (Three_Mile.high_alt == high_alt)
                                            & (Three_Mile.score == 40)).first()
    return time > min_score.time

def below_min_row(age, gender, time, high_alt):
    min_score = Row.query.filter((Row.age == age)
                                            & (Row.gender == gender)
                                            & (Row.high_alt == high_alt)
                                            & (Row.score == 40)).first()
    return time > min_score.time
    
def get_pft_run(age, gender, time, high_alt):
    if(above_max_run(age, gender, time, high_alt)):
        return 100
    if(below_min_run(age, gender, time, high_alt)):
        return 0
    event = Three_Mile.query.filter((Three_Mile.age == age)
                                        & (Three_Mile.gender == gender)
                                        & (Three_Mile.time == time)
                                        & (Three_Mile.high_alt == high_alt)).first()
    return event.score

def get_pft_row(age, gender, time, high_alt):
    if(above_max_row(age, gender, time, high_alt)):
        return 100
    if(below_min_row(age, gender, time, high_alt)):
        return 0
    event =  Row.query.filter((Row.age == age)
                                  & (Row.gender == gender)
                                  & (Row.time == time)
                                  & (Row.high_alt == high_alt)).first()
    return event.score

def above_max_pullups(age, gender, pullups):
    max_score = Pullups.query.filter((Pullups.age == age)
                                        & (Pullups.gender == gender)
                                        & (Pullups.score == 100)).first()
    return pullups > max_score.reps

def below_min_pullups(age, gender, pullups):
    min_allowed = 60 if gender == "F" else 40
    min_score = Pullups.query.filter((Pullups.age == age)
                                         & (Pullups.gender == gender)
                                         & (Pullups.score == min_allowed)).first()
    return pullups < min_score.reps

def get_pft_pullups(age, gender, pullups):
    if(above_max_pullups(age, gender, pullups)):
        return 100
    if(below_min_pullups(age, gender, pullups)):
        return 0
    event = Pullups.query.filter((Pullups.age == age)
                                        & (Pullups.gender == gender)
                                        & (Pullups.reps == pullups)).first()
    return event.score

def above_max_pushups(age, gender, pushups):
    max_score = Pushups.query.filter((Pushups.age == age)
                                        & (Pushups.gender == gender)
                                        & (Pushups.score == 70)).first()
    return pushups > max_score.reps

def below_min_pushups(age, gender, pushups):
    min_score = Pushups.query.filter((Pushups.age == age)
                                         & (Pushups.gender == gender)
                                         & (Pushups.score == 40)).first()
    return pushups < min_score.reps

def get_pft_pushups(age, gender, pushups):
    if(above_max_pushups(age, gender, pushups)):
        return 70
    if(below_min_pushups(age, gender, pushups)):
        return 0
    event = Pushups.query.filter((Pushups.age == age)
                                        & (Pushups.gender == gender)
                                        & (Pushups.reps == pushups)).first()
    return event.score

def above_max_crunches(age, gender, crunches):
    max_score = Crunches.query.filter((Crunches.age == age)
                                        & (Crunches.gender == gender)
                                        & (Crunches.score == 100)).first()
    return crunches > max_score.reps

def below_min_crunches(age, gender, crunches):
    min_score = Crunches.query.filter((Crunches.age == age)
                                         & (Crunches.gender == gender)
                                         & (Crunches.score == 40)).first()
    return crunches < min_score.reps

def get_pft_crunches(age, gender, crunches):
    if(above_max_crunches(age, gender, crunches)):
        return 100
    if(below_min_crunches(age, gender, crunches)):
        return 0
    event = Crunches.query.filter((Crunches.age == age)
                                        & (Crunches.gender == gender)
                                        & (Crunches.reps == crunches)).first()
    return event.score

def above_max_plank(age, gender, time):
    max_score = Plank.query.filter((Plank.age == age)
                                        & (Plank.gender == gender)
                                        & (Plank.score == 100)).first()
    return time > max_score.time

def below_min_plank(age, gender, time):
    min_score = Plank.query.filter((Plank.age == age)
                                         & (Plank.gender == gender)
                                         & (Plank.score == 40)).first()
    return time < min_score.time

def get_pft_plank(age, gender, time):
    if(above_max_plank(age, gender, time)):
        return 100
    if(below_min_plank(age, gender, time)):
        return 0
    actual_event = Plank.query.filter((Plank.age == age)
                                          & (Plank.gender == gender)
                                          & (Plank.time == time)).first()
    if(actual_event):
        return actual_event.score

    event_below = Plank.query.filter((Plank.age == age)
                                         & (Plank.gender == gender)
                                         & (Plank.time < time)).order_by(Plank.time.desc()).first()
    return event_below.score