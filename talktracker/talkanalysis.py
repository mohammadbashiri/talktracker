from datetime import timedelta


def time_diff(time1, time2):
    """calculate the time different"""
    time1_info = timedelta(hours=time1[0], minutes=time1[1], seconds=time1[2])
    time2_info = timedelta(hours=time2[0], minutes=time2[1], seconds=time2[2])
    diff_in_sec = (time1_info - time2_info).seconds

    diff_hours, diff_minutes, diff_seconds = dissect_time(diff_in_sec)

    return diff_hours, diff_minutes, diff_seconds


def time_add(time1, time2):
    """calculate the time different"""
    time1_info = timedelta(hours=time1[0], minutes=time1[1], seconds=time1[2])
    time2_info = timedelta(hours=time2[0], minutes=time2[1], seconds=time2[2])
    add_in_sec = (time1_info + time2_info).seconds

    add_hours, add_minutes, add_seconds = dissect_time(add_in_sec)

    return add_hours, add_minutes, add_seconds


def dissect_time(sec):
    """changes total seconds into hours, minutes, seconds"""
    seconds = sec % 60
    minutes = (sec // 60) % 60
    hours = (sec // 60) // 60

    return hours, minutes, seconds


def to_seconds(*args):
    """Converts (hour, min, sec) to seconds only"""
    if len(args) == 3:
        return args[0] * 60 * 60 + args[1] * 60 + args[2]
    elif len(args) == 1:
        return args[0][0] * 60 * 60 + args[0][1] * 60 + args[0][2]
    else:
        raise ValueError("Input must be either three integers, or a tuple of three integers")
