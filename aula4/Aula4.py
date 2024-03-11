import math


def atv1():
    digitado = str(input("DIGITE ALGO:"))
    digitado2 = str(input("DIGITE MAIS ALGUMA:"))
    comprimento = len(digitado)
    comprimento2 = len(digitado2)
    mesmoC= False
    iguais = False
    print("Conteúdo 1:  ", digitado)
    print("Comprimento 1:  ", comprimento)
    print("Conteúdo 2:  ", digitado2)
    print("Comprimento 2:  ", comprimento2)
    
    if(comprimento == comprimento2):
        mesmoC = True
    if(digitado == digitado2):
        iguais = True

    if(mesmoC == True):
        print("Possuem o mesmo comprimento!")
    else:
        print("Não possuem o mesmo comprimento!")
        
    if(iguais == True):
        print("São iguais me conteúdo!")
    else:
        print("São diferentes em conteúdo!")
    


def atv2():
    data = str(input("Digite sua data de nascimento: "))
    dia = data[0:2]
    mes = data[3]
    ano = data [5:10]

    mesExtenso = '';

    if(mes == '1'):
        mesExtenso = 'Janeiro'
    elif(mes == '2'):
        mesExtenso = 'Fevereiro'
    elif(mes == '3'):
        mesExtenso = 'Março'
    elif(mes == '4'):
        mesExtenso = 'Abril'
    elif(mes == '5'):
        mesExtenso = 'Maio'
    elif(mes == '6'):
        mesExtenso = 'Junho'
    elif(mes == '7'):
        mesExtenso = 'Julho'
    elif(mes == '8'):
        mesExtenso = 'Agosto'
    elif(mes == '9'):
        mesExtenso = 'Setembro'
    elif(mes == '10'):
        mesExtenso = 'Outubro'
    elif(mes == '11'):
        mesExtenso = 'Novembro'
    elif(mes == '12'):
        mesExtenso = 'Dezembro'

    print(dia,'de',mesExtenso,'de', ano)

def atv3():

    numero = int(input("DIGITE UM NÚMERO:"))
    
    unidades = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove']
    especiais = ['Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove']
    dezenas = ['Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa']
    
    if numero < 10:
        return unidades[numero]
    elif numero >= 10 and numero < 20:
        return especiais[numero - 10]
    else:
        dezena = dezenas[(numero // 10) - 2]
        unidade = unidades[numero % 10]
        if numero % 10 == 0:
            return dezena
        else:
            return dezena + " e " + unidade

  
    while numero < 0 or numero > 99:
        numero = int(input("Digite um número entre 0 e 99: "))
        if numero < 0 or numero > 99:
            print("Por favor, digite um número válido entre 0 e 99.")

    print("Número por extenso:", numero_por_extenso(numero))


def atv4(texto):
    texto_limpo = ''
    for char in texto:
        if char.isalpha() or char.isspace():
            texto_limpo += char
    palavras = texto_limpo.split()
    return " ".join(palavras)


    texto = "A reunião foi marcada para o dia 04/04 - 17:00 horas"
    palavras = atv4(texto)
    print("Palavras no texto:", palavras)
    print("Número de palavras:", len(palavras))




def atv5(num1,num2,num3):
    media = (num1+num2+num3)/3
    print ("Média = ", media)

def enviaAtv5():
    num1 = float(input("Digite um valor:"))
    num2 = float(input("Digite um valor:"))
    num3 = float(input("Digite um valor:"))

    atv5(num1, num2, num3)

def atv6(p1,p2):
    media = (p1+(p2*2))/3
    mediaP3 = 0
    maiorNota = 0
    if(p1>p2):
        maiorNota = p1
    if(p2>p1):
        maiorNota = p2

    
    if(media >=5):
        print("APROVADO!")
    elif(media <=5):
        print("FICOU DE P3!")
        p3 = float(input("Digite a sua p3:"))
        mediaP3 = (maiorNota+(2*p3))/3

        if(mediaP3>=5):
            print("APROVADO!")
        else:
            print("REPROVADO!")

        

def enviaAtv6():
    p1 = float(input("Digite sua p1:"))
    p2 = float(input("Digite sua p2:"))
    atv6(p1, p2)


def atv7(opcao):
    print("OPÇÃO ", opcao)

def enviaAtv7():
    opcao = int(input("OPÇÃO 1\nOPÇÃO 2\nOPÇÃO 3\nOPÇÃO 4\nOPÇÃO 5\n DIGITE SUA OPÇÃO:"))
    atv7(opcao)




def atv8(real, imag):
    modulo = math.sqrt(real*2 + imag*2)
    
    if real > 0:
        fase = math.atan(imag / real)
    elif real < 0 and imag >= 0:
        fase = math.atan(imag / real) + math.pi
    elif real < 0 and imag < 0:
        fase = math.atan(imag / real) - math.pi
    elif real == 0 and imag > 0:
        fase = math.pi / 2
    elif real == 0 and imag < 0:
        fase = -math.pi / 2
    else:
        fase = None
    
    return modulo, fase

    parteReal = float(input("Digite a parte real: "))
    parteImg = float(input("Digite a parte imaginária: "))

    modulo, fase = atv8(parteReal, parteImg)
    print("Número na forma polar: {:.2f}∠{:.2f} rad".format(modulo, fase))
