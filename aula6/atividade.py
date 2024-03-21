import sqlite3
import time

conexao = sqlite3.connect('tabela.db')
conexao.execute('CREATE TABLE IF NOT EXISTS tabelaBr(id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, pontos integer, vitorias integer, empates integer, derrotas integer, jogos integer, golsMarcados integer, golsSofridos integer, saldoGols integer, aproveitamento decimal)')

def enviaDados():
    nome = input('Digite o nome do time: ')
    vitorias = int(input('Digite o número de vitórias do time: '))
    empates = int(input('Digite o número de empates do time: '))
    derrotas = int(input('Digite o número de derrotas do time: '))
    pontos = (3*vitorias)+(1*empates)
    jogos = vitorias+empates+derrotas
    golsM = int(input('Digite o número de gols marcados: '))
    golsS = int(input('Digite o número de gols sofridos: '))
    saldoGols = golsM-golsS;
    pontuacaoMaxima = jogos*3
    aproveitamento = round(((pontos/pontuacaoMaxima)*100),1)

    conexao.execute('INSERT INTO tabelaBr VALUES(NULL,?,?,?,?,?,?,?,?,?,?)', (nome,pontos,vitorias,empates,derrotas,jogos,golsM,golsS,saldoGols,aproveitamento))
    conexao.commit()

def buscarTime():
    nome = input('Digite o nome do time que deseja buscar: ')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tabelaBr WHERE nome = ?', (nome,))
    lista = cursor.fetchall()
    if(len(lista)==0):
        print('TIME NÃO ENCONTRADO NA BASE DE DADOS!')
    else:
        print('ID\tN\tP\tV\tE\tD\tJ\tGM\tGS\tSG\tA')
        for i in lista:
            print(str(i[0])+'\t'+i[1]+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\t'+str(i[6])+'\t'+str(i[7])+'\t'+str(i[8])+'\t'+str(i[9])+'\t'+str(i[10])+'%')   

def buscarTimePontuacao():
    pontuacao = int(input('Digite a pontuação que deseja filtrar: '))
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tabelaBr WHERE pontos >= ?', (pontuacao,))
    lista = cursor.fetchall()
    if(len(lista)==0):
        print('NÃO POSSUI NENHUM TIME COM ESSA PONTUAÇÃO OU MAIOR NA BASE DE DADOS!')
    else:
        print('ID\tN\tP\tV\tE\tD\tJ\tGM\tGS\tSG\tA')
        for i in lista:
            print(str(i[0])+'\t'+i[1]+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\t'+str(i[6])+'\t'+str(i[7])+'\t'+str(i[8])+'\t'+str(i[9])+'\t'+str(i[10])+'%')

def buscarTimeAproveitamento():
    aproveitamento = int(input('Digite o aproveitamento que deseja filtrar: '))
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tabelaBr WHERE aproveitamento >= ?', (aproveitamento,))
    lista = cursor.fetchall()
    if(len(lista)==0):
        print('NÃO POSSUI NENHUM TIME COM ESSE APROVEITAMENTO OU MAIOR NA BASE DE DADOS!')
    else:
        print('ID\tN\tP\tV\tE\tD\tJ\tGM\tGS\tSG\tA')
        for i in lista:
            print(str(i[0])+'\t'+i[1]+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\t'+str(i[6])+'\t'+str(i[7])+'\t'+str(i[8])+'\t'+str(i[9])+'\t'+str(i[10])+'%')

def menu():
    opcao = int(input('1. CADASTRAR TIME\n2. BUSCAR TIME\n3. FILTRAR POR PONTUAÇÃO\n4. FILTRAR POR APROVEITAMENTO\n5.SAIR\n'))

    if (opcao==1):
        enviaDados()
    elif (opcao==2):
        buscarTime()
    elif (opcao==3):
        buscarTimePontuacao()
    elif (opcao==4):
        buscarTimeAproveitamento()
    elif(opcao==5):
        print('Encerrando o programa...')
        time.sleep(3)
        exit()
    else:
        print('Opção Inválida...')
        time.sleep(3)
        menu()

menu()
