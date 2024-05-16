from datetime import datetime


def seconds_to_minutes_and_seconds(seconds):
    return datetime.fromtimestamp(seconds).strftime("%M minutes %S seconds")

def minutes_to_seconds(minutes):
    return minutes * 60


def make_time_from_string(time_string):
    return datetime.strptime(time_string, "%H:%M").time()

def is_between_time(start, end, now=datetime.now().time()):
    time_to_check = now
    start = make_time_from_string(start)
    end = make_time_from_string(end)
    if start == end:
        return False
    elif start < end:
        return time_to_check >= start and time_to_check <= end
    else:
        return time_to_check >= start or time_to_check <= end