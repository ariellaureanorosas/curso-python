# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)


# lista = [numero for numero in range(10)]
# lista = [numero * 2 for numero in range(10)]

# print(lista)

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# Mapeamento de dados em list comprehension
produtos = [
    {
        "nome": "p1",
        "preco": 20,
    },
    {
        "nome": "p2",
        "preco": 10,
    },
    {
        "nome": "p3",
        "preco": 30,
    },
]
# MAPEAMENTO
novos_produtos = [
    (
        {**produto, "preco": produto["preco"] * 2}
        if produto["preco"] > 20
        else {**produto}
    )
    for produto in produtos
]

# print(*novos_produtos, sep="\n")
# lista = [n for n in range(10) if n < 5]

# FILTRO
novos_produtos = [{**produto} for produto in produtos if produto["preco"] > 10]
# Posso combinar o filter com o mapeamento
novos_produtos = [
    (
        {**produto, "preco": produto["preco"] * 1.05}
        if produto["preco"] >= 20
        else {**produto}
    )
    for produto in produtos
    if (produto["preco"] >= 20 and produto["preco"] * 1.05) > 10
]
p(novos_produtos)
