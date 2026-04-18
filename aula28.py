"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome_usuario = input("Digite seu nome: ")
idade_usuario = input("Digite sua idade: ")

if nome_usuario and idade_usuario:
    print(f"seu nome é {nome_usuario}")
    print(f"seu nome invertido é: {nome_usuario[::-1]}")
    print(f"Seu nome Contém Espaços: {'' in nome_usuario}")
    print(f"Seu nome tem {len(nome_usuario)} letras")
    print(f"A primeira letra do seu nome é: {nome_usuario[0]}")
    print(f"A Ultima letra do seu nome é: {nome_usuario[len(nome_usuario)-1]}")
else:
    print("Você não preencheu os campos corretamente!")
