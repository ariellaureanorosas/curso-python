frase = (
    "O python é uma linguagem de programação "
    "multiparadigma. "
    "Python foi criado por Guido van Rossum"
)

indice = 0
quantidade_de_vezes = 0
letra_mais_vezes = ""

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    contador_letra = frase.count(letra_atual)

    if quantidade_de_vezes < contador_letra:
        quantidade_de_vezes = contador_letra
        letra_mais_vezes = letra_atual

    indice += 1

print(
    "A letra que apareceu mais vezes foi "
    f"'{letra_mais_vezes}' que apareceu "
    f"{quantidade_de_vezes} vezes"
)
