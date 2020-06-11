import math

def get_run_row_time_to_seconds(run, row):
    time = run if run else row
    time_split = time.split(":")
    minutes = int(time_split[0]) * 60
    seconds = int(time_split[1])
    # Run times are rounded up to the 10 second mark.
    # Row times are rounded up to the 5 second mark.
    if(run):
        seconds = int(math.ceil(seconds / 10.0)) * 10
    if(row):
        seconds = int(math.ceil(seconds/5.0)) * 5 
    return minutes + seconds

def get_time_to_seconds(time_string):
    time = time_string.split(":")
    minutes = int(time[0]) * 60
    seconds = int(time[1])
    return minutes + seconds

def get_age_range(age):
    # Age ranges are defined by USMC order. The scores within each range are
    # calculated the same, so for simplicity the starting age is used in each range.
    # IE: range 17 - 21 will use 17 as the age for calculations.
    if(age >= 51):
        return 51
    for age_range in [[17, 20], [21, 25], [26, 30], [31, 35], [36, 40], [41, 45], [46, 50]]:
        if(age in range(age_range[0], age_range[1] + 1)):
            return age_range[0]