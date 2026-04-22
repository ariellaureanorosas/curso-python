"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
+ - aponta para o mesmo valor na memória (mutável)
"""

lista_1 = ["Ariel", 10, True]
lista_2 = lista_1  # Aponta para o mesmo valor na memória
lista_1[1] = "Rosas"
print(lista_2)
