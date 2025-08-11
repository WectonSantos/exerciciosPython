"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
def programa():
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite sua idade: '))
    vazios = 'Não';

    if nome and idade:
        for x in nome:
            if x == ' ':
                vazios = 'Sim'

            if idade:
                print(f"Nome: {nome}\nNome Invertido: {nome[::-1]}\nTem vazios: {vazios}\nTem {len(nome)} letras\nPrimeira Letra: {nome[0]}\nÚltima letra: {nome[-1]}")
    else:
        print('Desculpe, você deixou campos vazios.')
        programa()

programa()