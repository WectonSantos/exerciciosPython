contador = 0
contador2 = 0
apoio = 0
contaFinal= 0
conta = 0
lista = []
lista2 = []
while(contador<=9):
    numDigitado = int(input("Digite um valor: "))
    lista.append(numDigitado)
    contador+=1

multiplicador = int(input("Digite um número para multiplicar"))

while(contador2<=9):
    conta = multiplicador*lista[contador2]
    contaFinal += conta
    contador2+=1

lista.append(contaFinal)

print(lista)
