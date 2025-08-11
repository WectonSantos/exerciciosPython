"""
EX 01


numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero %2 != 0:
        print("É um número impar")
    else:
        print("É um número par")
    
except:
    print('O numero digitado não é inteiro!')

"""


"""
EX 02

hora = input("Digite a sua hora (00:00): ")
digitos = hora[0] + "" + hora[1]
horaInvalida = 'Hora inválida!'
try:
    digitos = int(digitos)
    if digitos >=0 and digitos <= 11:
        print('Bom Dia!')
    elif digitos >11 and digitos <=17:
        print('Boa Tarde!')
    elif digitos>18 and digitos <=23:
        print('Boa Noite!')
    elif digitos>23:
        print(horaInvalida)
except:
        print(horaInvalida)

"""

"""
EX 03
"""

nome = input('Digite seu nome: ')

if len(nome) >0:
    if len(nome) <=4:
        print('Seu nome é curto!')
    elif len(nome) >4 and len(nome) <7:
        print('Nome normal')
    elif len(nome)>6:
        print('Nome grande!') 
else:
    print('Nome inválido!')
    