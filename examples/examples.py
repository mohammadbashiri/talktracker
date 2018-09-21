from talktracker import Member, Team, Session

"""
talktracker's Python API is meant to be very flexible.
User can pretty much create Session, Teams, and Members in 
any intuitive way

Here are some examples: 
"""

"""
one way is the simplest step-by-step approach

1. create a session
2. create team(s)
3. create member(s)
4. assign member(s) to the team(s)
5. assign team(s) to the session
and done!
"""


msne = Session('MSNE')
team = Team('RockStars')
member = Memeber('Nick')

team.add_member(member)
session.add_team(team)

# and that is it. However, this whole thing can also boil down to one line
msne = Session('MSNE', teams=[Team('RockStars', members=['Nick'])])


# let's say you want to have more features for a member, including age, country, etc.
# For this purpose, we take advantage of the Member class, and pass the Member object to
# the Team initializer instead of the name of the member.
msne = Session('MSNE', teams=[Team('RockStars', members=[Member('Nick', age=30, country='USA')])])

# more members?
msne = Session('MSNE', teams=[Team('RockStars', 
									members=[Member('Nick', age=30, country='USA'),
											 Member('Aleks', age=24, country='Poland'),
											 Member('Raja', age=27, country='Jordan'),
											 Member('James', age=26, country='USA'),
									])])


# more teams?

msne = Session('MSNE', teams=[Team('RockStars', 
									members=[Member('Nick', age=30, country='USA'),
											 Member('Aleks', age=24, country='Poland'),
											 Member('Raja', age=27, country='Jordan'),
											 Member('James', age=26, country='USA'),
									]),
							  Team('ShadowWalkers', 
									members=[Member('Michael', age=24, country='Germany'),
											 Member('yagmur', age=22, country='Turkey'),
											 Member('Janne', age=24, country='Germany'),
											 Member('Christoph', age=26, country='Germany'),
									]),
							  Team('Huxlaysians', 
									members=[Member('Nicholas', age=25, country='Germany'),
											 Member('Francisco', age=24, country='Argentina'),
											 Member('Abdallah', age=25, country='Jordan'),
											 Member('Mohamad', age=29, country='Afghanistan'),
									]),
							  Team('Newrons', 
									members=[Member('Auguste', age=24, country='Germany'),
											 Member('Jonas', age=24, country='Germany'),
											 Member('Steffen', age=24, country='Germany'),
											 Member('Elisa', age=24, country='Italy'),
									]),])