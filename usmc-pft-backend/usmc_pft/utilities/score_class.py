def get_total_pft_score_and_class(scores):
    cardio = scores["run"]["score"] if "run" in scores.keys() else scores["row"]["score"]
    abdominal = scores["crunches"]["score"] if "crunches" in scores.keys() else scores["plank"]["score"]
    upper_body = scores["pullups"]["score"] if "pullups" in scores.keys() else scores["pushups"]["score"]
    auto_fail = 0 in [cardio, abdominal, upper_body]
    total = cardio + abdominal + upper_body
    pft_class = get_pft_cft_class(total, auto_fail)
    return {"score": total, "eventClass": pft_class}

def get_total_cft_score_and_class(scores):
    mtc = scores["mtc"]["score"]
    muf = scores["muf"]["score"]
    ammo = scores["ammo"]["score"]
    auto_fail = 0 in [mtc, muf, ammo]
    total = mtc + muf + ammo
    cft_class = get_pft_cft_class(total, auto_fail)
    return {"score": total, "eventClass": cft_class}

def get_pft_cft_class(score, auto_fail):
    if(score < 150 or auto_fail):
        return 0
    if(score >= 235):
        return 1
    if(200 <= score <= 234):
        return 2
    if(150 <= score <= 199):
        return 3