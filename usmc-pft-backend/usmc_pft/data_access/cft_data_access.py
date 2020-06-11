from usmc_pft import app, db
from usmc_pft.models.cft_models import *
from usmc_pft.utilities.time_age import *
from usmc_pft.utilities.min_max_scores import *
from usmc_pft.utilities.score_class import get_total_cft_score_and_class

def get_cft_score(request_body):
    gender = request_body.get("gender")
    mtc = request_body.get("mtc")
    muf = request_body.get("muf")
    ammo = request_body.get("ammo")
    high_alt = request_body.get("high_alt") != "False"
    age = get_age_range(int(request_body.get("age")))

    mtc_time = get_time_to_seconds(mtc)
    muf_time = get_time_to_seconds(muf)

    # The CFT has no alternate events authorized. Each CFT calculation
    # must contain the same 3 events.
    scores = {"mtc": {}, "muf": {}, "ammo": {}}
        
    scores["mtc"]["score"] = get_cft_mtc(age, gender, mtc_time, high_alt)
    scores["mtc"]["max"] = 100
 
    scores["muf"]["score"] = get_cft_muf(age, gender, muf_time, high_alt)
    scores["muf"]["max"] = 100

    scores["ammo"]["score"] = get_cft_ammo(age, gender, int(ammo))
    scores["ammo"]["max"] = 100
    
    scores["total"] = get_total_cft_score_and_class(scores)
    return scores

def get_cft_mtc(age, gender, time, high_alt):
    if(faster_than_max_time(age, gender, time, high_alt, Movement_Contact)):
        return 100
    if(slower_than_min_time(age, gender, time, high_alt, Movement_Contact)):
        return 0
    event = Movement_Contact.query.filter((Movement_Contact.age == age)
                                        & (Movement_Contact.gender == gender)
                                        & (Movement_Contact.time == time)
                                        & (Movement_Contact.high_alt == high_alt)).first()
    return event.score

def get_cft_muf(age, gender, time, high_alt):
    if(faster_than_max_time(age, gender, time, high_alt, Maneuver_Fire)):
        return 100
    if(slower_than_min_time(age, gender, time, high_alt, Maneuver_Fire)):
        return 0
    event = Maneuver_Fire.query.filter((Maneuver_Fire.age == age)
                                        & (Maneuver_Fire.gender == gender)
                                        & (Maneuver_Fire.time == time)
                                        & (Maneuver_Fire.high_alt == high_alt)).first()
    return event.score

def get_cft_ammo(age, gender, reps):
    if(above_max_reps(age, gender, reps, Ammo_Lift)):
        return 100
    if(below_min_reps(age, gender, reps, Ammo_Lift)):
        return 0
    event = Ammo_Lift.query.filter((Ammo_Lift.age == age)
                                        & (Ammo_Lift.gender == gender)
                                        & (Ammo_Lift.reps == reps)).first()
    return event.score