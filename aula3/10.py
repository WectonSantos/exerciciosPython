opcao = int(input("\n 1 - RETÂNGULO \n 2- QUADRADO \n 3- TRIÂNGULO \n 4- CÍRCULO \n 5- ENCERRAR" ))
base = 0
altura = 0;
raio = 0
soma = 0

if (opcao == 1):
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    soma = base*altura
    print("RESULTADO: ", soma)
                         
elif (opcao == 2):
    base = float(input("Digite o lado: "))
    soma = base*base
    print("RESULTADO: ", soma)
    
elif (opcao == 3):
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    soma = (base*altura)/2
    print("RESULTADO: ", soma)
    
elif (opcao == 4):
    base = float(input("Digite o raio: "))
    soma = (base*base)*3.14
    print("RESULTADO: ", soma)

elif (opcao ==5):
    print("ENCERRANDO...")
