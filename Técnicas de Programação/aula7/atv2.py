import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class Teste(App):
    def build(self):    
        box1=BoxLayout(orientation = "vertical")
        box2=BoxLayout()
        box3=BoxLayout()
        lbl1=Label(text ='ENGENHARIA', font_size='50')
        lbl2=Label(text ='COMPUTAÇÃO', font_size='10')
        lbl3=Label(text ='CÍVIL', font_size='10')
        lbl4=Label(text ='QUÍMICA', font_size='10')
        lbl5=Label(text ='UNISANTA', font_size='50')
        
        box1.add_widget(lbl1)
        box1.add_widget(lbl5)
        
        box2.add_widget(lbl2)
        box2.add_widget(lbl3)
        box2.add_widget(lbl4)
        
        
        box3.add_widget(box1)
        box3.add_widget(box2)
        


        return box3
    

Teste().run()
