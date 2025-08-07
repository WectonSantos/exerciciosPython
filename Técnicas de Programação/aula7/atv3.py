import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class Teste(App):
    def build(self):
        grid = GridLayout(cols=4)
        for x in range(3):
            grid.add_widget(Label(text = ''+str(x+7)))

        grid.add_widget(Label(text = '+'))
        for x in range(3):
            grid.add_widget(Label(text = ''+str(x+4)))

        grid.add_widget(Label(text = '-'))
        
        for x in range(3):
            grid.add_widget(Label(text = ''+str(x+1)))

        grid.add_widget(Label(text = '*'))
        grid.add_widget(Label(text = 'Clear'))
        grid.add_widget(Label(text = '0'))
        grid.add_widget(Label(text = '='))
        grid.add_widget(Label(text = '/'))
        
        return grid
    

Teste().run()

