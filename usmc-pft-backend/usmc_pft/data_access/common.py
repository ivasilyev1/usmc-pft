from __future__ import annotations
from typing import TYPE_CHECKING
from usmc_pft import app

if TYPE_CHECKING:
    from usmc_pft.models.cft_models import *
    from usmc_pft.models.pft_models import *

def get_cardio_event_score(
        age: int,
        gender:str,
        time: int,
        high_alt: bool,
        event: Three_Mile|Row|Movement_Contact|Maneuver_Fire
    ) -> dict:
    app.logger.info(f"Getting score correlating to time {time}s for {event.__name__}")
    faster_than_max, slower_than_min =_check_min_max_time(age, gender, time, high_alt, event)
    if (faster_than_max):
        app.logger.info(f"Time reported is above fastest possible. Returning a score of 100")
        score = event.max_score
    elif (slower_than_min):
        app.logger.info(f"Time reported is below minimum allowed. Returning a score of 0 as this event is considered failed")
        score = 0
    else:
        event_entry = event.query.filter((event.age == age)
                                         & (event.gender == gender)
                                         & (event.time == time)
                                         & (event.high_alt == high_alt)).first()

        score = event_entry.score
        app.logger.info(f"Retrieved score is {score} points")

    return {"score": score, "max": event.max_score}

def get_strength_event_score(
        age: int,
        gender: str,
        reps: int,
        event: Ammo_Lift|Crunches|Pullups|Pushups
    ) -> dict:
    app.logger.info(f"Getting score correlating to {reps} reps for {event.__name__}")
    more_than_max, below_min = _check_min_max_reps(age, gender, reps, event)
    if(more_than_max):
        app.logger.info(f"Reps are above most possible. Returning a score of 100")
        score = event.max_score
    elif(below_min):
        app.logger.info(f"Reps are below minimum allowed. Returning a score of 0 as this event is considered failed")
        score = 0
    else:
        event_entry = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.reps == reps)).first()

        score = event_entry.score
        app.logger.info(f"Retrieved score is {score} points")

    return {"score": score, "max": event.max_score}


def _check_min_max_reps(
        age: int,
        gender: str,
        reps: int,
        event: Ammo_Lift|Crunches|Pullups|Pushups
    ) -> tuple:
    app.logger.info(f"Checking if {reps} reps is above max possible or below min required for event {event.__name__}")
    min_max = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.score.in_((event.max_score, event.min_score)))
                                   ).order_by(event.score.desc()).all()

    max_score = min_max[0]
    min_score = min_max[1]

    return (reps > max_score.reps, reps < min_score.reps)

def _check_min_max_time(
        age: int,
        gender: str,
        time: int,
        high_alt: bool,
        event: Three_Mile|Row|Movement_Contact|Maneuver_Fire
    ) -> tuple:
    app.logger.info(f"Checking if {time}s is above fastest possible or below slowest allowed for event {event.__name__}")
    min_max = event.query.filter((event.age == age)
                                & (event.gender == gender)
                                & (event.high_alt == high_alt)
                                & (event.score.in_((event.max_score, event.min_score)))
                                ).order_by(event.score.desc()).all()

    max_score = min_max[0]
    min_score = min_max[1]

    return (time < max_score.time, time > min_score.time)
