from flexx import flx
import talktracker as tt

class TalkTrackerGUI(flx.PyComponent):

    def init(self):
        super().init()
        with flx.HBox():
            with flx.VBox():
                with flx.VBox():
                    self.session_name = flx.LineEdit(placeholder_text='Session name')
                    self.team_name = flx.LineEdit(placeholder_text='Team name')
                    self.member_name = flx.LineEdit(placeholder_text='Member name')
                with flx.VBox():
                    self.label_session = flx.Label(flex=1)
                    self.label_team = flx.Label(flex=1)
                    self.label_member = flx.Label(flex=1)

            with flx.VBox():
                with flx.VBox():
                    self.but_create = flx.Button(text='Create')
                with flx.VBox():
                    self.but_start = flx.Button(text='Start')
                    self.but_stop = flx.Button(text='Stop')
                    self.label_time_indicator = flx.Label(flex=2)
                    self.label_time = flx.Label(flex=2)


    @flx.reaction('but_create.pointer_click')
    def create_member(self, *events):
        self.msne = tt.Session(self.session_name.text,
                       teams=[tt.Team(self.team_name.text,
                                      members=[self.member_name.text])])

        self.label_session.set_text('Session ' + self.session_name.text + ' created')
        self.label_team.set_text('Team ' + self.team_name.text + ' created')
        self.label_member.set_text('Member ' + self.member_name.text + ' created')

    @flx.reaction('but_start.pointer_click')
    def start_member(self, *events):
        self.msne[self.team_name.text][self.member_name.text].start()
        self.label_time_indicator.set_text('start')

    @flx.reaction('but_stop.pointer_click')
    def stop_member(self, *events):
        self.msne[self.team_name.text][self.member_name.text].end()
        time = self.msne[self.team_name.text][self.member_name.text].total_time

        self.label_time_indicator.set_text('stop')
        self.label_time.set_text(time)


if __name__ == '__main__':
    app = flx.App(TalkTrackerGUI)
    app.launch('app')
    # app.launch('browser')
flx.run()
