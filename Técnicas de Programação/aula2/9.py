contador = 0
lista = []
while(contador<=9):
    numDigitado = int(input("Digite um valor: "))
    lista.append(numDigitado)
    contador+=1

menor= min(lista)
maior = max(lista)
soma = sum(lista)
media = soma/10

print("MENOR:", menor)
print("MAIOR:", maior)
print("SOMA:", soma)
print("MEDIA:", media)
