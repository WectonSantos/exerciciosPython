import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tela(BoxLayout):
    pass

class AulaSlider(App):
    def build(self):
        return Tela()

AulaSlider().run()
