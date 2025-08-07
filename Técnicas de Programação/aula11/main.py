# WECTON SANTOS
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label

class Tela(ScreenManager):
    pass

class Aplicativo(App):
    def build(self):
        self.lista = [['Agatha','F',25], ['Alexandre','M',32], ['Camila','F',30], ['Esther','F',18], 
                      ['Nathan','M',24], ['Isis','F',42], ['Amanda','F',32], ['Antônio','M',21], 
                      ['Maria','F',22], ['Pietro','M',30], ['Henry','M',45], ['Laís','F',26], 
                      ['Ian','M',31], ['Carolina','F',29], ['Vicente','M',30]]
        return Tela()
    
    def guardar(self, nome, genero, idade):
        self.lista.append([nome, genero, int(idade)])
    
    def mostrar(self, box, generos, idade_minima, idade_maxima):
        box.clear_widgets()  # Limpar widgets existentes
        genero_selecionado = None
        if generos[0] == 'down':
            genero_selecionado = 'M'
        elif generos[1] == 'down':
            genero_selecionado = 'F'
        else:
            genero_selecionado = 'Qualquer'
        
        for pessoa in self.lista:
            if (genero_selecionado == 'Qualquer' or genero_selecionado == pessoa[1]) and pessoa[2] >= int(idade_minima) and pessoa[2] <= int(idade_maxima):
                label = Label(text=f"{pessoa[0]}, {pessoa[1]}, {pessoa[2]}", size_hint_y=None, height=40)
                box.add_widget(label)

            
Aplicativo().run()
