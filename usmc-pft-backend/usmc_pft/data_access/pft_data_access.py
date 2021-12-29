from usmc_pft import app
from usmc_pft.models.pft_models import *
from usmc_pft.utilities.time_age import *
from usmc_pft.utilities.score_class import get_total_pft_score_and_class
from .common import get_cardio_event_score, get_strength_event_score

def get_pft_score(request_body: dict) -> dict:
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
    if(run):
        scores["run"] = get_cardio_event_score(age, gender, run_row_time, high_alt, Three_Mile)
    if(row):
        scores["row"] = get_cardio_event_score(age, gender, run_row_time, high_alt, Row)
    if(pullups):
        scores["pullups"] = get_strength_event_score(age, gender, int(pullups), Pullups)
    if(pushups):
        scores["pushups"] = get_strength_event_score(age, gender, int(pushups), Pushups)
    if(crunches):
        scores["crunches"] = get_strength_event_score(age, gender, int(crunches), Crunches)
    if(plank):
        # The Plank event uses the same calculation for all ages, so using 17 for simplicity.
        age = 17
        plank_time = get_time_to_seconds(plank)
        scores["plank"] = get_pft_plank(age, gender, plank_time)

    scores["total"] = get_total_pft_score_and_class(scores)

    return scores

def get_pft_plank(age: int, gender: str, time: int) -> dict:
    app.logger.info(f"Getting score correlated to {time}s for Plank")
    longer_than_max, shorter_than_min = _check_min_max_plank(age, gender, time)
    if(longer_than_max):
        app.logger.info("Plank held above longest possible. Returning a score of 100")
        score = Plank.max_score
    elif(shorter_than_min):
        app.logger.info("Plank held below shortest allowed. Returning a score of 0 as this event is considered failed")
        score = 0
    else:
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
            score = actual_event.score
        else:
            event_below = Plank.query.filter((Plank.age == age)
                                     & (Plank.gender == gender)
                                     & (Plank.time < time)).order_by(Plank.time.desc()).first()
            score = event_below.score

        app.logger.info(f"Retrieved score is {score} points")

    return {"score": score, "max": Plank.max_score}


def _check_min_max_plank(age: int, gender: str, time: int) -> tuple:
    app.logger.info(f"Checking if {time}s is above longest possible or below minimum required for event Plank")
    min_max = Plank.query.filter((Plank.age == age)
                                   & (Plank.gender == gender)
                                   & (Plank.score.in_((Plank.max_score, Plank.min_score)))
                                   ).order_by(Plank.score.desc()).all()

    max_score = min_max[0]
    min_score = min_max[1]

    # Plank time is calculated in "reverse", where a longer time
    # correlates to a higher score
    return (time > max_score.time, time < min_score.time)
