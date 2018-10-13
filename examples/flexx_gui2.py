from flexx import flx
import talktracker as tt

class TalkTrackerGUI(flx.PyComponent):

    def init(self):
        super().init()
        with flx.HSplit():
            with flx.VSplit():

                with flx.VSplit():
                    with flx.HSplit():
                        with flx.VSplit():
                            self.label_session = flx.Label(flex=1, text='Session:')
                            self.label_team = flx.Label(flex=1, text='Team:')
                        with flx.VSplit():
                            self.session_name = flx.LineEdit(placeholder_text='Session name')
                            self.team_name = flx.LineEdit(placeholder_text='Team name')
                        with flx.VBox():
                            self.but_create = flx.Button(text='Create')
                    with flx.HSplit():
                        with flx.VBox():
                            self.label_member = flx.Label(flex=1, text='Member:')
                        with flx.VBox():
                            self.label_teamA = flx.Label(flex=1, text='Team A')
                            self.member_name = flx.LineEdit(placeholder_text='Member name')
                        with flx.VBox():
                            self.but_create2 = flx.Button(text='Create')

                        pass

                with flx.VSplit():
                    pass
            with flx.HSplit():
                pass


    @flx.reaction('but_create.pointer_click')
    def create_member(self, *events):
        self.member_name = 'aaaaa'
        self.msne = tt.Session(self.session_name.text,
                   teams=[tt.Team(self.team_name.text,
                                  members=[self.member_name])])


if __name__ == '__main__':
    app = flx.App(TalkTrackerGUI)
    app.launch('app')
    # app.launch('browser')
flx.run()
