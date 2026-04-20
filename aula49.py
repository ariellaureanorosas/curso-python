"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_1 = [10, 20, 30, 40]
lista_2 = [30, 40, 50, 60]
lista_unificada = lista_1 + lista_2
lista_1.extend(lista_2)
print(lista_1)
# # lista[2] = 300
# del lista[2]
# # print(lista)
# lista.append(50)
# lista.pop()
# lista.append(60)
# ultimo_valor = lista.pop()
# print(lista, ultimo_valor)
