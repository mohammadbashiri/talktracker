import talktracker as tt

team1 = tt.Team(members=["mohd", "raja", "abd"], name="team1")
team2 = tt.Team(members=["nick", "aleks", "james"], name="team2")

session1 = tt.Session(teams=(team1, team2))
