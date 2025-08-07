import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class Teste(App):
    def build(self):    
        box1=BoxLayout()

        lbl1=Label(text ='João', font_size='15', color=[255,242/255,0,1])
        lbl2=Label(text ='Maria', font_size='30', color=[251/255,4/255,233/255,1])
        lbl3=Label(text ='José', font_size='45', color=[27/255,214/255,228/255,1])
        
        box1.add_widget(lbl1)
        box1.add_widget(lbl2)
        box1.add_widget(lbl3)


        return box1
    

Teste().run()
