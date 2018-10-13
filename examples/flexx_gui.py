from flexx import flx
import talktracker as tt

class Example(flx.PyComponent):

    def setup_member(self, msg):
        print(msg)
        mem = tt.Member(msg)


    def init(self):
        super().init()
        with flx.VBox():
            with flx.HBox():
                self.sessionname = flx.LineEdit(placeholder_text='First name')
            with flx.HBox():
                self.but = flx.Button(text='Reset')
                self.butadd = flx.Button(text='Add')
                self.label = flx.Label(flex=1)


    @flx.reaction('sessionname.text')
    def greet(self, *events):
        self.label.set_text(self.sessionname.text)

    @flx.reaction('but.pointer_click')
    def reset(self, *events):
        self.label.set_text('')

    @flx.reaction('butadd.pointer_click')
    def reset(self, *events):
        self.setup_session(self.sessionname.text)


if __name__ == '__main__':
    app = flx.App(Example)
    app.launch('app')  # to run as a desktop app
    # app.launch('browser')  # to open in the browser
flx.run()
