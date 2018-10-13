from flexx import flx
import talktracker as tt

class Example(flx.PyComponent):

    def init(self):
        super().init()
        with flx.VBox():
            with flx.HBox():
                self.member_name = flx.LineEdit(placeholder_text='Member name')

            with flx.HBox():
                self.but_create = flx.Button(text='Create')
                self.label_member = flx.Label(flex=1)


    # @flx.reaction('member_name.text')
    # def greet(self, *events):
    #     self.label_member.set_text(self.member_name.text)

    @flx.reaction('but_create.pointer_click')
    def create_member(self, *events):
        mem = tt.Member(self.member_name.text)
        self.label_member.set_text('Member ' + self.member_name.text + ' created')



if __name__ == '__main__':
    app = flx.App(Example)
    app.launch('app')
    # app.launch('browser')
flx.run()
