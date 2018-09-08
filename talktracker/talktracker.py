import time
from datetime import datetime, timedelta
from warnings import warn


class Member(object):
    def __init__(self, country=None, age=None, batch=None, name=None):
    #TODO: get the input as kwargs so the user can have control over args
    """Create a Memebr

    Args:
        country (string):
        age (int):
        batch (string):
        name (string):

    Returns:
        a Member object
    """
        self.name = name
        self.country = country
        self.age = age
        self.batch = batch
        self._start_times = []
        self._end_times = []
        self._intervals = []
        self._total_time = (0, 0, 0)

    @property
    def start_times(self):
        return self._start_times

    @property
    def end_times(self):
        return self._end_times

    @property
    def intervals(self):
        """Returns the time interval for every single time a member has talked"""
        self._intervals = []
        for time1, time2 in zip(self.start_times, self.end_times):
            self._intervals.append(time_diff(time2, time1))

        return self._intervals

    @property
    def total_time(self):
        """Return the total time a member has talked"""
        self._total_time = (0, 0, 0)
        for t in self.intervals:
            self._total_time = time_add(self._total_time, t)

        return self._total_time

    def start(self):
        """Adds the time at which the member starts talking to the _start_times"""
        now = datetime.now()
        self._start_times.append((now.hour, now.minute, now.second))

    def end(self):
        """Adds the time at which the member stops talking to the _end_times"""
        now = datetime.now()
        self._end_times.append((now.hour, now.minute, now.second))


class Team(object):
    def __init__(self, members, name):
    """Create a Team object

    Args:
        members: list of member names
        name: name of the team

    Returns:
        a Team object
    """
    #TODO: user should be able to also create a Team with a list of existing member objects
        if all(isinstance(member, str) for member in members):
            self._members = {member: Member(name=member) for member in members}
        else:
            raise TypeError("Please provide a list of member names.")

        self.name = name
        self._total_time = (0, 0, 0)

    def __getitem__(self, item):
        return self._members[item]

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self._members[item]

    @property
    def members(self):
        return list(self._members.keys())

    @property
    def member_counts(self):
        return len(self.members)

    @property
    def total_time(self):
        """Returns the total time of the whole group speaking"""
        self._total_time = (0, 0, 0)
        for member in self._members.keys():
            self._total_time = time_add(self._total_time, self[member].total_time)

        return self._total_time

    def add_member(self, name):
        """Adds a user to the group

        Args:
            name (string or list of strings)
        """
        if isinstance(name, str):
            self._members[name] = Member(name=name)
        elif isinstance(name, list):
            if all(isinstance(n, str) for n in name):
                for n in name:
                    self._members[n] = Member(name=n)
        else:
            raise TypeError("Input must be a string, or a list of string)


class Session(object):
    def __init__(self, teams, name=None):
    """Creates a session object

    Args:
        teams ():
        name ():
    """
        self.name = name
        self._teams = {team.name: team for team in teams}
        self.date = None
        self.start_time = (0, 0, 0)
        self.end_time = (0, 0, 0)
        self.set_date()

    def __getitem__(self, item):
        return self._teams[item]

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self._teams[item]

    @property
    def teams(self):
        return list(self._teams.keys())

    def set_date(self, force_it=False):
    """Set a date for the session"""
        yy = time.ctime().split(' ')[-1]
        ddmm = ' '.join(time.ctime().split(' ')[1:3])
        if (not self.date) or force_it:
            self.date = ' '.join([ddmm, yy])
        else:
            warn("You are trying to set the date again. \nIf you are aware of that, set force_it to True")

    def start(self):
        now = datetime.now()
        self.start_time = (now.hour, now.minute, now.second)

    def end(self):
        now = datetime.now()
        self.end_time = (now.hour, now.minute, now.second)

    def save(self):
        raise NotImplementedError


# class Analysis(object):
#     def __init__(self):

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
