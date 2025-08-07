valorEmDolar = float(input("Digite o valor da sua compra em dólar: "))
cartao = int(input("\n 1 - BRONZE \n 2- PRATA \n 3- OURO \n 4- DIAMANTE" ))
cotacaoDolar = 4.99
pontos = 0
tipoCartao = ""

if(cartao ==1):
    pontos = 1.0
    tipoCartao = "Bronze"
elif(cartao == 2):
    pontos = 1.2
    tipoCartao = "Prata"
elif(cartao ==3):
    pontos = 1.5
    tipoCartao = "Ouro"
elif(cartao == 4):
    pontos = 2.0
    tipoCartao = "Diamante"
else:
    print("Inválido")

valorFinal = pontos*valorEmDolar

print("O VALOR TOTAL DA SUA COMPRA FOI:$", valorEmDolar, "\nSEU CARTÃO:", tipoCartao, "\nTOTAL DE PONTOS:", pontos)
