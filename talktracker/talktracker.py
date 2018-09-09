import time
from datetime import datetime
from warnings import warn

from talktracker.talkanalysis import time_diff, time_add, dissect_time, to_seconds


class Member(object):
    def __init__(self, country=None, age=None, batch=None, name=None):

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
        """returns the time interval for every single time a member has talked"""
        self._intervals = []
        for time1, time2 in zip(self.start_times, self.end_times):
            self._intervals.append(time_diff(time2, time1))

        return self._intervals

    @property
    def total_time(self):
        """return the total time a member has talked"""
        self._total_time = (0, 0, 0)
        for t in self.intervals:
            self._total_time = time_add(self._total_time, t)

        return self._total_time

    def start(self):
        """adds the time at which the member starts talking to the _start_times"""
        now = datetime.now()
        self._start_times.append((now.hour, now.minute, now.second))

    def end(self):
        """adds the time at which the member stops talking to the _end_times"""
        now = datetime.now()
        self._end_times.append((now.hour, now.minute, now.second))


class Team(object):
    def __init__(self, members, name):

        if all(isinstance(member, str) for member in members):
            self._members = {member: Member(name=member) for member in members}
        else:
            raise TypeError

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
        self._total_time = (0, 0, 0)
        for member in self._members.keys():
            self._total_time = time_add(self._total_time, self[member].total_time)

        return self._total_time

    def add_member(self, name):
        if isinstance(name, str):
            self._members[name] = Member(name=name)
        elif isinstance(name, list):
            if all(isinstance(n, str) for n in name):
                for n in name:
                    self._members[n] = Member(name=n)
        else:
            raise TypeError("Input must be a string, or a list of ")


class Session(object):
    def __init__(self, teams, name=None):

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
