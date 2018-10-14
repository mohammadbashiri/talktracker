from datetime import datetime
from warnings import warn

from talktracker.analysis import time_diff, time_add, dissect_time, to_seconds


class Member(object):
    def __init__(self, name, **kwargs):
        """Create a Memebr

        Args:
            name (str): name of the memebr

        Returns:
            a Member object
        """
        self.name = name
        [setattr(self, key, value) for key, value in kwargs.items()];
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
    def __init__(self, name, members=[]):
        """Create a Team object

        Args:
            members: list of member names or a list of member object
            name: name of the team

        Returns:
            a Team object
        """
        self._members = []
        [self.add_member(member) for member in members];
        self.name = name
        self._total_time = (0, 0, 0)

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def members(self):
        return self._members

    @property
    def member_counts(self):
        return len(self.members)

    @property
    def total_time(self):
        """Returns the total time of the whole group speaking"""
        self._total_time = (0, 0, 0)
        for member in self._members:
            self._total_time = time_add(self._total_time, getattr(self, member).total_time)

        return self._total_time

    def add_member(self, member):
        """Adds a user to the group

        Args:
            member (str ot list): the name of the new member or the new Member object
        """
        if isinstance(member, str):
            setattr(self, member, Member(member))
            self._members.append(member)
        elif isinstance(member, Member):
            setattr(self, member.name, member)
            self._members.append(member.name)
        else:
            raise TypeError("Please provide a list of member names or member objects.")


class Session(object):
    def __init__(self, name, teams=[], members=[]):
        """Creates a session object

        Args:
            teams (list): list of team names or a list of team object
            name (str): name of the session
        """
        self.name = name if name else "Untitled"
        self._members = []
        [self.add_member(member) for member in members];
        self._teams = []
        [self.add_team(team) for team in teams];
        self.date = None
        self.start_time = (0, 0, 0)
        self.end_time = (0, 0, 0)
        self.set_date()

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def members(self):
        return self._members
    
    @property
    def teams(self):
        return self._teams

    def add_member(self, member):
        """Adds a new member to the session

        Args:
            member(str or Member): Either a string or a Memebr object to be added to the session
        """
        if isinstance(member, str):
            setattr(self, member, Member(member))
            self._members.append(member)
        elif isinstance(member, Member):
            setattr(self, member.name, member)
            self._members.append(member.name)
        else:
            raise TypeError("Please provide a member name or a member object.")

    def add_team(self, team):
        """Adds a new team to the session

        Args:
            team (str or Team): Either a string or a Team object to be added to the session
        """
        if isinstance(team, str):
            setattr(self, team, Team(team))
            self._teams.append(team)
        elif isinstance(team, Team):
            setattr(self, team.name, team)
            self._teams.append(team.name)
        else:
            raise TypeError("Please provide a team name or a team object.")

    def set_date(self, force_it=False):
        """Set a date for the session"""
        if (not self.date) or force_it:
            self.date = datetime.now().strftime('%d/%m/%Y')
        else:
            warn("You are trying to set the date again. \nIf you are aware of that, set force_it to True")


    def start(self):
        """Sets the start time of the whole session"""
        now = datetime.now()
        self.start_time = (now.hour, now.minute, now.second)

    def end(self):
        """Sets the end time of the whole session"""
        now = datetime.now()
        self.end_time = (now.hour, now.minute, now.second)

    def save(self):
        """Save the session data in a CSV file"""
        raise NotImplementedError
