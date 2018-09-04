import talktracker as tt
import numpy as np

"""
This simple program implements an alternative to the GUI I was originally planning to implement for the
msne ethical discussion.

1. my approach is to implement each group as a member.
2. on paper I keep track of group member talking order.
3. on this api I keep track of groups

So in this case, weirdly, each team will be represented as a member!

"""

team1 = tt.Member(name="team1")
team2 = tt.Member(name="team2")
team3 = tt.Member(name="team3")
team4 = tt.Member(name="team4")
team5 = tt.Member(name="team5")

teams = [team1, team2, team3, team4, team5]
team_nums = list(map(str, np.arange(1, len(teams)+1)))
talking = False
old_team_num = 0

session_name = input("Please insert the name of this session: ")
print("\n==================== SESSION BEGINS ====================\n")

while True:

    team_num = input("\nTeam number: ")

    if team_num in team_nums:

        if (team_num != old_team_num) and not talking:  # a new team
            print("New team, team {}, started talking".format(team_num))
            teams[int(team_num)-1].start()
            talking = True
            old_team_num = team_num

        elif (team_num != old_team_num) and talking:  # a team is interrupting another team
            print("New team, team {}, started talking - interrupting team {}".format(team_num, old_team_num))
            teams[int(old_team_num)-1].end()
            teams[int(team_num) - 1].start()
            talking = True
            old_team_num = team_num

        elif (team_num == old_team_num) and not talking:  # a new team
            print("Old team, team {}, started talking again!".format(team_num))
            teams[int(team_num) - 1].start()
            talking = True

        elif (team_num == old_team_num) and talking:  # when same team is stopping!
            print("Current team, team {}, stopped talking".format(team_num))
            teams[int(old_team_num) - 1].end()
            talking = False

    elif team_num == 'q':
        result = np.array(teams)
        np.save(session_name, result)
        print("program finished, data is saved!")
        break

    else:
        print("please insert the right team number or command.")
