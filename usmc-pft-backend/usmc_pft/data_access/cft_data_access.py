from usmc_pft.models.cft_models import *
from usmc_pft.utilities.time_age import *
from usmc_pft.utilities.score_class import get_total_cft_score_and_class
from .common import get_cardio_event_score, get_strength_event_score

def get_cft_score(request_body: dict) -> dict:
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
    scores = {
        "mtc": get_cardio_event_score(age, gender, mtc_time, high_alt, Movement_Contact),
        "muf": get_cardio_event_score(age, gender, muf_time, high_alt, Maneuver_Fire),
        "ammo": get_strength_event_score(age, gender, int(ammo), Ammo_Lift)
    }

    scores["total"] = get_total_cft_score_and_class(scores)

    return scores
