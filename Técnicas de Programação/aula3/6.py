digitado = int(input("Digite o número de alunos: "))
notas = []
soma = 0
media = 0

for x in range(digitado):
    notas.append(int(input("Digite a nota deste aluno:")))
    print(notas)

for x in range (digitado):
    soma+= notas[x]

media = soma/digitado

print("A Média da turma foi:", media)
