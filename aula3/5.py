def soma_sequencia(N):
    if N <= 0 or N >= 100:
        print("Erro: O valor de N deve ser positivo e menor que 100.")
        return None
    else:
        sequencia = [2]  # Iniciar a sequência com o primeiro termo
        valor = 2
        for i in range(1, N):
            valor += 3 + i * 2  # O próximo termo é calculado a partir do anterior
            sequencia.append(valor)  # Adicionar o próximo termo à sequência
        return sum(sequencia)  # Retornar a soma dos N primeiros valores da sequência

# Pedir ao usuário para digitar o valor de N
N = int(input("Digite o valor de N (positivo, menor que 100): "))

# Calcular e exibir a soma dos N primeiros valores da sequência
resultado = soma_sequencia(N)
if resultado is not None:
    print(f"A soma dos {N} primeiros valores da sequência é: {resultado}")
