import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.10.1')


class Tela(BoxLayout):

    def revificar(self):
        msg = "Chamado"
        print(msg)
        self.ids.lb_title_expl.text = ""
        self.ids.lb_title_apre.text = msg
class Tela4App(App):
    pass


janela = Tela4App()
janela.run()