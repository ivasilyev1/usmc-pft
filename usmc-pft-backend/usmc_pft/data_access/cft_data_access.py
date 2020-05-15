from usmc_pft import app, db
from usmc_pft.models.cft_models import *
from usmc_pft.utilities.usmc_utilities import *

def get_cft_score(request_body):
    gender = request_body.get("gender")
    mtc = request_body.get("mtc")
    muf = request_body.get("muf")
    ammo = request_body.get("ammo")
    high_alt = request_body.get("high_alt") != "False"
    age = get_age_range(int(request_body.get("age")))

    mtc_time = get_time_to_seconds(mtc)
    muf_time = get_time_to_seconds(muf)

    scores = {"mtc": {}, "muf": {}, "ammo": {}}
        
    scores["mtc"]["score"] = get_cft_mtc(age, gender, mtc_time, high_alt)
    scores["mtc"]["max"] = 100
 
    scores["muf"]["score"] = get_cft_muf(age, gender, muf_time, high_alt)
    scores["muf"]["max"] = 100

    scores["ammo"]["score"] = get_cft_ammo(age, gender, int(ammo))
    scores["ammo"]["max"] = 100
    
    scores["total"] = get_total_cft_score_and_class(scores)
    return scores

def above_max_mtc(age, gender, time, high_alt):
    max_score = Movement_Contact.query.filter((Movement_Contact.age == age)
                                            & (Movement_Contact.gender == gender)
                                            & (Movement_Contact.high_alt == high_alt)
                                            & (Movement_Contact.score == 100)).first()
    return time < max_score.time

def below_min_mtc(age, gender, time, high_alt):
    min_score = Movement_Contact.query.filter((Movement_Contact.age == age)
                                            & (Movement_Contact.gender == gender)
                                            & (Movement_Contact.high_alt == high_alt)
                                            & (Movement_Contact.score == 40)).first()
    return time > min_score.time

def get_cft_mtc(age, gender, time, high_alt):
    if(above_max_mtc(age, gender, time, high_alt)):
        return 100
    if(below_min_mtc(age, gender, time, high_alt)):
        return 0
    event = Movement_Contact.query.filter((Movement_Contact.age == age)
                                        & (Movement_Contact.gender == gender)
                                        & (Movement_Contact.time == time)
                                        & (Movement_Contact.high_alt == high_alt)).first()
    return event.score


def above_max_muf(age, gender, time, high_alt):
    max_score = Maneuver_Fire.query.filter((Maneuver_Fire.age == age)
                                            & (Maneuver_Fire.gender == gender)
                                            & (Maneuver_Fire.high_alt == high_alt)
                                            & (Maneuver_Fire.score == 100)).first()
    return time < max_score.time

def below_min_muf(age, gender, time, high_alt):
    min_score = Maneuver_Fire.query.filter((Maneuver_Fire.age == age)
                                            & (Maneuver_Fire.gender == gender)
                                            & (Maneuver_Fire.high_alt == high_alt)
                                            & (Maneuver_Fire.score == 40)).first()
    return time > min_score.time

def get_cft_muf(age, gender, time, high_alt):
    if(above_max_muf(age, gender, time, high_alt)):
        return 100
    if(below_min_muf(age, gender, time, high_alt)):
        return 0
    event = Maneuver_Fire.query.filter((Maneuver_Fire.age == age)
                                        & (Maneuver_Fire.gender == gender)
                                        & (Maneuver_Fire.time == time)
                                        & (Maneuver_Fire.high_alt == high_alt)).first()
    return event.score

def above_max_ammo(age, gender, ammo_reps):
    max_score = Ammo_Lift.query.filter((Ammo_Lift.age == age)
                                        & (Ammo_Lift.gender == gender)
                                        & (Ammo_Lift.score == 100)).first()
    return ammo_reps > max_score.reps

def below_min_ammo(age, gender, ammo_reps):
    min_score = Ammo_Lift.query.filter((Ammo_Lift.age == age)
                                         & (Ammo_Lift.gender == gender)
                                         & (Ammo_Lift.score == 40)).first()
    return ammo_reps < min_score.reps

def get_cft_ammo(age, gender, pullups):
    if(above_max_ammo(age, gender, pullups)):
        return 100
    if(below_min_ammo(age, gender, pullups)):
        return 0
    event = Ammo_Lift.query.filter((Ammo_Lift.age == age)
                                        & (Ammo_Lift.gender == gender)
                                        & (Ammo_Lift.reps == pullups)).first()
    return event.score