import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.pagelayout import PageLayout

class Tela(BoxLayout):
    pass

class AulaSlider2(App):
    def build(self):
        return Tela()
    valor=0
    print(valor)

AulaSlider2().run()
