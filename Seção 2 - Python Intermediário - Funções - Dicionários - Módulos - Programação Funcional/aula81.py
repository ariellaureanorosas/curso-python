# Exemplo de uso dos sets

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


letras = set()
while True:
    if len(letras) != 0:
        print(letras)

    letra_input = input("Digite a letra: ").lower()

    if len(letra_input) > 1:
        limpar_tela()
        print("Digite apenas uma letra")
        continue

    if not letra_input.isalpha():
        limpar_tela()
        print("digite apenas letra")
        continue

    if letra_input in letras:
        limpar_tela()
        print("essa letra já foi digitada")

    letras.add(letra_input)
    limpar_tela()

    if "l" in letras:
        print("parabéns você encontrou a letra misteriosa")
        break
