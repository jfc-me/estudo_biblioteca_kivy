import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require(kivy.version.__version__) #versao


class Unix(BoxLayout):
    def apresent(self):
        print("Msg...")

    def bt2(self):
        print("Msg... _2")
class TlApp(App):
    pass

janela = TlApp()
janela.run()