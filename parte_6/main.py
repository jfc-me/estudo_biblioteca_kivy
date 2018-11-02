import kivy
from kivy.app import App
from kivy.lang import Builder
kivy.require('1.10.1')


cod = """
BoxLayout:
 orientation: 'vertical'
 Button:
  text: 'iniciar'
 Button:
  text: 'retornar'
 Button:
  text: 'parar'
"""

class TelaApp(App):
    def build(self):
        return Builder.load_string(cod)

janela = TelaApp()
janela.run()