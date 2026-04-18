"""
Iterando strings com while
"""

nome = input("Insira seu nome: ")
# print(nome)
# print(tamanho_do_nome)

contador = 0
novo_nome = ""
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f"*{letra}"
    contador += 1

novo_nome += "*"
print(novo_nome)
