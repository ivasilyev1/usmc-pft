import math

def get_run_row_time_to_seconds(run, row):
    time = run if run else row
    time_split = time.split(":")
    minutes = int(time_split[0]) * 60
    seconds = int(time_split[1])
    if(run):
        seconds = int(math.ceil(seconds / 10.0)) * 10
    if(row):
        seconds = int(math.ceil(seconds/5.0)) * 5 
    return minutes + seconds

def get_plank_time_to_seconds(plank):
    time = plank.split(":")
    minutes = int(time[0]) * 60
    seconds = int(time[1])
    return minutes + seconds

def get_age_range(age):
    for age_range in [[17, 20], [21, 25], [26, 30], [31, 35], [36, 40], [41, 45], [46, 50]]:
        if(age in range(age_range[0], age_range[1] + 1)):
            return age_range[0]
        if(age >= 51):
            return 51

def get_total_pft_score_and_class(scores):
    cardio = scores["run"]["score"] if "run" in scores.keys() else scores["row"]["score"]
    abdominal = scores["crunches"]["score"] if "crunches" in scores.keys() else scores["plank"]["score"]
    upper_body = scores["pullups"]["score"] if "pullups" in scores.keys() else scores["pushups"]["score"]
    auto_fail = True if 0 in [cardio, abdominal, upper_body] else False
    total = cardio + abdominal + upper_body
    pft_class = get_pft_class(total, auto_fail)
    return {"score": total, "class": pft_class}

def get_pft_class(score, auto_fail):
    if(score < 150 or auto_fail):
        return 0
    if(score >= 235):
        return 1
    if(200 <= score <= 234):
        return 2
    if(150 <= score <= 199):
        return 3