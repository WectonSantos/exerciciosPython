contador = 0
lista = []
while(contador<=9):
    numDigitado = int(input("Digite um valor: "))
    lista.append(numDigitado)
    contador+=1

maior = max(lista)
soma = sum(lista)
media = soma/10
print("O maior número: ", maior)
print("O soma dos valores: ", soma)
print("O média: ", media)
