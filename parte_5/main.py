import kivy
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
kivy.require('1.10.1')


def func_self(ad):
    print("Func_Self")
Button.func_self = func_self

class Tela(BoxLayout):

    def func_root(self):
        print("Funç Root")




class Tela5App(App):
    def func_app(self):
        print("Func App")

janela = Tela5App()
janela.run()