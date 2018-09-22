from datetime import timedelta
from random import sample, randint
import talktracker as tt


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

def gen_fake_data(teams_n=0, members_n=[], duration=(2, 30, 0)):

    """ Sudo code
    
    1. create teams_n teams with randomly generated names
    2. for each team create corresponding number of members with randomly generated attributes.
       attributes might include:
        - age (int)
        - country (str, category)
        - batch (int)

    3. create a session and add the teams to the session
    4. randomly pick a team
    5. randomly pick a member and assign a time to him/her
    6. do 4 and 5 again and again until the total time of the session (total time of the total times of the teams) becomes greater than the given duration

    """

    team_names = team_name_list.copy()
    member_names = member_name_list.copy()

    teams = []
    for ind in range(teams_n):
        members = []
        for _ in range(members_n[ind]):
            name = sample(member_names, 1)[0]
            member_names.remove(name) # remove this name from the list (without replacement)
            age = randint(1, 40)
            batch = randint(1, 3)
            country = 'Germany'
            members.append(tt.Member(name, age=age, batch=batch, country=country))

        name = sample(team_names, 1)[0]
        team_names.remove(name)
        teams.append(tt.Team(name, members=members))


    session = tt.Session('Untitled', teams=teams)

    return session
    """ Generates data for a fake session

    Args:
        teams_n (int): number of teams
        members_n (int or a list): a single number or a list of numbers. of a single number os passed all the team will have similar number of members.

    Returns:
        a session object with fake data
    
    """


team_name_list = ["RockStars", "ShadowWalkers", "MiddleEasterns", "Newrons", "Persians", 
                  "Baghalies", "Golabies", "Loosers"]

member_name_list = ["Mohammad", "Annika", "Amir", "Yasaman", "Arman", "Nick", "Nicholas" , 
                    "Michael", "Aleksndra", "Fati", "Rasoul", "Janne", "Yagmur", "Raja", 
                    "Abdallah", "Viktorja", "Alex", "James", "Marie", "Auguste", "Nora", 
                    "Mathew", "Stefan", "Steffen", "Darya", "Tamara", "Ali", "Niloufar", 
                    "Christoph", "Werner", "Florian", "Bernhard", "Samuel", "Karan", "Elisa",
                    "Atena", "Milad", "Nazanin", "Rahaa", "Amin", "Ehsan", "Shahab", "Sepideh"]