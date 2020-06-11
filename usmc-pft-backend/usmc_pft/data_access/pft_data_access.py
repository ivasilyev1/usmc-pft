from usmc_pft import app, db
from usmc_pft.models.pft_models import *
from usmc_pft.utilities.time_age import *
from usmc_pft.utilities.min_max_scores import *
from usmc_pft.utilities.score_class import get_total_pft_score_and_class

def get_pft_score(request_body):
    gender = request_body.get("gender")
    run = request_body.get("run")
    row = request_body.get("row")
    pullups = request_body.get("pullups")
    pushups = request_body.get("pushups")
    crunches = request_body.get("crunches")
    plank = request_body.get("plank")
    high_alt = request_body.get("high_alt") != "False"

    age = get_age_range(int(request_body.get("age")))
    run_row_time = get_run_row_time_to_seconds(run, row)

    # There are 2 events that can be taken for each PFT event
    # category (cardio, abdominal, upper-body), resulting in 6
    # possible events that must be accounted for.
    scores = {}
    if(run is not None):
        scores["run"] = {}
        scores["run"]["score"] = get_pft_run(
            age, gender, run_row_time, high_alt)
        scores["run"]["max"] = 100
    if(row is not None):
        scores["row"] = {}
        scores["row"]["score"] = get_pft_row(
            age, gender, run_row_time, high_alt)
        scores["row"]["max"] = 100
    if(pullups is not None):
        scores["pullups"] = {}
        scores["pullups"]["score"] = get_pft_pullups(age, gender, int(pullups))
        scores["pullups"]["max"] = 100
    if(pushups is not None):
        scores["pushups"] = {}
        scores["pushups"]["score"] = get_pft_pushups(age, gender, int(pushups))
        # Can not get more than 70 points for pushups, regardless of reps.
        scores["pushups"]["max"] = 70
    if(crunches is not None):
        scores["crunches"] = {}
        scores["crunches"]["score"] = get_pft_crunches(
            age, gender, int(crunches))
        scores["crunches"]["max"] = 100
    if(plank is not None):
        # The Plank event uses the same calculation for all ages, so using 17 for simplicity.
        age = 17
        plank_time = get_time_to_seconds(plank)
        scores["plank"] = {}
        scores["plank"]["score"] = get_pft_plank(age, gender, plank_time)
        scores["plank"]["max"] = 100
    scores["total"] = get_total_pft_score_and_class(scores)
    return scores

def get_pft_run(age, gender, time, high_alt):
    if(faster_than_max_time(age, gender, time, high_alt, Three_Mile)):
        return 100
    if(slower_than_min_time(age, gender, time, high_alt, Three_Mile)):
        return 0
    event = Three_Mile.query.filter((Three_Mile.age == age)
                                    & (Three_Mile.gender == gender)
                                    & (Three_Mile.time == time)
                                    & (Three_Mile.high_alt == high_alt)).first()
    return event.score

def get_pft_row(age, gender, time, high_alt):
    if(faster_than_max_time(age, gender, time, high_alt, Row)):
        return 100
    if(slower_than_min_time(age, gender, time, high_alt, Row)):
        return 0
    event = Row.query.filter((Row.age == age)
                             & (Row.gender == gender)
                             & (Row.time == time)
                             & (Row.high_alt == high_alt)).first()
    return event.score

def get_pft_pullups(age, gender, reps):
    if(above_max_reps(age, gender, reps, Pullups)):
        return 100
    if(below_min_reps(age, gender, reps, Pullups)):
        return 0
    event = Pullups.query.filter((Pullups.age == age)
                                 & (Pullups.gender == gender)
                                 & (Pullups.reps == reps)).first()
    return event.score

def get_pft_pushups(age, gender, reps):
    if(above_max_reps(age, gender, reps, Pushups)):
        return 70
    if(below_min_reps(age, gender, reps, Pushups)):
        return 0
    event = Pushups.query.filter((Pushups.age == age)
                                 & (Pushups.gender == gender)
                                 & (Pushups.reps == reps)).first()
    return event.score

def get_pft_crunches(age, gender, reps):
    if(above_max_reps(age, gender, reps, Crunches)):
        return 100
    if(below_min_reps(age, gender, reps, Crunches)):
        return 0
    event = Crunches.query.filter((Crunches.age == age)
                                  & (Crunches.gender == gender)
                                  & (Crunches.reps == reps)).first()
    return event.score

def get_pft_plank(age, gender, time):
    if(longer_than_max_plank(age, gender, time)):
        return 100
    if(shorter_than_min_plank(age, gender, time)):
        return 0
    actual_event = Plank.query.filter((Plank.age == age)
                                      & (Plank.gender == gender)
                                      & (Plank.time == time)).first()
    
    # Per USMC order, plank times correlate to a score every 3rd or 4th second (arbitrarily).
    # This means that a submitted time can fall exactly on an existing time correlation OR can
    # fall somewhere between 2 time correlations. Since there is no way to predict if the time falls
    # on the 3rd or 4th second, the time is queried for the 1st occuring score correlation that is
    # less than the submitted time (rounded down against the event taker's favor).
    # See: https://www.marines.mil/News/Messages/MARADMINS/Article/1869148/forthcoming-change-to-the-physical-fitness-test-pft/
    if(actual_event):
        return actual_event.score

    event_below = Plank.query.filter((Plank.age == age)
                                     & (Plank.gender == gender)
                                     & (Plank.time < time)).order_by(Plank.time.desc()).first()
    return event_below.score