contador = 1;
numDigitado = int(input("Digite um número"))

while(contador<=10):
    if(numDigitado<0):
        print("Número inválido")
        numDigitado = int(input("Digite um número"))

    calculo= contador*numDigitado
    print(numDigitado,"*",contador, " = ", calculo)
    contador+=1
    


