"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os
import random

lista_de_nomes = [
    "Isadora",
    "Lucas",
    "Mariana",
    "João",
    "Beatriz",
    "Rafael",
    "Camila",
    "Pedro",
    "Ana",
    "Gabriel",
    "Larissa",
    "Felipe",
    "Juliana",
    "Matheus",
    "Bianca",
    "Gustavo",
    "Renata",
    "Thiago",
    "Vanessa",
    "Bruno",
]

palavra_secreta = random.choice(lista_de_nomes).lower()
tentativas = 0
letras_acertadas = ""

while True:

    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("digite apenas uma letra")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letras in palavra_secreta:
        if letras in letras_acertadas:
            palavra_formada += letras
        else:
            palavra_formada += "*"

    print("Palavra Formada:", palavra_formada)

    if palavra_formada == palavra_secreta:
        print("Você Acertou!")
        print("numeros de tentativas:", tentativas)

        while True:
            opcao_saida = input("você deseja sair? [S] ou [N]: ").lower()
            if len(opcao_saida) > 1:
                print("Digite apenas um valor")
                continue
            elif opcao_saida not in ("s", "n"):
                print("Digite apenas [S] ou [N]")
                continue

            break

        if opcao_saida == "s":
            print("Saindo...")
            break
        os.system("cls" if os.name == "nt" else "clear")
        tentativas = 0
        letras_acertadas = ""
        palavra_secreta = random.choice(lista_de_nomes).lower
