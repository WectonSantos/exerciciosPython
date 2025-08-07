import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

class Tela(BoxLayout):
    pass

class TelaCanvas(App):
    def Build(self):
        return Tela()

TelaCanvas().run()
