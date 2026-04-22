"""
enumerate - enumera iteráveis (indices)
"""

lista = ["Ariel", "laureano", "Rosas"]
lista.append("Luiz")

for indice, nome in enumerate(lista):
    print(indice, nome)
