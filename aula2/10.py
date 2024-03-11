contador = 1
salvaNum = 0
lista = []
digitado1 = int(input("Digite um valor: "))
lista.insert(0, digitado1)

while(contador<=9):
    numDigitado = int(input("Digite um valor: "))
    lista.append(numDigitado)
    
    if (numDigitado > lista[contador-1]):
        lista.pop(contador)
        lista.append(numDigitado)
        
    elif (numDigitado<lista[contador-1]):
        lista.pop(contador)
        contador-=1
        
    elif (numDigitado==lista[contador-1]):
        lista.pop(contador)
        contador-=1
        
    contador+=1

print(lista)
