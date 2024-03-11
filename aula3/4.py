fatorial = int(input("Digite o valor:"))
apoio = 0;


if(fatorial<0):
    print("Número inválido.")
    print("Deseja digitar outro número? S/N")
    tentativa = str(input())
    
    if(tentativa=="S"):
        fatorial = int(input("Digite o valor:"))
    if(tentativa=="N"):
        print("Encerrando!")
        
calculo = 0

for x in range (fatorial, 0, -1):
    print(fatorial, "x", x, "=", fatorial*fatorial)
    calculo = fatorial*apoio

print(calculo)



