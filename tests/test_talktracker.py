import pytest
import talktracker as tt
import time
import numpy as np


class TestMember(object):
    def test_init(self):
        with pytest.raises(TypeError):
            tt.Member()

        tt.Member('Nick')
        tt.Member('Nick', age=30, country='USA' )

        mem = tt.Member('Nick', age=30, country='USA' )
        assert mem.name == 'Nick'
        assert mem.age == 30

    def test_intervals(self):
        mem = tt.Member('a')

        mem.start()
        time.sleep(1)
        mem.end()
        assert np.shape(mem.intervals) == (1,3)
        assert mem.intervals[0][2] == 1

        mem.start()
        time.sleep(1)
        mem.end()
        assert np.shape(mem.intervals) == (2,3)
        assert mem.intervals[1][2] == 1

    def test_total_time(self):
        mem = tt.Member('a')
        mem.start()
        time.sleep(1)
        mem.end()
        assert np.shape(mem.total_time) == (3,)
        assert mem.total_time[2] == 1

        mem.start()
        time.sleep(1)
        mem.end()
        assert np.shape(mem.total_time) == (3,)
        assert mem.total_time[2] == 2



class TestTeam(object):
    def test_init(self):
        with pytest.raises(TypeError):
            tt.Team()
            tt.Team(members=['mem'])

        tt.Team('team0')
        tt.Team('team1', members=['mem0'])
        tt.Team('team1', members=[tt.Member('0')])

        t = tt.Team('team1', members=[tt.Member('0'),
                                      tt.Member('1')])
        assert '0' in t.members
        assert '1' in t.members

    def test_add_member(self):
        team0 = tt.Team('team0')
        team0.add_member(tt.Member('0'))
        assert '0' in team0.members

        team0.add_member(tt.Member('1'))
        assert '0' in team0.members
        assert '1' in team0.members

        team0.add_member('2')
        assert '2' in team0.members



class TestSession(object):
    def test_init(self):
        with pytest.raises(TypeError):
            tt.Session()

        tt.Session('ses')
        tt.Session('teams', teams=[tt.Team('team0',
                                           members=['Nick'])])

        tt.Session('teams', teams=[tt.Team('team0',
                                           members=[tt.Member('Nick', age=30, country='USA')])])

        ses0 = tt.Session('teams', teams=[tt.Team('team0',
                                         members=[tt.Member('Nick'),
                                                  tt.Member('Aleks'),
                                                  tt.Member('Raja'),
                                                  tt.Member('James')])])
        assert 'Nick' in ses0.team0.members
        assert 'James' in ses0.team0.members


        ses1 = tt.Session('no_teams',
                           members=['Nick',  'Aleks'])
        assert 'Nick' in ses1.members
        assert 'Aleks' in ses1.members

        ses2 = tt.Session('no_teams',
                           members=[tt.Member('Nick'),])
       assert 'Nick' in ses1.members
        with pytest.raises(AttributeError):
            ses1.team.members


        def test_add_team(self):
            ses = tt.Session('with_teams')
            ses.add_team('0')
            assert '0' in ses.teams

            ses.add_team(tt.Team('1', members='Mohammad'))
            assert '1' in ses.teams
            assert 'Mohammad' in ses.members


        def test_add_member(self):
            ses = tt.Session('no_teams')
            ses.add_member('0')
            assert '0' in ses.members
