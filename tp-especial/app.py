import sqlite3 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label

conexao = sqlite3.connect('laboratorio.db')
conexao.execute('CREATE TABLE IF NOT EXISTS verifica(id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, data text, e110 text, e220 text, cooler text, e_5 text, e5 text, e33 text, e12 text, e_12 text, obs text)')


class Tela(BoxLayout):
    pass

class Aplicativo(App):
    def build(self):
        self.lista = [];
        
        return Tela()
    def guardar(self, nome, data, e110,e220, cooler, e_5, e5,e33, e12, e_12, obs):
        self.lista.append ([nome, data, e110,e220, cooler, e_5, e5,e33, e12, e_12, obs])
        conexao.execute('INSERT INTO verifica VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)', (nome, data, e110,e220, cooler, e_5, e5,e33, e12, e_12, obs))
        conexao.commit()
        print(self.lista)
    def buscar(self, box, estado):
        box.clear_widgets() 
        if estado == 'ok':
            print('ok')
        else:
            print('x')
            
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM verifica WHERE cooler = '{}'".format(estado))
        qtd = cursor.fetchall()

        box.text = 'Resultado de Pesquisa: '+str(qtd[0][0])
            
Aplicativo().run()
