from usmc_pft import app

def get_total_pft_score_and_class(scores: dict) -> dict:
    app.logger.info("Calculating total PFT score and class")
    cardio_event = "run" if "run" in scores.keys() else "row"
    ab_event = "crunches" if "crunches" in scores.keys() else "plank"
    strength_event = "pullups" if "pullups" in scores.keys() else "pushups"

    cardio = scores[cardio_event]["score"]
    abdominal = scores[ab_event]["score"]
    upper_body = scores[strength_event]["score"]

    auto_fail = 0 in [cardio, abdominal, upper_body]
    total = cardio + abdominal + upper_body

    return {
        "score": total,
        "eventClass": get_pft_cft_class(total, auto_fail)
    }

def get_total_cft_score_and_class(scores):
    app.logger.info("Calculating total CFT score and class")
    mtc = scores["mtc"]["score"]
    muf = scores["muf"]["score"]
    ammo = scores["ammo"]["score"]

    auto_fail = 0 in [mtc, muf, ammo]
    total = mtc + muf + ammo

    return {
        "score": total,
        "eventClass": get_pft_cft_class(total, auto_fail)
    }

def get_pft_cft_class(score, auto_fail):
    if(score < 150 or auto_fail):
        return 0
    if(score >= 235):
        return 1
    if(200 <= score <= 234):
        return 2
    if(150 <= score <= 199):
        return 3